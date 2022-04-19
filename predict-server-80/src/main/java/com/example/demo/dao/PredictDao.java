package com.example.demo.dao;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.demo.pojo.Predict;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface PredictDao extends BaseMapper<Predict> {
}
