-- 创建预测过的新闻文本的数据库
create database if not exists predict_data character set utf8;
use predict_data;
-- 创建data表
create table if not exists predict
(
	id int primary key AUTO_INCREMENT, -- 自增主键
    url varchar(80) default "无",  -- 新闻链接
    algorithm varchar(40),  -- 预测使用的算法
    method varchar(40),  -- 预测使用的方法
    pretext longtext,  -- 文本内容
    pretype varchar(40) -- 新闻类型
)character set utf8;