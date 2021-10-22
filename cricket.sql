
DROP DATABASE IF EXISTS `WORLDCUP`;
CREATE SCHEMA `WORLDCUP`;

use WORLDCUP;

DROP TABLE IF  exists `CRICKETER`;


CREATE TABLE `CRICKETER`(
`Cricketer_Id` int(10) NOT NULL,
`FName` char(20) NOT NULL,
`LName` char(20) NOT NULL,
`Wickets_Taken` int(5) NOT NULL DEFAULT 0,
`Matches_Played` int(5) NOT NULL DEFAULT 0,
`Runs_Scored` int(7) NOT NULL DEFAULT 0,
`Batsman_Rank` int(4),
`Team_Id` int(10) NOT NULL,
`Batsman_Points` int(10) NOT NULL DEFAULT 0,
Primary key(`Cricketer_Id`)
-- foreign key (`Team Id`) references `TEAMS_AND_PERFORMANCE` (`Team Id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;
create trigger `abc` 
before INSERT 
on 
CRICKETER 
for each row 
set NEW.Batsman_Points := NEW.Runs_Scored/NEW.Matches_Played;


DROP TABLE IF EXISTS `TEAMS_AND_PERFORMANCE`;

CREATE TABLE `TEAMS_AND_PERFORMANCE`(
`Team_Id` int(10) NOT NULL,
`Team_Name` char(20) NOT NULL,
-- `Matches_Played` int(5) NOT NULL DEFAULT 0,
-- `Matches_Lost` int(5) NOT NULL DEFAULT 0,
-- `No_Result_Tie` int(5) NOT NULL DEFAULT 0,
-- `Matches_Won` int(5) NOT NULL DEFAULT 0,
-- `Rank` int(3), 
-- `Points` int(3) NOT NULL DEFAULT 0,
`Team_Captain_CRICKETER_ID` int(12),
primary key(`Team_Id`)
-- unique key `Team_Captain_CRICKETER_ID` (`Team_Captain_CRICKETER_ID`)
-- FOREIGN KEY (`Team Captain CRICKETER ID`) REFERENCES `CRICKETER` (`Cricketer Id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

lock tables `TEAMS_AND_PERFORMANCE` write;

-- INSERT INTO `TEAMS_AND_PERFORMANCE` VALUES(1,'India',100,0,0,100,1,200,1);
-- INSERT INTO `TEAMS_AND_PERFORMANCE` VALUES(2,'Sri Lanka',84,42,0,42,2,84,2);
-- INSERT INTO `TEAMS_AND_PERFORMANCE` VALUES(3,'South Africa',100,100,0,0,4,0,3);
-- INSERT INTO `TEAMS_AND_PERFORMANCE` VALUES(4,'England',56,0,56,0,3,56,4);
INSERT INTO `TEAMS_AND_PERFORMANCE` VALUES(1,'India',1);
INSERT INTO `TEAMS_AND_PERFORMANCE` VALUES(2,'Sri Lanka',2);
INSERT INTO `TEAMS_AND_PERFORMANCE` VALUES(3,'South Africa',3);
INSERT INTO `TEAMS_AND_PERFORMANCE` VALUES(4,'England',4);

unlock tables;

lock tables `CRICKETER` write;

INSERT INTO `CRICKETER` VALUES(1,'Virat','Kohli',0,100,10000,1,1,900);
INSERT INTO `CRICKETER` VALUES(2,'Lasith','Malinga',500,100,100,4,2,30);
INSERT INTO `CRICKETER` VALUES(3,'AB','Devilliers',0,100,8000,2,3,700);
INSERT INTO `CRICKETER` VALUES(4,'Ben','Stokes',50,100,5000,3,4,400);
-- INSERT INTO `CRICKETER` VALUES(1,'Virat','Kohli',0,100,10000,1,1);
-- INSERT INTO `CRICKETER` VALUES(2,'Lasith','Malinga',500,100,100,4,2);
-- INSERT INTO `CRICKETER` VALUES(3,'AB','Devilliers',0,100,8000,2,3);
-- INSERT INTO `CRICKETER` VALUES(4,'Ben','Stokes',50,100,5000,3,4);


unlock tables;


ALTER TABLE `CRICKETER`
ADD FOREIGN KEY (`Team_Id`) REFERENCES `TEAMS_AND_PERFORMANCE`(`Team_Id`);

ALTER TABLE `TEAMS_AND_PERFORMANCE`
ADD FOREIGN KEY (`Team_Captain_CRICKETER_ID`) REFERENCES `CRICKETER`(`Cricketer_Id`);


drop table if exists `CAPTAIN`;

create table `CAPTAIN`(
`Cricketer_Id` int(10) NOT NULL,
`Captain_Id` int(10) NOT NULL,
primary key(`Cricketer_Id`),
constraint `CAPTAIN_ibfk_1` foreign key(`Cricketer_Id`) references `CRICKETER` (`Cricketer_Id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;




DROP table IF EXISTS `MAN_OF_THE_MATCH`;

CREATE TABLE `MAN_OF_THE_MATCH`(
`Cricketer_Id` int(10) NOT NULL,
`Team_Id` int(10) NOT NULL,
primary key(`Cricketer_Id`),
constraint `MAN_OF_THE_MATCH_ibfk_1` foreign key(`Cricketer_Id`) references `CRICKETER` (`Cricketer_Id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;





drop table if exists `WORLD_CUP_MATCHES`;

CREATE TABLE `WORLD_CUP_MATCHES`(
`Match_Id` int(10) NOT NULL,
`Margin` char(40),
`MOM_Cricketer_Id` int(10) NOT NULL,
`First_Team_Id` int(10) NOT NULL,
`Second_Team_Id` int(10) NOT NULL CHECK (`First_Team_Id`<>`Second_Team_Id`),
`Won_By_Team_Id` int(10) NOT NULL,
 -- CHECK (`Won By Team Id`==`First Team Id` OR `Won By Team Id`==`Second Team Id`),
primary key(`Match_Id`),
constraint `WORLD_CUP_MATCHES_ibfk_1` foreign key(`MOM_Cricketer_Id`) references `MAN_OF_THE_MATCH` (`Cricketer_Id`),
constraint `WORLD_CUP_MATCHES_ibfk_2` foreign key(`First_Team_Id`) references `TEAMS_AND_PERFORMANCE` (`Team_Id`),
constraint `WORLD_CUP_MATCHES_ibfk_3` foreign key(`Second_Team_Id`) references `TEAMS_AND_PERFORMANCE` (`Team_Id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;




DROP TABLE IF EXISTS `MOM_MATCHES_INFO`;

CREATE TABLE `MOM_MATCHES_INFO`(
`Cricketer_Id` int(10) NOT NULL,
`Match_Id` int(10) NOT NULL,
primary key(`Cricketer_Id`,`Match_Id`),
constraint `MOM_MATCHES_INFO_ibfk_1` foreign key(`Cricketer_Id`) references  `MAN_OF_THE_MATCH` (`Cricketer_Id`),
constraint `MOM_MATCHES_INFO_ibfk_2` foreign key(`Match_Id`) references `WORLD_CUP_MATCHES` (`Match_Id`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;



lock tables `CAPTAIN` write;

INSERT INTO `CAPTAIN` VALUES(1,1);
INSERT INTO `CAPTAIN` VALUES(2,2);
INSERT INTO `CAPTAIN` VALUES(3,3);

unlock tables;

lock tables `MAN_OF_THE_MATCH` write;

INSERT INTO `MAN_OF_THE_MATCH` VALUES(1,1);
INSERT INTO `MAN_OF_THE_MATCH` VALUES(2,2);

unlock tables;

lock tables `WORLD_CUP_MATCHES` write;

INSERT INTO `WORLD_CUP_MATCHES` VALUES(1,'WON BY 2 RUNS',1,1,2,1);
INSERT INTO `WORLD_CUP_MATCHES` VALUES(2,'WON BY 2 RUNS',1,1,3,1);
INSERT INTO `WORLD_CUP_MATCHES` VALUES(3,'WON BY 2 RUNS',2,2,3,2);

unlock tables;



lock tables `MOM_MATCHES_INFO` write;

insert into `MOM_MATCHES_INFO` VALUES(1,1);
insert into `MOM_MATCHES_INFO` VALUES(1,2);
insert into `MOM_MATCHES_INFO` VALUES(2,3);

unlock tables;






