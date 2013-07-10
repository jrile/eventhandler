connect '/var/lib/firebird/data/events.fdb';
commit;
drop table events;
drop table emails;

create domain boolean
as smallint
check(value is null or value in (0,1));

create table events (event_name varchar (50) primary key, 
email_title varchar(50),
email_text varchar(1000),
sender_email varchar(50),
attach_purchase_order_report boolean
);


-- master/detail table was not working with composite PK, so I made a unique ID (generator below)
create table emails (id integer primary key,
event_name varchar (50) not null,
email_address varchar(50) not null,
unique(event_name, email_address));

create generator gen_email_id;
set generator gen_email_id to 0;
set term ^ ;
create trigger email_id for emails
active before insert position 0
as
begin
if (new.id is null) then new.id = gen_id(gen_email_id, 1);
end^
set term ; ^				
