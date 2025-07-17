USE HMS;

# QUERIES BEGI TO INTER

SELECT * FROM PATIENT p JOIN appointment app on p.id = app.id ;

SELECT * FROM PATIENT P JOIN patientsattendappointments PATT ON P.ID = PATT.APPT;

SELECT * FROM PATIENT P JOIN medicalhistory MH ON P.ID = MH.ID ;

SELECT * FROM patient P JOIN DIAGNOSE DIA ON P.ID = DIA.APPT;

SELECT * FROM docshaveschedules DOCS JOIN schedule SCH ON DOCS.SCHED = SCH.ID;

-- all paient which had a crocin medication, show there name adn other infomation
SELECT * FROM PATIENT P JOIN medicalhistory MH ON P.ID = MH.ID where medication = 'crocin' ;
