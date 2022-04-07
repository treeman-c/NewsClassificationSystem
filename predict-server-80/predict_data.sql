-- 创建预测过的新闻文本的数据库
create database if not exists predict_data character set utf8;
use predict_data;
-- 创建data表
create table if not exists predict
(
	id int primary key AUTO_INCREMENT, -- 自增主键
    url char(20),  -- 新闻链接
    text text,  -- 文本内容
    type char(20) -- 新闻类型
)character set utf8;