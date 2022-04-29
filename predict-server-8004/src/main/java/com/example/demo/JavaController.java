package com.example.demo;


import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.demo.pojo.Predict;
import com.example.demo.server.IPredict;
import com.example.demo.server.Imp.PredictServeImp;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import com.google.common.collect.Maps;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import javax.servlet.http.HttpServletRequest;
import java.util.*;

@CrossOrigin(value = {"http://localhost:8080"})  //跨域问题注解
@RestController
public class JavaController {

    public static final String REDIS_KEY = "predict:";  //redis的key前缀，可以更改任意值
    @Autowired
    private RestTemplate restTemplate;

    @Autowired
    private IPredict predict;

    @Autowired
    private RedisTemplate<String,String> redisTemplate;

    private final ObjectMapper objectMapper = new ObjectMapper();

    @RequestMapping("/java-user")
    public String JavaUser() {
        return "{'username': 'java', 'password': 'java'}"  ;
    }

    @RequestMapping("/python-user")
    public String PythonUser() {
        return restTemplate.getForEntity("http://py-sidecar/getUser", String.class).getBody();
    }


    @RequestMapping(value = "/predictData", method = RequestMethod.POST)
    public IPage getPredictData (@RequestBody Map<String, String> params, HttpServletRequest request) {
        IPage page = new Page(Long.parseLong(params.get("current")),Long.parseLong(params.get("size")));
        return predict.page(page);
    }

    @RequestMapping(value = "/updataById", method = RequestMethod.POST)
    public boolean updataById (@RequestBody Map<String, String> params, HttpServletRequest request) {
        Predict body = new Predict();
        body.setId(Integer.valueOf(params.get("id")));
        body.setMethod(params.get("method"));
        body.setAlgorithm(params.get("algorithm"));
        body.setPretext(params.get("pretext"));
        body.setPretype(params.get("pretype"));
        body.setUrl(params.get("url"));
        boolean flag = false;
        if (predict.updateById(body)){
            flag = true;
        }
        String key = REDIS_KEY + body.getId();
        redisTemplate.opsForValue().set(key,JSON.toJSONString(body));
        return flag;
    }
    @RequestMapping(value = "/findByOrder", method = RequestMethod.POST)
    public IPage findByorder (@RequestBody Map<String, String> params, HttpServletRequest request) {
        IPage page = new Page(Long.parseLong(params.get("current")),Long.parseLong(params.get("size")));
        QueryWrapper<Predict> queryWrapper = new QueryWrapper<>();
        List<String> pretypes = JSON.parseArray(params.get("pretype"), String.class);
        List<String> methods = JSON.parseArray(params.get("method"), String.class);
        List<String> algorithms = JSON.parseArray(params.get("algorithm"), String.class);
        if(params.get("id")!=null&&!params.get("id").equals("")){
            String key = REDIS_KEY + params.get("id");
            Predict pred =JSON.parseObject((String) redisTemplate.opsForValue().get(key),Predict.class);
            if(pred!=null){
                List<Predict> lists = new ArrayList<>();
                lists.add(pred);
                page.setRecords(lists);
                System.out.println("命中缓存");
                return page;
            }
            System.out.println("未命中缓存"+params.get("id"));
            queryWrapper.eq("id",Integer.valueOf(params.get("id")));
            predict.page(page,queryWrapper);
            return page;
        }
        if(pretypes!=null&&!pretypes.isEmpty()){
           queryWrapper.in("pretype",pretypes);
        }
        if(algorithms!=null&&!algorithms.isEmpty()){
            queryWrapper.in("algorithm",algorithms);
        }
        if(methods!=null&&!methods.isEmpty()){
            queryWrapper.in("method",methods);
        }
        predict.page(page,queryWrapper);
        System.out.println(page.toString());
        return page;
    }

    @RequestMapping(value = "/deleteById", method = RequestMethod.POST)
    public boolean deleteById (@RequestBody Map<String, String> params, HttpServletRequest request) {
        boolean flag = false;
        if (predict.removeById(Integer.valueOf(params.get("id")))){
            flag = true;
        }
        String key = REDIS_KEY + params.get("id");
        redisTemplate.delete(key);
        return flag;
    }


    /* *
     * @author treeman
     * @date 2022/3/29 21:12
     * 调用python机器学习的贝叶斯分类器
     * 使用网易链接进行分类
     * @return 返回完整的查询数据和文本
     */
    @RequestMapping(value = "/bayes-url", method = RequestMethod.POST)
    public Predict aopbayes_url (@RequestBody Map<String, String> params, HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        MultiValueMap<String, String> mapurl = new LinkedMultiValueMap<>();
        body.setUrl(params.get("url"));

        try{
            mapurl.add("url",body.getUrl());
            HttpEntity<MultiValueMap<String, String>> httpEntity =
                    new HttpEntity<MultiValueMap<String, String>>(mapurl, headers);
            body.setPretext(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/urlToText", httpEntity, String.class)));
//            System.out.println("请求text参数是："+ unicodeToUtf8(body.getText()));
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/bayes_text", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }

    /* *
     * @author treeman
     * @date 2022/3/29 21:12
     * 调用python机器学习的贝叶斯分类器
     * 使用文本直接分类
     * @return 返回完整的查询数据和文本
     */
    @RequestMapping(value = "/bayes-text", method = RequestMethod.POST)
    public Predict aopbayes_text(@RequestBody Map<String, String> params,HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        body.setUrl("");
        try{
            body.setPretext(params.get("text"));
//            System.out.println(body.getText());
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/bayes_text", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }


    /* *
     * @author treeman
     * @date 2022/3/29 21:12
     * 调用python机器学习的支持向量机分类器
     * 使用网易链接进行分类
     * @return 返回完整的查询数据和文本
     */
    @RequestMapping(value = "/svm-url", method = RequestMethod.POST)
    public Predict aopsvm_url (@RequestBody Map<String, String> params,HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        MultiValueMap<String, String> mapurl = new LinkedMultiValueMap<>();
        body.setUrl(params.get("url"));
        try{
            mapurl.add("url",body.getUrl());
            HttpEntity<MultiValueMap<String, String>> httpEntity =
                    new HttpEntity<MultiValueMap<String, String>>(mapurl, headers);
            body.setPretext(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/urlToText", httpEntity, String.class)));
//            System.out.println("请求text参数是："+ body.getText());
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/svm_text", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }

    /* *
     * @author treeman
     * @date 2022/3/29 21:12
     * 调用python机器学习的支持向量机分类器
     * 使用文本直接分类
     * @return 返回完整的查询数据和文本
     */
    @RequestMapping(value = "/svm-text", method = RequestMethod.POST)
    public Predict aopsvm_text(@RequestBody Map<String, String> params,HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        body.setUrl("");
        try{
            body.setPretext(params.get("text"));
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/svm_text", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }

    /* *
     * @author treeman
     * @date 2022/3/29 21:12
     * 调用python机器学习的K最近邻分类器
     * 使用网易链接进行分类
     * @return 返回完整的查询数据和文本
     */
    @RequestMapping(value = "/knn-url", method = RequestMethod.POST)
    public Predict aopknn_url (@RequestBody Map<String, String> params,HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        MultiValueMap<String, String> mapurl = new LinkedMultiValueMap<>();
        body.setUrl( params.get("url"));
        try{
            mapurl.add("url",body.getUrl());
            HttpEntity<MultiValueMap<String, String>> httpEntity =
                    new HttpEntity<MultiValueMap<String, String>>(mapurl, headers);
            body.setPretext(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/urlToText", httpEntity, String.class)));
//            System.out.println("请求text参数是："+ unicodeToUtf8(body.getText()));
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/knn_text", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }

    /* *
     * @author treeman
     * @date 2022/3/29 21:12
     * 调用python机器学习的K最近邻分类器
     * 使用文本直接分类
     * @return 返回完整的查询数据和文本
     */
    @RequestMapping(value = "/knn-text", method = RequestMethod.POST)
    public Predict aopknn_text(@RequestBody Map<String, String> params,HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        body.setUrl("");
        try{
            body.setPretext(params.get("text"));
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/knn_text", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }


    /* *
     * @author treeman
     * @date 2022/3/29 21:12
     * 调用python机器学习的bp神经网络分类器
     * 使用网易链接进行分类
     * @return 返回完整的查询数据和文本
     */
    @RequestMapping(value = "/bp-url", method = RequestMethod.POST)
    public Predict aopbp_url (@RequestBody Map<String, String> params,HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        MultiValueMap<String, String> mapurl = new LinkedMultiValueMap<>();
        body.setUrl( params.get("url"));
        try{
            mapurl.add("url",body.getUrl());
            HttpEntity<MultiValueMap<String, String>> httpEntity =
                    new HttpEntity<MultiValueMap<String, String>>(mapurl, headers);
            body.setPretext(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/urlToText", httpEntity, String.class)));
//            System.out.println("请求text参数是："+ unicodeToUtf8(body.getText()));
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/bp_text", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }

    /* *
     * @author treeman
     * @date 2022/3/29 21:12
     * 调用python机器学习的bp神经网络分类器
     * 使用文本直接分类
     * @return 返回完整的查询数据和文本
     */
    @RequestMapping(value = "/bp-text", method = RequestMethod.POST)
    public Predict aopbp_text(@RequestBody Map<String, String> params,HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        body.setUrl("");
        try{
            body.setPretext(params.get("text"));
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/bp_text", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }

    @RequestMapping(value = "/intelligent-text", method = RequestMethod.POST)
    public Predict aopit_text(@RequestBody Map<String, String> params,HttpServletRequest request) {
        Predict body = new Predict();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        body.setUrl("");
        try{
            body.setPretext(params.get("text"));
            MultiValueMap<String, String> maptext = new LinkedMultiValueMap<>();
            maptext.add("text",body.getPretext());
            HttpEntity<MultiValueMap<String, String>> httpEntity1 =
                    new HttpEntity<MultiValueMap<String, String>>(maptext ,headers);
            body.setPretype(unicodeToUtf8(restTemplate.postForObject("http://py-sidecar/python/intelligent_type", httpEntity1, String.class)));
        }catch (Exception e){
            body.setPretext("链接错误请检查，目前仅支持网易新闻链接");
            return body;
        }
//        System.out.println(body);
        return body;
    }

/* *
 * @date 2022/3/31 16:46
 * @param [theString] Unicode编码的字符串
 * @return java.lang.String  utf-8编码的字符串
 */
    public static String unicodeToUtf8(String theString) {
        char aChar;
        int len = theString.length();
        StringBuffer outBuffer = new StringBuffer(len);
        for (int x = 0; x < len;) {
            aChar = theString.charAt(x++);
            if (aChar == '\\') {
                aChar = theString.charAt(x++);
                if (aChar == 'u') {
                    // Read the xxxx
                    int value = 0;
                    for (int i = 0; i < 4; i++) {
                        aChar = theString.charAt(x++);
                        switch (aChar) {
                            case '0':
                            case '1':
                            case '2':
                            case '3':
                            case '4':
                            case '5':
                            case '6':
                            case '7':
                            case '8':
                            case '9':
                                value = (value << 4) + aChar - '0';
                                break;
                            case 'a':
                            case 'b':
                            case 'c':
                            case 'd':
                            case 'e':
                            case 'f':
                                value = (value << 4) + 10 + aChar - 'a';
                                break;
                            case 'A':
                            case 'B':
                            case 'C':
                            case 'D':
                            case 'E':
                            case 'F':
                                value = (value << 4) + 10 + aChar - 'A';
                                break;
                            default:
                                throw new IllegalArgumentException(
                                        "Malformed   \\uxxxx   encoding.");
                        }
                    }
                    outBuffer.append((char) value);
                } else {
                    if (aChar == 't')
                        aChar = '\t';
                    else if (aChar == 'r')
                        aChar = '\r';
                    else if (aChar == 'n')
                        aChar = '\n';
                    else if (aChar == 'f')
                        aChar = '\f';
                    outBuffer.append(aChar);
                }
            } else
                outBuffer.append(aChar);
        }
        return outBuffer.toString();
    }

}
