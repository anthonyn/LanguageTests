
###outputs are: ######8 SCORES displays
# ### 8 BETS displays, which will show XX 's between rounds, until bets are gotten
# ###1 st, 2 nd, 3 rd places(with possible ties)
### a display that shows the Current Round### an "X" that toggles between two displays, only works before the game starts
###### inputs: ###the RESET button should be a power switchfor the system.
###the other buttons should do what the buttons do###
import simplegui
import  random
import math
scores = [100, 100, 100, 100, 100, 100, 100, 100]
bets = [0, 0, 0, 0, 0, 0, 0, 0]
places = [1, 1, 1, 1, 1, 1, 1, 1]
button_press_count = 0
current_round = 0
rounds_limit = 10
button_msg = "NEXT!"
rules = "Winner Takes All"
big_X_coord = (10, 395)
def reset_game():

  global scores, bets, button_press_count, current_round
  for i in range(0, 8):
    scores[i] = 100;
    bets[i] = 0;
    places[i] = 1
    button_press_count = 0;

    current_round = 0

    def adv_button():
      global button_press_count, button_msg, current_round, \
      scores, bets, places, sorted_array_scores

      if current_round <= rounds_limit - 1:
  if button_press_count % 2 == 0: ###'GET BETS'
    for i in range(0, 8):
      bets[i] = bet_getter(scores[i], places[i])
else :###'APPLY win/losses'
for i in range(0, 8):
  scores[i] = scores[i] + random.randint(-1, 1) * bets[i]
  for i in range(0, 8):
    bets[i] = "xx"
    button_press_count = button_press_count + 1;
current_round = int(button_press_count / 2)# gets Players ' current Places
sorted_array_scores = sorted(scores, reverse = True)
for i in range(0, 8):
  places[i] = sorted_array_scores.index(scores[i]) + 1
  def change_rules():
  global rules, big_X_coord# can only change rules at beginning of game
  if button_press_count == 0:
    if rules == "Winner Takes All":
      rules = "1,2,3 = 50,30,20";
      big_X_coord = (10, 445)
    else :
      rules = "Winner Takes All";
      big_X_coord = (10, 395)

def bet_getter(score, place): #going to have to do some work on this one...
a, c, k = 12, 36, .55

place = float(place);

mu = int(20 + (26 / (1 + 12 * math.e ** (-k * place))));

bet = abs(int(random.normalvariate(mu, 15)));

return bet

# define draw handler
def draw_handler(canvas):

#draw the scores
for i in range(0, 8):
  if i < 4:
    canvas.draw_text(str(scores[i]), (10 + 110 * i, 150), 40, "White");
  else :
  canvas.draw_text(str(scores[i]), (10 + 110 * (i - 4), 250), 40, "White");#
  draw the bets
  for i in range(0, 8):
    if i < 4:
      canvas.draw_text(str(bets[i]), (60 + 110 * i, 100), 30, "Red");
    else :
  canvas.draw_text(str(bets[i]), (60 + 110 * (i - 4), 200), 30, "Red");#
  draw the places
  for i in range(0, 8):
    if i < 4:
      if places[i] <= 3:
        canvas.draw_text(str(places[i]), (10 + 110 * i, 100), 40, "Green");
      else :
        if places[i] <= 3:
          canvas.draw_text(str(places[i]), (10 + 110 * (i - 4), 200), 40, "Green");
          if current_round == rounds_limit:
            canvas.draw_text("FINAL SCORES!!!!", (10, 50), 30, "White");
          else :
  canvas.draw_text(str(current_round) + " Rounds Done", (10, 50), 30, "White");#
  these are the two toggle spots, pre - start
  canvas.draw_polygon([(10, 400), (40, 400), (40, 360), (10, 360)], 5, "White");
  canvas.draw_polygon([(10, 450), (40, 450), (40, 410), (10, 410)], 5, "White");
  canvas.draw_text("X", big_X_coord, 40, "White");

#
create frame
frame = simplegui.create_frame("Big Board", 500, 500)# register event handlers
frame.add_button("Reset", reset_game, 100);
frame.add_button(button_msg, adv_button, 100);
frame.add_button("Change Rules - only works before Start of Game", change_rules, 100);
frame.set_draw_handler(draw_handler);##
main
frame.start()
      