package com.example.demo.dao;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.demo.pojo.Classification;
import org.apache.ibatis.annotations.Mapper;

/* *
 * @author treeman
 * @date 2022/3/30 10:16
 * 使用MP自动的实现数据层的基础CRUD，并还有分页功能的实现
 */

@Mapper
public  interface ClassificationDao extends BaseMapper<Classification> {
}
