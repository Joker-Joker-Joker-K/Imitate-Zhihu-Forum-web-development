-- MySQL dump 10.13  Distrib 5.7.36, for Win64 (x86_64)
--
-- Host: localhost    Database: zhihu
-- ------------------------------------------------------
-- Server version	5.7.36-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answers` (
  `答案ID` int(11) NOT NULL AUTO_INCREMENT,
  `问题ID` int(11) NOT NULL,
  `回答者ID` int(11) NOT NULL,
  `点赞数量` int(11) NOT NULL,
  `回答内容` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `回答时间` datetime NOT NULL,
  PRIMARY KEY (`答案ID`),
  KEY `回答者ID_idx` (`回答者ID`),
  KEY `问题ID_idx` (`问题ID`),
  CONSTRAINT `回答者ID` FOREIGN KEY (`回答者ID`) REFERENCES `users` (`用户ID`),
  CONSTRAINT `问题ID` FOREIGN KEY (`问题ID`) REFERENCES `questions` (`问题ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answers`
--

LOCK TABLES `answers` WRITE;
/*!40000 ALTER TABLE `answers` DISABLE KEYS */;
INSERT INTO `answers` VALUES (1,1,1,0,'3','2023-05-25 20:10:21'),(2,1,10,0,'4','2023-05-25 20:15:02'),(3,2,1,0,'1','2023-05-25 20:15:24'),(4,2,1,0,'2','2023-05-27 10:09:47'),(6,3,1,0,'abcdefgh','2023-06-13 14:28:52'),(9,1,1,0,'1+2=3','2023-06-14 10:29:14'),(10,1,1,0,'3','2023-06-17 12:07:29');
/*!40000 ALTER TABLE `answers` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`skip-grants user`@`skip-grants host`*/ /*!50003 TRIGGER `answers_AFTER_INSERT` AFTER INSERT ON answers FOR EACH ROW
BEGIN
	declare id int;
    set id=new.问题ID;
    update questions set 回答数量=回答数量+1 where 问题ID=id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `articals`
--

DROP TABLE IF EXISTS `articals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `articals` (
  `文章ID` int(11) NOT NULL AUTO_INCREMENT,
  `作者用户ID` int(11) NOT NULL,
  `赞同数` int(11) NOT NULL,
  `文章内容` varchar(100) COLLATE utf32_unicode_ci NOT NULL,
  `文章名称` varchar(45) COLLATE utf32_unicode_ci NOT NULL,
  `创作时间` datetime NOT NULL,
  PRIMARY KEY (`文章ID`),
  KEY `作者用户ID` (`作者用户ID`),
  KEY `articals_文章名称_index` (`文章名称`),
  CONSTRAINT `作者用户ID` FOREIGN KEY (`作者用户ID`) REFERENCES `users` (`用户ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf32 COLLATE=utf32_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articals`
--

LOCK TABLES `articals` WRITE;
/*!40000 ALTER TABLE `articals` DISABLE KEYS */;
INSERT INTO `articals` VALUES (2,2,0,'abcdf','英语abc','2023-06-13 14:27:39'),(4,1,0,'那就再来','再来一篇','2023-06-14 12:02:04'),(5,1,0,'内容','写一篇写文章','2023-06-17 12:05:33');
/*!40000 ALTER TABLE `articals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `问题ID` int(11) NOT NULL AUTO_INCREMENT,
  `提问者ID` int(11) NOT NULL,
  `问题名称` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `回答数量` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `提问时间` datetime NOT NULL,
  PRIMARY KEY (`问题ID`),
  UNIQUE KEY `yueshu3` (`问题名称`),
  KEY `提问者ID_idx` (`提问者ID`),
  KEY `questions_问题名称_index` (`问题名称`),
  CONSTRAINT `提问者ID` FOREIGN KEY (`提问者ID`) REFERENCES `users` (`用户ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,1,'1+2=?','7','2023-05-25 19:51:16'),(2,1,'1+0=?','2','2023-05-25 20:02:19'),(3,2,'avc?','2','2023-06-13 14:28:08'),(4,1,'试试能不能发问题？','0','2023-06-14 07:14:46'),(5,2,'测试并发','0','2023-06-16 10:57:48'),(6,1,'一个问题','0','2023-06-17 12:06:16');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`skip-grants user`@`skip-grants host`*/ /*!50003 TRIGGER questions_AFTER_DELETE AFTER DELETE ON questions FOR EACH ROW
BEGIN
	declare id int;
    set id=old.问题ID;
    delete from answers where 问题ID=id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test` (
  `test_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `test_name` varchar(100) NOT NULL,
  PRIMARY KEY (`test_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
INSERT INTO `test` VALUES (1,'dd'),(2,'99'),(3,'00'),(4,'11');
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `用户ID` int(11) NOT NULL AUTO_INCREMENT,
  `用户名` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `用户介绍` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `性别` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  `学号` int(11) NOT NULL,
  `学校` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `院系专业` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `密码` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`用户ID`),
  UNIQUE KEY `用户名` (`用户名`),
  KEY `major_index` (`院系专业`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'关','zhifou_master','男',20281240,'北京交通大学','计算机科学与技术','666'),(2,'李','cat','男',20281244,'北京交通大学','计算机科学与技术','666'),(10,'user_10','该用户没有留下任何痕迹','男',20281239,'Unknown','Unknown','666'),(11,'user_11','该用户没有留下任何痕迹','sex',11,'Unknown','Unknown','666'),(12,'user_12','该用户没有留下任何痕迹','sex',12,'Unknown','Unknown','111'),(13,'user_13','该用户没有留下任何痕迹','sex',13,'Unknown','Unknown','111'),(14,'user_14','该用户没有留下任何痕迹','sex',14,'Unknown','Unknown','1'),(16,'user_16','该用户没有留下任何痕迹','sex',16,'Unknown','Unknown','1'),(17,'user_17','该用户没有留下任何痕迹','sex',17,'Unknown','Unknown','1'),(18,'user_18','该用户没有留下任何痕迹','女',18,'Unknown','Unknown','1'),(19,'王','空空如也','sex',0,'Unknown','Unknown','111');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_articals`
--

DROP TABLE IF EXISTS `v_articals`;
/*!50001 DROP VIEW IF EXISTS `v_articals`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_articals` AS SELECT 
 1 AS `作者用户ID`,
 1 AS `赞同数`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_questions`
--

DROP TABLE IF EXISTS `v_questions`;
/*!50001 DROP VIEW IF EXISTS `v_questions`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_questions` AS SELECT 
 1 AS `问题ID`,
 1 AS `提问者ID`,
 1 AS `问题名称`,
 1 AS `热度`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_users`
--

DROP TABLE IF EXISTS `v_users`;
/*!50001 DROP VIEW IF EXISTS `v_users`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_users` AS SELECT 
 1 AS `用户ID`,
 1 AS `用户名`,
 1 AS `用户介绍`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `v_users_password`
--

DROP TABLE IF EXISTS `v_users_password`;
/*!50001 DROP VIEW IF EXISTS `v_users_password`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `v_users_password` AS SELECT 
 1 AS `用户ID`,
 1 AS `用户名`,
 1 AS `密码`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_articals`
--

/*!50001 DROP VIEW IF EXISTS `v_articals`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`skip-grants user`@`skip-grants host` SQL SECURITY DEFINER */
/*!50001 VIEW `v_articals` AS select `articals`.`作者用户ID` AS `作者用户ID`,sum(`articals`.`赞同数`) AS `赞同数` from `articals` group by `articals`.`作者用户ID` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_questions`
--

/*!50001 DROP VIEW IF EXISTS `v_questions`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`skip-grants user`@`skip-grants host` SQL SECURITY DEFINER */
/*!50001 VIEW `v_questions` AS select `questions`.`问题ID` AS `问题ID`,`questions`.`提问者ID` AS `提问者ID`,`questions`.`问题名称` AS `问题名称`,(`questions`.`回答数量` * 10) AS `热度` from `questions` where (`questions`.`问题ID` < 10) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_users`
--

/*!50001 DROP VIEW IF EXISTS `v_users`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`skip-grants user`@`skip-grants host` SQL SECURITY DEFINER */
/*!50001 VIEW `v_users` AS select `users`.`用户ID` AS `用户ID`,`users`.`用户名` AS `用户名`,`users`.`用户介绍` AS `用户介绍` from `users` where (`users`.`用户ID` < 10) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_users_password`
--

/*!50001 DROP VIEW IF EXISTS `v_users_password`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`skip-grants user`@`skip-grants host` SQL SECURITY DEFINER */
/*!50001 VIEW `v_users_password` AS select `users`.`用户ID` AS `用户ID`,`users`.`用户名` AS `用户名`,`users`.`密码` AS `密码` from `users` where (`users`.`用户ID` > 0) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-18 19:03:30
