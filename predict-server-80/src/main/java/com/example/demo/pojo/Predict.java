package com.example.demo.pojo;

import lombok.Data;

@Data
public class Predict {
    private Integer id;
    private String url;   //链接，可没有
    private  String algorithm;  //分类算法
    private String method;  //分类方法
    private String pretext;   //预测文本
    private String pretype;   //预测分类结果
}
