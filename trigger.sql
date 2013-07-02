SET TERM ^ ;

CREATE TRIGGER test_trig FOR test
ACTIVE AFTER INSERT POSITION 0
AS
BEGIN
	-- before posting event, we could update the last modified date 
	-- in order to be able to get more information about what was
	-- updated if need be.
	POST_EVENT 'test_inserted';
END^

SET TERM ; ^
