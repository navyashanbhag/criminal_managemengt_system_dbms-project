CREATE TABLE `admin` (
  `admin_name` varchar(25) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`admin_name`,`password`)
);

INSERT INTO `admin` VALUES ('kripa','1000'),('navya','1234');

CREATE TABLE `courts` (
  `court_id` int NOT NULL,
  `court_name` varchar(45) DEFAULT NULL,
  `court_type` varchar(45) DEFAULT NULL,
  `court_place` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`court_id`)
);

INSERT INTO `courts` VALUES 
(201,'supreme_court','criminal','Delhi'),
(202,'high court','criminal','Banglore'),
(203,'district court','family','Udupi');

CREATE TABLE `police_info` (
  `police_id` varchar(10) NOT NULL,
  `police_name` varchar(45) DEFAULT NULL,
  `station_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`police_id`),
  KEY `sn_idx` (`station_name`)
);

INSERT INTO `police_info` VALUES 
('101','Naveen','udupi'),
('102','Bhaskar','manglore'),
('103','Annamalai','banglore'),
('105','Suma','mysore'),
('106','Sagar','raichur'),
('108','Sindu','Belagavi'),
('109','Bharat','banglore'),
('110','Shrinivas','raichur'),
('111','Gurudath','udupi'),
('112','NITHIN','kundapura'),
('113','NAVANEETH','Hasan');

CREATE TABLE `criminal_info` (
  `criminal_id` varchar(10) NOT NULL,
  `criminal_name` varchar(45) DEFAULT NULL,
  `crime_name` varchar(45) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `police_id` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`criminal_id`),
  FOREIGN KEY (`police_id`) REFERENCES `police_info` (`police_id`) ON DELETE SET NULL
);

INSERT INTO `criminal_info` VALUES 
('1','sarvesha','pickpocketing','banglore','102'),
('2','gunda','murder','belagavi','103'),
('3','kasabkhan','mob','Banglore','106'),
('5','husen','murder','manglore',NULL),
('6','manja','kidnapping','udupi','103');

CREATE TABLE `station_info` (
  `station_name` varchar(20) NOT NULL,
  `station_incharge` varchar(45) DEFAULT NULL,
  `no_of_cells` int DEFAULT NULL,
  PRIMARY KEY (`station_name`)
);

INSERT INTO `station_info` VALUES 
('Ballary','Jamer',40),
('banglore','Annamalai',40),
('belagavi','Shrikanth',40),
('Chikkamagaluru','Prasad1',60),
('darwad','bhargav',24),
('Dharwad','Sangam',12),
('Hubli','Ram',45),
('manglore','Gururaj',20),
('udupi','Manjunath',12);
