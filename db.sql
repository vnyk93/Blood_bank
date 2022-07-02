create database bloodbank;

create table bloodbank.user(
    userid int AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    email varchar(100) NOT NULL UNIQUE,
    phone varchar(100) UNIQUE,
    bloodgroup varchar(10) NOT NULL,
    password varchar(10) NOT NULL,
    PRIMARY KEY(userid)
);

create table bloodbank.request(
    reqid int AUTO_INCREMENT,
    personname varchar(100) NOT NULL,    
    phone varchar(100) NOT NULL,
    bloodgroup varchar(10) NOT NULL,
    hospital varchar(100) NOT NULL,    
    city varchar(100) NOT NULL,    
    user int,
    FOREIGN KEY(user) REFERENCES bloodbank.user(userid),
    PRIMARY KEY(reqid)
);