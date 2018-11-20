CREATE DATABASE scriptTest;
USE scriptTest;
CREATE TABLE testTable ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );
INSERT INTO testTable ( id, name ) VALUES ( null, 'Sample data' );
