package com.example.demo.aop;


import com.alibaba.fastjson.JSON;
import com.example.demo.pojo.Predict;
import com.example.demo.server.IPredict;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class ControllerAOP {

    public static final String REDIS_KEY = "predict:";

    @Autowired
    private IPredict predictserve;
    @Autowired
    private RedisTemplate<String,String>  redisTemplate;


    @Pointcut("execution(public * com.example.demo.*.aop*(..) )")
    public void point(){
    }

    @Before("point()")
    public void before(){
        System.out.println("进入了前置返回值的处理方法");
    }

    @AfterReturning(pointcut = "point()", returning = "object")
    public void afterReturn(JoinPoint joinPoint, Object object)  {
        System.out.println("进入了后置返回值的处理方法");
        Predict predict =(Predict) object;
        if(predict.getPretext().contains("链接错误")) return;
        String menthod=joinPoint.getSignature().getName();
        String relMethod = "";
        String relAlgorithm = "";
        if(menthod.contains("url")){
            relAlgorithm = returnMenthod(menthod);
            relMethod="url";
        }else if(menthod.contains("text")){
            relAlgorithm = returnMenthod(menthod);
            relMethod="text";
        }else{
            relAlgorithm = "";
            relMethod="";
        }

        predict.setPretext(predict.getPretext().replace("\"",""));
        predict.setPretype(predict.getPretype().replace("\"",""));
        predict.setAlgorithm(relAlgorithm);
        predict.setMethod(relMethod);

        predictserve.save(predict);
        String key = REDIS_KEY+predict.getId();
        redisTemplate.opsForValue().set(key, JSON.toJSONString(predict)); //存入数据库后，保存在缓存中
    }

    public String returnMenthod(String s){
        if (s.contains("bayes")){
            return "bayes";
        }else if(s.contains("svm")){
            return "svm";
        }else if(s.contains("knn")){
            return "knn";
        }else if(s.contains("bp")){
            return "bp";
        }
        else if(s.contains("it")){
            return "intelligent";
        }
        return "";
    }

}
