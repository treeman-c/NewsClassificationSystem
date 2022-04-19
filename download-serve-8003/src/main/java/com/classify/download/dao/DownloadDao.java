package com.classify.download.dao;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.classify.download.pojo.Infomation;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface DownloadDao extends BaseMapper<Infomation> {

}
