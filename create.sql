#CPSC 362 PROJECT
DROP DATABASE IF EXISTS COURSECATALOG;
CREATE DATABASE COURSECATALOG;

USE COURSECATALOG;

CREATE TABLE COURSE(
DEPTCODE			CHAR(4) NOT NULL,
COURSENUM			SMALLINT NOT NULL,
COURSELETTER		CHAR NOT NULL,
COURSENAME			VARCHAR(100) NOT NULL,
COURSEDESCRIPTION	VARCHAR(300),
CREDITS				TINYINT NOT NULL,
GRADCREDIT			BOOL,
MAJMINREQ			BOOL,
PRIMARY KEY (DEPTCODE, COURSENUM, COURSELETTER)
);

CREATE TABLE COURSEPREREQ(
COURSEDEPT			CHAR(4) NOT NULL,
COURSENUM			SMALLINT NOT NULL,
COURSELETTER		CHAR NOT NULL,
PREREQDEPT			CHAR(4) NOT NULL,
PREREQNUM			SMALLINT NOT NULL,
PREREQCOURSELETTER	CHAR,
FOREIGN KEY (COURSEDEPT) REFERENCES COURSE (DEPTCODE),
FOREIGN KEY (COURSENUM) REFERENCES COURSE (COURSENUM),
FOREIGN KEY (COURSELETTER) REFERENCES COURSE (COURSELETTER)
);

CREATE TABLE COREQUISITE(
COURSEDEPT			CHAR(4) NOT NULL,
COURSENUM			SMALLINT NOT NULL,
COURSELETTER		CHAR,
COREQDEPT			CHAR(4) NOT NULL,
COREQNUM			SMALLINT NOT NULL,
COREQCOURSELETTER	CHAR,
FOREIGN KEY (COURSEDEPT) REFERENCES COURSE (DEPTCODE),
FOREIGN KEY (COURSENUM) REFERENCES COURSE (COURSENUM),
FOREIGN KEY (COURSELETTER) REFERENCES COURSE (COURSELETTER)
);
