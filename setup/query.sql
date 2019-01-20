select * from de.CUSTOMER_RELATION_PROFILE
--DEPOSIT--------------------------------------------------------------------------
SELECT * from de.DEPOSIT a where a.DEPOSIT_CODE=6814817;
SELECT * from de.DEPOSIT de where de.id = 1;
----------------------------------------------------------------------------

SELECT min(id), max(id) from DEPOSIT WHERE id >= 1790333 and id <= 6833762;
SELECT id,DEPOSIT_CODE  from DEPOSIT where DEPOSIT_CODE >= 6814805 and DEPOSIT_CODE <= 9000000;

SELECT id,DEPOSIT_CODE  from DEPOSIT WHERE id = 1790333
union
SELECT id,DEPOSIT_CODE  from DEPOSIT WHERE  id = 6833762;

SELECT * from ac.account aac WHERE  aac.ID = 1790335; -- DEPOSIT.id = account.id

SELECT count(*) from ac.account
select * from ac.ACCOUNT aa where aa.id = 6774889;
SELECT * from ac.account where id >= 1790333
SELECT min(id), max(id) from ac.account
SELECT * from ac.account where id = 1790333

SELECT  * FROM de.DEPOSIT_CUSTOMER_RELATION
SELECT * FROM de.PLATFORM
SELECT * FROM de.PRODUCT

select max(id) from de.CUSTOMER_RELATION_PROFILE


SELECT *
FROM user_constraints
where constraint_type = 'R'
where  constraint_name = '<your constraint name>'

SELECT *
FROM ALL_CONSTRAINTS
where constraint_type = 'P'
and  constraint_name LIKE '%ACNT_ID_PK%'

-----------------------------------------------------
select max(id) from ACCOUNT
-----------------------------------------------------


SELECT target.Table_Name, src.*
FROM User_Constraints src
  JOIN User_Constraints target ON src.R_Constraint_Name = target.Constraint_Name
WHERE --src.Table_Name = 'ENTITY'
  src.Constraint_Name like '%ACNT_ID%' and
  src.Constraint_Type = 'R'

-----------------
SELECT de.deposit_test_seq.nextval FROM dual;
SELECT de.deposit_test_seq.currval from dual;


--UPDATE DEPOSIT_CODE------------------------------------------------------------
SELECT min(id), max(id) from DEPOSIT WHERE id >= 1790333 and id <= 6833762;
SELECT count(*) from DEPOSIT WHERE id >= 1790333 and id <= 6833762;
SELECT min(DEPOSIT_CODE), max(DEPOSIT_CODE)  from DEPOSIT WHERE id >= 1790333 and id <= 6833762;
SELECT id,DEPOSIT_CODE  from DEPOSIT where DEPOSIT_CODE >= 6814805 and DEPOSIT_CODE <= 9000000;
SELECT count(*)  from DEPOSIT where DEPOSIT_CODE >= 6814805 and DEPOSIT_CODE <= 20000000;

SELECT DEPOSIT_CODE from DEPOSIT WHERE id >= 1790333 and id <= 6833762;
SELECT * from  ac.account aa WHERE aa.id >= 1790333 and aa.id <= 6833762 and aa.CURRENT_BALANCE < 999999999999999999.0000 ;
-----
UPDATE DEPOSIT
set DEPOSIT.DEPOSIT_CODE = de.deposit_test_seq.nextval
where  id >= 1790333 and id <= 6833762;

COMMIT;

-----LEFT JOIN DEPOSIT > account------------------------------------------------
SELECT de.ID, de.DEPOSIT_CODE, aa.id from de.DEPOSIT de LEFT JOIN ac.account aa on de.ID = aa.ID WHERE aa.id is null
and de.ID >= 1790333 and de.ID <= 6833762;

SELECT count(*) from de.DEPOSIT de LEFT JOIN ac.account aa on de.ID = aa.ID
WHERE aa.id is null
      and de.ID >= 1790333
      and de.ID <= 6833762;


---add to account------------------------------------------------------------------
SELECT sys_guid() from dual;
------------------------------
DECLARE
  c_id ac.account.ID%type;
  CURSOR c_deposit is
    SELECT de.ID
    from de.DEPOSIT de LEFT JOIN ac.account aa on de.ID = aa.ID
    WHERE aa.id is null
     and de.ID >= 1790333
          and de.ID <= 6833762;
BEGIN
  OPEN c_deposit;
  LOOP
    FETCH c_deposit into c_id;
    EXIT WHEN c_deposit%notfound;
    INSERT INTO AC.ACCOUNT
    VALUES (
      c_id,
      sys_guid(),
      1000000.0000, 2994,
      1111,
      'test',
      1,
      1,
      8001,
      112,
      null,
      0.0000,
      9999999999999999999.0000,
      0.0000,
      TO_DATE('2018-05-24 00:00:00', 'YYYY-MM-DD HH24:MI:SS'),
      TO_DATE('2018-05-24 00:00:00', 'YYYY-MM-DD HH24:MI:SS'),
      null,
      null,
      TO_DATE('2018-05-24 00:00:00', 'YYYY-MM-DD HH24:MI:SS'),
      TO_DATE('2018-05-24 00:00:00', 'YYYY-MM-DD HH24:MI:SS'),
      0.0000,
      TO_DATE('2018-05-24 00:00:00', 'YYYY-MM-DD HH24:MI:SS'),
      0.0000,
      0.0000,
      null,
      null,
      null,
      null,
      null,
      null,
      1,
      null);
  END LOOP;
  CLOSE c_deposit;
END;
/

--ac.account---------------------------------------
 UPDATE ac.account
    set ac.account.CURRENT_BALANCE = 999999999999999999
--where  ac.account.id >= 1790333
-----------
select * from ac.account a where a.id=1790333 ;
select max(a.ID) from ac.account a;

---SEQUENCE ---------------------------------------------------------
DROP SEQUENCE ACCOUNT_SEQ;
----------
CREATE SEQUENCE ACCOUNT_SEQ
MINVALUE 1
MAXVALUE 999999999999999999999999999
CACHE 20
start with 6833762
INCREMENT BY 1;

GRANT SELECT on ACCOUNT_SEQ to core;
GRANT SELECT on DE_TEST_SEQ to core;
-----------------------------------------
SELECT *
FROM user_sequences
WHERE sequence_name = 'SEQ_SSO_KEY_AUTHENTICATION';

------
SELECT *-- last_number
FROM   user_sequences
WHERE  sequence_name = 'ACCOUNT_SEQ';
----
SELECT ac.ACCOUNT_SEQ.nextval from dual;
SELECT ac.ACCOUNT_SEQ.currval from dual;

--CHANGE SQUECVE VALUE------
ALTER SEQUENCE ac.ACCOUNT_SEQ INCREMENT BY 6833762;
select ac.ACCOUNT_SEQ.nextval from dual;
ALTER SEQUENCE ac.ACCOUNT_SEQ INCREMENT BY 1;

