#视图操作
#行列子集视图
CREATE VIEW V_users
AS
SELECT *
FROM users WHERE 用户ID<10;

#创建一个用户密码视图
CREATE VIEW V_users_password
AS
SELECT 用户ID, 用户名, 密码
FROM users WHERE 用户ID>0;

#带表达式的视图
CREATE OR REPLACE VIEW V_questions(问题ID,提问者ID,问题名称,热度)
AS
SELECT 问题ID,提问者ID,问题名称,回答数量*10
FROM questions WHERE 问题ID<10;

#分组视图
Create view V_articals(作者用户ID,赞同数)
As select 作者用户ID,sum(赞同数)
From articals
Group by 作者用户ID;

select 作者用户ID
from v_articals
where 赞同数<10;

update V_users
set 用户名='假'
where 用户ID=2;
delete
from V_users
where 用户ID=2;

update V_questions
set 热度=100
where 问题ID=2;
delete
from V_questions
where 问题ID=2;

update V_articals
set 赞同数=100
where 作者用户ID=1;
delete
from V_articals
where 作者用户ID=1;

delete
from questions
where 回答数量<0;
#用户授权

flush privileges;
create user gzk@localhost  IDENTIFIED by '123456';
create user k@localhost  IDENTIFIED by '123456';
select * from mysql.user;

flush privileges;
GRANT ALL PRIVILEGES
on table articals
to gzk@localhost;
GRANT SELECT, INSERT, UPDATE, DELETE
on table questions
to k@localhost;
show grants for gzk@localhost;
show grants for k@localhost;

REVOKE ALL PRIVILEGES
on  articals
from gzk@localhost;
show grants for gzk@localhost;
REVOKE SELECT, INSERT, UPDATE, DELETE
on  questions
from k@localhost;
show grants for k@localhost;

GRANT SELECT(文章ID), INSERT(文章ID), UPDATE(文章ID)
on table articals
to gzk@localhost;
GRANT SELECT(问题ID), INSERT(问题ID,提问者ID,问题名称,回答数量), UPDATE(问题ID)
on table questions
to k@localhost;
show grants for gzk@localhost;
show grants for k@localhost;

select 问题ID
from questions
where 回答数量<10;

REVOKE SELECT(文章ID), INSERT(文章ID), UPDATE(文章ID)
on  articals
from gzk@localhost;
show grants for gzk@localhost;
REVOKE SELECT(问题ID), INSERT(问题ID,提问者ID,问题名称,回答数量), UPDATE(问题ID)
on  questions
from k@localhost;
show grants for k@localhost;

#角色创建

drop role if exists  jiaose;
create role 'jiaose';
grant select on users to jiaose;
grant jiaose to gzk@localhost;
show grants for gzk@localhost;
#revoke 'jiaose' from gzk@localhost;

#完整性设计
INSERT INTO questions values(null,1,'why?',0);
INSERT INTO questions values(2,4,'why',0);
INSERT INTO questions values(2,1,null,0);

alter table questions
add constraint yueshu check ( 回答数量>0 );
INSERT INTO questions value (5,1,'1+2=?',-1);

alter table questions
add constraint yueshu3 unique ( 问题名称 );
INSERT INTO questions value (5,1,'1+1=?',-1);


alter table users add sex char;
alter table users add constraint xingbie check(sex in ('男','女'));
INSERT INTO users value (2,'李','cat','男');
INSERT INTO users value (3,'李','cat','li1');


alter table answers
add constraint yueshu2 foreign key (回答者ID) references users( 用户ID );
INSERT INTO answers value (3,1,'1+2=?',-1);

#存储过程
#单表查找
#根据id查找用户名
drop procedure find_name;
CREATE PROCEDURE find_name(in init_id int)
BEGIN
    DECLARE ID INT;
    SET ID=init_id;
    select * from users
        where 用户ID=ID;
END;
call find_name(1);

drop procedure find_userid;

# 一个完整可用的存储过程
CREATE PROCEDURE find_userid(IN name VARCHAR(50), OUT user_id INT)
BEGIN
    SELECT 用户ID INTO user_id FROM users WHERE 用户名 = name;
END;
CALL find_userid('关', @user_id);
SELECT @user_id AS user_id;


drop procedure insert_user;
#数据插入
#init_id开始插入items条数据
CREATE PROCEDURE insert_user(in init_id int,in items int)
BEGIN
    DECLARE ID INT;
    DECLARE i INT;
    SET i=0;
    SET ID=init_id;
    WHILE i < items DO
        insert into users
            values (ID,CONCAT('user_',ID),'该用户没有留下任何痕迹','sex',ID,'Unknown','Unknown');
        SET i=i+1;
        SET ID=ID+1;
    END WHILE;
    #设置AUTOCOMMIT，让所有insert语句最后统一录入数据
    SET AUTOCOMMIT =0;
END;
call insert_user(10,10);
set autocommit = 1;

#数据删除
#根据init_id删除用户
drop procedure delete_user;
CREATE PROCEDURE delete_user(in init_id int)
BEGIN
    DECLARE ID INT;
    SET ID=init_id;
    delete from users
        where 用户ID=ID;
END;
call delete_user(18);

#数据修改
#根据id修改用户性别
drop procedure update_sex;
CREATE PROCEDURE update_sex(in init_id int,in sex varchar(20))
BEGIN
    update users set 性别=sex
        where 用户ID=init_id;
END;
call update_sex(10,'男');

drop procedure update_usernumber;
CREATE PROCEDURE update_usernumber(in init_id int,in number int)
BEGIN
    DECLARE ID INT;
    DECLARE NUM INT;
    SET ID=init_id;
    SET NUM=number;
    update users set 学号=NUM
        where 用户ID=ID;
END;
call update_usernumber(10,20281239);

#触发器设置
# 数据插入触发器：
# 在answer表插入一条数据后，对question表对应的问题的回答数属性进行update调整，回答数+1。
DROP TRIGGER answers_AFTER_INSERT;
CREATE TRIGGER `answers_AFTER_INSERT` AFTER INSERT ON answers FOR EACH ROW
BEGIN
	declare id int;
    set id=new.问题ID;
    update questions set 回答数量=回答数量+1 where 问题ID=id;
END;
#插入回答
insert into answers values(5,2,1,0,'2',CURRENT_TIMESTAMP);

# 数据更新触发器：
# 当用户修改自己提出的问题后，在question表中对于问题文本进行修改，那么之前的对应回答就没有了意义，所以在answer表中删除这一问题的所有回答。
DROP TRIGGER questions_AFTER_UPDATE;
CREATE TRIGGER questions_AFTER_UPDATE AFTER UPDATE ON questions FOR EACH ROW
BEGIN
	declare id int;
    set id=old.问题ID;
    delete from answers where 问题ID=id;
END;
#插入回答
update questions set 问题名称='1+2=?' where 问题ID=1;

# 数据删除触发器：
# 用户删除了自己提出的问题后，那么之前的对应回答就没有了意义，所以在answer表中删除这一问题的所有回答。
DROP TRIGGER questions_AFTER_DELETE;
CREATE TRIGGER questions_AFTER_DELETE AFTER DELETE ON questions FOR EACH ROW
BEGIN
	declare id int;
    set id=old.问题ID;
    delete from answers where 问题ID=id;
END;


#插入回答
#先设置外键约束检查关闭
SET foreign_key_checks = 0;
delete from questions  where 问题ID=3;
#开启外键约束检查，以保持表结构完整性
SET foreign_key_checks = 1;
#外键完善
ALTER TABLE questions ADD CONSTRAINT  FOREIGN KEY (提问者ID)
REFERENCEs  users(用户ID) ON  DELETE  no action
ALTER TABLE answers ADD CONSTRAINT  FOREIGN KEY (问题ID)
REFERENCEs  questions(问题ID) ON  DELETE  CASCADE ;


#创建索引
ALTER TABLE users ADD INDEX major_index (院系专业);
#删除索引
ALTER TABLE users DROP INDEX major_index;

#删除数据
delete from users where 用户ID>100;

#备份与恢复
#创建一个测试表
CREATE TABLE IF NOT EXISTS `test`(
   `test_id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
   `test_name` VARCHAR(100) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
INSERT INTO test values (1,'aa');

drop table test;

#打开日志
show variables like '%general%';

#并发控制实验
#展示自动提交情况
SHOW VARIABLES LIKE 'autocommit';
#关闭自动提交
SET autocommit =0;

flush privileges;
create user user_1 IDENTIFIED by '123456';
create user user_2 IDENTIFIED by '123456';

select * from mysql.user;

GRANT ALL PRIVILEGES
on table test
to user_1;
GRANT ALL PRIVILEGES
on table test
to user_2;

show grants for user_1;
show grants for user_2;

# mysql -u user_1 -p
# mysql -u user_2 -p
# use zhihu
set autocommit =0;
SHOW VARIABLES LIKE 'autocommit';
start transaction ;
commit ;
select @@tx_isolation;
set session transaction isolation level read uncommitted;
set session transaction isolation level read committed;
set session transaction isolation level repeatable read ;
set session transaction isolation level SERIALIZABLE ;
select * from test;
update test set test_name='dd' where test_id=1;
insert into test values(2,'00');
delete from test where test_id=2;












