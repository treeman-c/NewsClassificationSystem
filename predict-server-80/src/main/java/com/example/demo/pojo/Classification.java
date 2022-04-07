package com.example.demo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data  //get-set-hashcode-equal-tostring函数注解
@NoArgsConstructor  //无参构造函数注解
@AllArgsConstructor  //全参构造函数注解
public class Classification {
    private Integer id;
    private String url;
    private String text;
    private String type;
}
