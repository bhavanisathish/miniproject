
create database studentform;


create table adminlogin(name varchar(50),password varchar(50),department varchar(20),posting varchar(100),emailid varchar(600));

create table studentdetails(name varchar(50),reg_number int(30),roll_number varchar(20),father_name varchar(50),nationality varchar(30),religion varchar(20),caste varchar(50),community varchar(40),sex varchar(15),dateofbirth DATE,course varchar(30),branch varchar(100),admittedon DATE,receiptno int(100) ,receiptdate DATE,mothertongue varchar(60),state varchar(100),present_address varchar(600),taluk varchar(100),city varchar(50),district varchar(60),cell_number int(100),aadhar_number int(100),tcno int(90),issuedon DATE;


INSERT INTO `studentdetails` (`name`, `reg_number`, `roll_number`, `father_name`, `nationality`, `religion`, `caste`, `community`, `sex`, `dateofbirth`, `course`, `branch`, `admittedon`, `receiptno`, `receiptdate`, `mothertongue`, `state`, `present_address`,`taluk`, `city`, `district`, `cell_number`, `aadhar_number`, `tcno`, `issuedon`) VALUES ('Bhavani R', '1715007', '17cs008', 'Rangasamy A', 'Indian', 'Hindu', 'B.C', 'Gowda', 'Female', '2000-03-14', 'B.E', 'C.S.E', '12', '123456789', '2020-01-09', 'Tamil', 'Tamilnadu', '4-2-45 North Raja Street,melachokkanathapuram.', 'bodinayakanur','bodi', 'theni', '9791999076', '123456', '12345', '2020-01-09');	