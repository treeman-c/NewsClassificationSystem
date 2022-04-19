package com.classify.download.server.Imp;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.classify.download.dao.DownloadDao;
import com.classify.download.pojo.Infomation;
import com.classify.download.server.IDownload;
import org.springframework.stereotype.Service;


/* *
 * @author treeman
 * @date 2022/3/30 11:51
 * 使用MP将业务层高效实现
 * 搭建业务层不需要过多的代码，且可以扩展自己需要的功能
 */

@Service
public class DownloadDaoImp extends ServiceImpl<DownloadDao, Infomation > implements IDownload {
}
