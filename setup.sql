drop database test;


create database test;
use test;


create table master_drive (
serial varchar(30) primary key,
drive_name varchar(50) not null,
date_added timestamp,
username varchar(20) not null,
is_backup_of varchar(30));


create table data_folders (
folder_sequence int auto_increment primary key,
serial varchar(30) not null references master_drive,
folder_name varchar(100) not null,
unique index(serial, folder_name));

create table data_files (
file_sequence int auto_increment primary key,
folder_sequence int not null references data_folders,
file_name varchar(100) not null,
unique index(folder_sequence, file_name));

create table location (
serial varchar(30) primary key,
location text);

create table users (
id int auto_increment primary key,
username varchar(20) unique not null,
name varchar(40),
createtime timestamp,
passhash varchar(40) not null,
level int default 1);

insert into users (username, name, passhash, level) values ("test", "test", sha1("test"), 3);
