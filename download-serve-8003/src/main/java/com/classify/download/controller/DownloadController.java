package com.classify.download.controller;


import com.alibaba.fastjson.JSON;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.classify.download.pojo.Infomation;
import com.classify.download.server.Imp.DownloadDaoImp;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import javax.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.URLDecoder;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@CrossOrigin(value = {"http://localhost:8080"})  //跨域问题注解
@RestController
public class DownloadController {

    public static final String REDIS_KEY = "download:";

    @Autowired
    private RestTemplate restTemplate;

    @Autowired
    private DownloadDaoImp download;

    @Autowired
    private RedisTemplate<String,String> redisTemplate;
    /* *
     * @author treeman
     * @date 2022/4/8 9:08
     * 下载应用程序的接口，返回下载数据
     */
    @RequestMapping(value = "/download-file", method = RequestMethod.POST)
    public HttpServletResponse GetData(HttpServletResponse response) throws IOException {
        String path = DownloadController.class.getResource("/downloadfile/newsclassify.rar").getPath();
        BufferedInputStream bf=null;
        BufferedOutputStream bufferedOutputStream=null;
        try {
            path = URLDecoder.decode(path,"utf-8");
            File file  = new File(path);
            System.out.println(file);
            bf = new BufferedInputStream(new FileInputStream(file));
            byte[] bt = new byte[bf.available()];
            System.out.println(bt);
            bf.read(bt);
            System.out.println(bf);
            bf.close();
            bufferedOutputStream = new BufferedOutputStream(response.getOutputStream());
            bufferedOutputStream.write(bt);
            bufferedOutputStream.flush();
        }catch (Exception e){

        }finally {
            try {
                if (bf != null) {
                    bf.close();
                }
            } catch(Exception ex) {
            }
            try {
                if (bufferedOutputStream != null) {
                    bufferedOutputStream.close();
                }
            } catch(Exception ex) {
            }
        }
        return response;
    }


    /* *
     * @author treeman
     * @date 2022/4/8 9:08
     * 下载dataset数据集的接口，返回下载数据
     */
    @RequestMapping(value = "/download-dataset", method = RequestMethod.POST)
    public HttpServletResponse getDataset(HttpServletResponse response) throws IOException {
        String path = DownloadController.class.getResource("/downloadfile/newdata.csv").getPath();
        BufferedInputStream bf=null;
        BufferedOutputStream bufferedOutputStream=null;
        try {
            path = URLDecoder.decode(path,"utf-8");
            File file  = new File(path);
            bf = new BufferedInputStream(new FileInputStream(file));
            byte[] bt = new byte[bf.available()];
            bf.read(bt);
            bf.close();
            bufferedOutputStream = new BufferedOutputStream(response.getOutputStream());
            bufferedOutputStream.write(bt);
            bufferedOutputStream.flush();
        }catch (Exception e){

        }finally {
            try {
                if (bf != null) {
                    bf.close();
                }
            } catch(Exception ex) {
            }
            try {
                if (bufferedOutputStream != null) {
                    bufferedOutputStream.close();
                }
            } catch(Exception ex) {
            }
        }
        return response;
    }

    @RequestMapping(value = "/getData", method = RequestMethod.POST)
    public IPage getAll(@RequestBody Map<String,String> map) {
        String key = REDIS_KEY + map.get("current")+"-"+map.get("size");
        IPage redis_page = JSON.parseObject((String) redisTemplate.opsForValue().get(key),Page.class);
        if(redis_page!=null){
            System.out.println("命中缓存");
            return redis_page;
        }
        IPage page = new Page(new Long(map.get("current")),new Long(map.get("size")));
        download.page(page);
        redisTemplate.opsForValue().set(key,JSON.toJSONString(page));
        return page;
    }

    @RequestMapping(value = "/getData", method = RequestMethod.GET)
    public List<Infomation> getAll1() {
        return download.list();
    }

    @RequestMapping(value = "/train-model", method = RequestMethod.GET)
    public void TrainModel() {
        restTemplate.getForEntity("http://py-sidecar/python/train_model", String.class);
    }
}
