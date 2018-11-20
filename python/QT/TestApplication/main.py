# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import sys
import opc

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# This is our window from QtCreator
import mainwindow_auto

global form

ADDRESS1 = '10.0.0.121:7890'
client1 = opc.Client(ADDRESS1)

global r, g, b
r = 0
g = 0
b = 0



# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

   # lastSend


    def sendValue(self):
        my_pixels = [(r * 100, g * 100, b * 100)] * 64
        client1.put_pixels(my_pixels, channel=0)

    def sendVals(self, r, g, b):
        my_pixels = [(r , g , b )] * 64
        client1.put_pixels(my_pixels, channel=0)

    ### functions for the buttons to call
    def pressedbtnGrid_1(self):
        print ("Pressed On 1!")
        # isFullScreen() ? showNormal(): showFullScreen();
        global r
        if r == 1:
            r = 0
        else:
            r = 1
        self.sendValue()

    def pressedbtnGrid_2(self):
        print ("Pressed On 2!")
        global g
        if g == 1:
            g = 0
        else:
            g = 1
        self.sendValue()

    def pressedbtnGrid_3(self):
        print ("Pressed On 3!")
        global b
        if b == 1:
            b = 0
        else:
            b = 1
        self.sendValue()

    def pressedbtnGrid_4(self):
        print ("Pressed On 4!")
        global r , g, b
        r = 0
        g = 0
        b = 0
        self.sendValue()

    def pressedbtnGrid_5(self):
        print ("Pressed On 5!")

    def pressedbtnGrid_6(self):
        print ("Pressed On 6!")

    def pressedbtnGrid_7(self):
        print ("Pressed On 7!")

    def pressedbtnGrid_8(self):
        print ("Pressed On 8!")

    def pressedbtnGrid_9(self):
        print ("Pressed On 9!")

    def pressedbtnGrid_10(self):
        print ("Pressed On 10!")

    def pressedbtnGrid_11(self):
        print ("Pressed On 11!")

    def pressedbtnGrid_12(self):
        print ("Pressed On 12!")

    def pressedbtnGrid_13(self):
        print ("Pressed On 13!")

    def pressedbtnGrid_14(self):
        print ("Pressed On 14!")

    def pressedbtnGrid_15(self):
        print ("Pressed On 15!")

    def pressedbtnGrid_16(self):
        print ("Pressed On 16!")

    # def slideverticalSliderRed(self):
    #     value = self.verticalSliderRed.value()
    #     print ("red slider value is ", value)
    #     global r
    #     r = value
    #     self.sendValue()
    #
    # def slideverticalSliderGreen(self):
    #     print ("green slider value is ", value)
    #     # global g
    #     # g = value
    #     # self.sendValue()
    #
    # def slideverticalSliderBlue(self):
    #     print ("blue slider value is ", value)
    #     # global b
    #     # b = value
    #     # self.sendValue()

    def slideverticalSlider(self):
        redValue = self.verticalSliderRed.value()
        greenValue = self.verticalSliderGreen.value()
        blueValue = self.verticalSliderBlue.value()
        print("values are", redValue, greenValue, blueValue)
        self.sendVals(redValue, greenValue, blueValue)


    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.btnGrid_1.clicked.connect(lambda: self.pressedbtnGrid_1())
        self.btnGrid_2.clicked.connect(lambda: self.pressedbtnGrid_2())
        self.btnGrid_3.clicked.connect(lambda: self.pressedbtnGrid_3())
        self.btnGrid_4.clicked.connect(lambda: self.pressedbtnGrid_4())
        self.btnGrid_5.clicked.connect(lambda: self.pressedbtnGrid_5())
        self.btnGrid_6.clicked.connect(lambda: self.pressedbtnGrid_6())
        self.btnGrid_7.clicked.connect(lambda: self.pressedbtnGrid_7())
        self.btnGrid_8.clicked.connect(lambda: self.pressedbtnGrid_8())
        self.btnGrid_9.clicked.connect(lambda: self.pressedbtnGrid_9())
        self.btnGrid_10.clicked.connect(lambda: self.pressedbtnGrid_10())
        self.btnGrid_11.clicked.connect(lambda: self.pressedbtnGrid_11())
        self.btnGrid_12.clicked.connect(lambda: self.pressedbtnGrid_12())
        self.btnGrid_13.clicked.connect(lambda: self.pressedbtnGrid_13())
        self.btnGrid_14.clicked.connect(lambda: self.pressedbtnGrid_14())
        self.btnGrid_15.clicked.connect(lambda: self.pressedbtnGrid_15())
        self.btnGrid_16.clicked.connect(lambda: self.pressedbtnGrid_16())

        # self.verticalSliderRed.valueChanged.connect(self.slideverticalSliderRed)
        # self.verticalSliderBlue.valueChanged.connect(self.slideverticalSliderGreen)
        # self.verticalSliderGreen.valueChanged.connect(self.slideverticalSliderBlue)
        self.verticalSliderRed.sliderReleased.connect(self.slideverticalSlider)
        self.verticalSliderBlue.sliderReleased.connect(self.slideverticalSlider)
        self.verticalSliderGreen.sliderReleased.connect(self.slideverticalSlider)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            print ("you pressed esc")
            global form
            form.showFullScreen()
            #isFullScreen() ? showNormal(): showFullScreen();
        if e.key() == Qt.Key_F1:
            print ("you pressed F1")
            global form
            form.showNormal()

# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    global form
    form = MainWindow()
    #form.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
    #form.showFullScreen()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()