use challenge_2;

create table CARS (
	MODEL varchar (10),
    BRAND VARCHAR (10),
    CAR_ID varchar (10),
    RELEASE_DATE DATE );

create table BUYERS (
	LAST_NAME varchar (10),
    FIRST_NAME VARCHAR (10),
    CAR_ID varchar (10),
    MODEL varchar(10),
    PURCHASE_DATE DATE );

create table MODELS (
	CAR_ID varchar (10),
    PRICE VARCHAR (10),
    IN_STOCK varchar (10),
    CAR_TYPE varchar (10),
    RELEASE_DATE DATE );
    
create table MODELS_OPTIONS (
	ID varchar (10),
	FUEL_Y_N varchar (10),
    HYBRID_Y_N VARCHAR (10),
    ELECTRIC_Y_N varchar (10),
    RELEASE_DATE DATE );
    
INSERT INTO CARS (MODEL,BRAND, CAR_ID, RELEASE_DATE) VALUES ('Model6','PSA', '06', '2015-01-01');
 



#Delete from MODELS where car_id = '04'  limit 1; 

INSERT INTO models (car_id, release_date)
  SELECT car_id, C.release_date #colum_name
  FROM CARS C
  where car_id not in (select distinct car_id from models );

INSERT INTO MODELS_OPTIONS (id, release_date)
  SELECT car_id, C.release_date #colum_name
  FROM CARS C
  where car_id not in (select distinct car_id from MODELS_OPTIONS );



INSERT INTO BUYERS (LAST_NAME,FIRST_NAME,CAR_ID,PURCHASE_DATE) VALUES ('GG','MONSIEUR','04','2016-01-01');
  

select 
last_name,
FIRST_NAME,
b.CAR_ID,
c.Model,
PURCHASE_DATE,
Brand
from BUYERS b
left join cars c on c.car_id = b.car_id
order by PURCHASE_DATE desc;