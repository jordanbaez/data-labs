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