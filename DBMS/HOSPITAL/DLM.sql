/*
TABLE NAME:-
Appointment
Patient
MedicalHistory
Doctor
Schedule
PatientsFillHistory
Diagnose
PatientsAttendAppointments
DocsHaveSchedules
DoctorViewsHistory
*/

CREATE DATABASE HMS;
USE HMS;
DROP DATABASE HMS;

CREATE TABLE Appointment(
id int PRIMARY KEY,
date DATE NOT NULL,
starttime TIME NOT NULL,
endtime TIME NOT NULL,
status varchar(15) NOT NULL
);

CREATE TABLE Patient(
id int NOT NULL auto_increment,
email varchar(50) NOT NULL UNIQUE ,
password varchar(30) NOT NULL,
name varchar(50) NOT NULL,
address varchar(60) NOT NULL,
gender VARCHAR(20) NOT NULL,
PRIMARY KEY(id , email)
);

#DROP TABLE patient;

CREATE TABLE MedicalHistory(
id int PRIMARY KEY,
date DATE NOT NULL,
conditions VARCHAR(100) NOT NULL, 
surgeries VARCHAR(100) NOT NULL, 
medication VARCHAR(100) NOT NULL
);

CREATE TABLE Doctor(
doc_id int not null,
email varchar(50) NOT NULL unique,
password varchar(30) NOT NULL,
name varchar(50) NOT NULL,
gender varchar(20) NOT NULL,
PRIMARY KEY(doc_id , email)
);
# drop table doctor;

CREATE TABLE Schedule(
id int NOT NULL,
starttime TIME NOT NULL,
endtime TIME NOT NULL,
breaktime TIME NOT NULL,
day varchar(20) NOT NULL,
PRIMARY KEY (id, starttime, endtime, breaktime, day)
);

CREATE TABLE PatientsFillHistory(
patient varchar(50) NOT NULL,
history int NOT NULL,
FOREIGN KEY (patient) REFERENCES Patient(email) ON DELETE CASCADE,
FOREIGN KEY (history) REFERENCES MedicalHistory(id) ON DELETE CASCADE,
PRIMARY KEY (patient, history)
);

#DROP TABLE PatientsFillHistory;

CREATE TABLE Diagnose(
appt int NOT NULL,
doctor varchar(50) NOT NULL,
diagnosis varchar(40) NOT NULL,
prescription varchar(50) NOT NULL,
FOREIGN KEY (appt) REFERENCES Appointment (id) ON DELETE CASCADE,
FOREIGN KEY (doctor) REFERENCES Doctor (email) ON DELETE CASCADE,
PRIMARY KEY (appt, doctor)
);

CREATE TABLE PatientsAttendAppointments(
patient varchar(50) NOT NULL,
appt int NOT NULL,
concerns varchar(40) NOT NULL,
symptoms varchar(40) NOT NULL,
FOREIGN KEY (patient) REFERENCES Patient (email) ON DELETE CASCADE,
FOREIGN KEY (appt) REFERENCES Appointment (id) ON DELETE CASCADE,
PRIMARY KEY (appt)
);

#DROP TABLE PatientsAttendAppointments;


CREATE TABLE DocsHaveSchedules(
sched int NOT NULL,
doctor varchar(50) NOT NULL,
FOREIGN KEY (sched) REFERENCES Schedule (id) ON DELETE CASCADE,
FOREIGN KEY (doctor) REFERENCES Doctor (email) ON DELETE CASCADE,
PRIMARY KEY (sched, doctor)
);

CREATE TABLE DoctorViewsHistory(
history int NOT NULL,
doctor varchar(50) NOT NULL,
FOREIGN KEY (doctor) REFERENCES Doctor (email) ON DELETE CASCADE,
FOREIGN KEY (history) REFERENCES MedicalHistory (id),
PRIMARY KEY (history, doctor)
);
