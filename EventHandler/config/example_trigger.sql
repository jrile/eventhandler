create table eventreports (id integer not null,
trigger_name varchar (50) not null,
primary key(id, trigger_name));



SET TERM ^ ;

CREATE TRIGGER pr_status_updated FOR CUSTOMSET
ACTIVE BEFORE INSERT POSITION 0
AS
BEGIN
        IF (NEW.INFO='Waiting for Approval') THEN
            POST_EVENT 'pr_status_updated';
            INSERT INTO EVENTREPORTS (RECORDID, TRIGGER_NAME) values (NEW.RECORDID, 'pr_status_updated');
END^

SET TERM ; ^