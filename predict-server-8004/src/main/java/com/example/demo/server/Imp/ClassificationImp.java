package com.example.demo.server.Imp;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.demo.dao.ClassificationDao;
import com.example.demo.pojo.Classification;
import com.example.demo.server.IClassification;
import org.springframework.stereotype.Service;


/* *
 * @author treeman
 * @date 2022/3/30 11:51
 * 使用MP将业务层高效实现
 * 搭建业务层不需要过多的代码，且可以扩展自己需要的功能
 */

@Service
public class ClassificationImp extends ServiceImpl<ClassificationDao,Classification> implements IClassification {
}
