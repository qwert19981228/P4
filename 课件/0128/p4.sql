/*
 Navicat Premium Data Transfer

 Source Server         : P4 yjw
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost:3306
 Source Schema         : p4

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 28/01/2019 18:14:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for salary
-- ----------------------------
DROP TABLE IF EXISTS `salary`;
CREATE TABLE `salary`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL COMMENT 'user表中的用户id',
  `dep` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '部门',
  `money` decimal(10, 2) NOT NULL COMMENT '工资',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of salary
-- ----------------------------
INSERT INTO `salary` VALUES (1, 5, '技术部', 50000.00);
INSERT INTO `salary` VALUES (2, 11, '技术部', 5888.00);
INSERT INTO `salary` VALUES (3, 12, '技术部', 88888.00);
INSERT INTO `salary` VALUES (4, 1, '公关部', 9000.00);
INSERT INTO `salary` VALUES (5, 13, '公关部', 11000.00);
INSERT INTO `salary` VALUES (6, 14, '公关部', 15000.00);
INSERT INTO `salary` VALUES (7, 15, '公关部', 10000.00);
INSERT INTO `salary` VALUES (8, 2, '保安部', 6000.00);
INSERT INTO `salary` VALUES (9, 3, '保安部', 51000.00);
INSERT INTO `salary` VALUES (10, 8, '保安部', 30000.00);
INSERT INTO `salary` VALUES (11, 4, '销售部', 3000.00);
INSERT INTO `salary` VALUES (12, 6, '销售部', 5000.00);
INSERT INTO `salary` VALUES (13, 7, '销售部', 100000.00);
INSERT INTO `salary` VALUES (14, 9, '保洁部', 8000.00);
INSERT INTO `salary` VALUES (15, 10, '财务部', 12000.00);
INSERT INTO `salary` VALUES (16, 16, '财务部', 9000.00);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pwd` char(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '加密32位',
  `tel` char(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sex` tinyint(1) NULL DEFAULT 1 COMMENT '1-男  2-女',
  `birthday` date NULL DEFAULT NULL,
  `address` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `status` tinyint(1) NULL DEFAULT 1,
  `regtime` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `tel`(`tel`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '小王', 'e10adc3949ba59abbe56e057f20f883e', '15000000001', 1, '2002-12-03', '青花楼老宋床底下', 1, 1548384200);
INSERT INTO `user` VALUES (2, '亚瑟', 'e10adc3949ba59abbe56e057f20f883e', '15000000002', 1, '1970-10-01', '召唤师峡谷', 1, 1548384200);
INSERT INTO `user` VALUES (3, '钟馗', 'e10adc3949ba59abbe56e057f20f883e', '15000000003', 1, '1995-11-11', '召唤师峡谷', 2, 1548382600);
INSERT INTO `user` VALUES (4, '老宋', 'e10adc3949ba59abbe56e057f20f883e', '15000000004', 1, '2006-07-18', '宝马车上', 1, 1548382537);
INSERT INTO `user` VALUES (5, '貂蝉', 'e10adc3949ba59abbe56e057f20f883e', '15000000005', 2, '2017-02-13', '吕布or董卓别墅', 1, 1548384240);
INSERT INTO `user` VALUES (6, '本伟', 'e10adc3949ba59abbe56e057f20f883e', '17000000001', 1, '1990-10-10', '绝地海岛监狱', 1, 1548384200);
INSERT INTO `user` VALUES (7, '无名', 'e10adc3949ba59abbe56e057f20f883e', '17000000002', 2, '1941-05-27', NULL, 2, 1548380735);
INSERT INTO `user` VALUES (8, '路飞', 'e10adc3949ba59abbe56e057f20f883e', '17000000003', 1, '1999-09-01', '海贼王岛', 1, 1548384270);
INSERT INTO `user` VALUES (9, '鸣人', 'e10adc3949ba59abbe56e057f20f883e', '17000000004', 1, '1985-12-13', '木叶忍者村', 1, 1548384200);
INSERT INTO `user` VALUES (10, '奥九马', 'e10adc3949ba59abbe56e057f20f883e', '17000000005', 1, '1957-11-25', '黑宫顶层', 1, 1548384204);
INSERT INTO `user` VALUES (11, '晋四', 'e10adc3949ba59abbe56e057f20f883e', '17000000006', 1, '2015-06-06', NULL, 2, 1548384213);
INSERT INTO `user` VALUES (12, '星爷', 'e10adc3949ba59abbe56e057f20f883e', '17000000007', 1, '1962-10-10', '太师华府', 1, 1548381853);
INSERT INTO `user` VALUES (13, '波老师', 'e10adc3949ba59abbe56e057f20f883e', '13000000001', 2, '2000-01-01', '老王隔壁', 1, 1548384200);
INSERT INTO `user` VALUES (14, '苍老师', 'e10adc3949ba59abbe56e057f20f883e', '13000000002', 2, '2001-10-01', '老王隔壁', 1, 1548384259);
INSERT INTO `user` VALUES (15, '小泽', 'e10adc3949ba59abbe56e057f20f883e', '13000000003', 2, '2002-06-01', '老王隔壁', 1, 1548384200);
INSERT INTO `user` VALUES (16, '小飞飞', 'e10adc3949ba59abbe56e057f20f883e', '13000000004', 1, '2009-09-09', '老王下面', 1, 1548384200);

SET FOREIGN_KEY_CHECKS = 1;
