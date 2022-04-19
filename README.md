# NewsClassificationSystem
springcloud整合python语言的新闻文本分类系统
![image](https://user-images.githubusercontent.com/77831973/162118094-7b791632-7f75-44b5-9342-43dabcc3cb0b.png)
# 机器学习
机器学习算法部分，采用具有强大机器学习库的python语言开发，我选用sklearn第三库训练模型。 分类器选择四种进行训练，分别为贝叶斯、支持向量机、K最近邻算法、BP神经网络。 数据集采用的网易新闻的网页内容，python爬虫获取文本内容。 数据集、模型、评价得分都保存为文件形式。
![image](https://user-images.githubusercontent.com/77831973/162118687-206f98ff-8786-4653-9ebe-af5053010f8f.png)
# 系统搭建
系统开发模式采用前后端分离开发，前端使用Vue+Element-ui开发，Axios异步请求信息，echarts可视分类器得分比较。 后端采用spring boot和spring cloud框架搭建微服务后台系统，使用spring cloud Netflix sidecar实现跨语言接口访问， 实现python与Java之间的访问与服务调用。eureka组件管理微服务调用与注册。
![image](https://user-images.githubusercontent.com/77831973/162118628-266cee65-d2ce-48c9-a6eb-d1ebd5407a26.png)
