package com.example.demo.server.Imp;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.demo.dao.PredictDao;
import com.example.demo.pojo.Predict;
import com.example.demo.server.IPredict;
import org.springframework.stereotype.Service;

@Service
public class PredictServeImp extends ServiceImpl<PredictDao, Predict> implements IPredict {
}
