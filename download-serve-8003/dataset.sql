-- 创建dataset数据集的数据库
create database if not exists dataset character set utf8;
use dataset;
-- 创建data表
create table if not exists infomation
(
	id int primary key  AUTO_INCREMENT, -- 自增主键
    url varchar(40),  -- 新闻链接
    text longtext,  -- 文本内容
    type varchar(20) -- 新闻类型
)character set utf8;