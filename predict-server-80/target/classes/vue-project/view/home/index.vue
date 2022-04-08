<template>
    <el-row class="home" :gutter="20">
        <el-col :span="10" style="margin-top: 20px">
            <el-card shadow="hover">
                <el-row  type="flex" justify="center">
                    <div class="user">
                        <img :src="userImg" />
                    </div>
                </el-row>

                    <el-descriptions title="" :column="2">
                        <el-descriptions-item label="作者">TREEMAN-C</el-descriptions-item>
                        <el-descriptions-item label="项目身份">项目作者</el-descriptions-item>
                        <el-descriptions-item label="开发时间">2022-3-21</el-descriptions-item>
                        <el-descriptions-item label="学校">HBGEO</el-descriptions-item>
                    </el-descriptions>

            </el-card>
            <el-divider><i class="el-icon-info"/></el-divider>
            <el-card style="margin-top: 20px;height: 460px;">
                <el-table :data="tabledata">
                    <el-table-column v-for="(val, key) in tabledataheader" :key="key" :prop="key" :label="val">

                    </el-table-column>
                </el-table>
            </el-card>
        </el-col>

        <el-col :span="14" style="margin-top: 20px">
            <el-card shadow="hover">
                <el-descriptions title="项目框架" :column="1">
                    <el-descriptions-item label="后端框架">
                        <el-tag size="small">spring boot 1.5.7</el-tag>
                        <el-tag size="small">spring cloud Dalston.SR3</el-tag>
                    </el-descriptions-item>
                    <el-descriptions-item label="前端框架">
                        <el-tag size="small">node.js v16.14.2</el-tag>
                        <el-tag size="small">@vue/cli 5.0.4</el-tag>
                        <el-tag size="small">yarn 1.22.18</el-tag>
                        <el-tag size="small">npm 8.5.0</el-tag>
                    </el-descriptions-item>
                    <el-descriptions-item label="Maven版本">
                        <el-tag size="small">Apache Maven 3.6.1</el-tag>
                    </el-descriptions-item>
                    <el-descriptions-item label="数据库">
                        <el-tag size="small">MySQL 5.7</el-tag>
                    </el-descriptions-item>
                    <el-descriptions-item label="测试工具">
                        <el-tag size="small">postman</el-tag>
                    </el-descriptions-item>
                </el-descriptions>
            </el-card>
            <el-divider><i class="el-icon-star-on"></i></el-divider>
            <el-card shadow="hover">
                <el-descriptions title="机器学习" :colon="false">
                    <el-descriptions-item label="">
                        机器学习算法部分，采用具有强大机器学习库的python语言开发，我选用sklearn第三库训练模型。
                        分类器选择四种进行训练，分别为贝叶斯、支持向量机、K最近邻算法、BP神经网络。
                        数据集采用的网易新闻的网页内容，python爬虫获取文本内容。
                        数据集、模型、评价得分都保存为文件形式。
                    </el-descriptions-item>
                </el-descriptions>
            </el-card>
            <el-divider><i class="el-icon-star-on"></i></el-divider>
            <el-card shadow="hover">
                <el-descriptions title="系统搭建" :colon="false">
                    <el-descriptions-item label="">
                        系统开发模式采用前后端分离开发，前端使用Vue+Element-ui开发，Axios异步请求信息，echarts可视分类器得分比较。
                        后端采用spring boot和spring cloud框架搭建微服务后台系统，使用spring cloud Netflix sidecar实现跨语言接口访问，
                        实现python与Java之间的访问与服务调用。eureka组件管理微服务调用与注册。
                    </el-descriptions-item>
                </el-descriptions>
            </el-card>
        </el-col>
    </el-row>
</template>

<script>
    import 'element-ui/lib/theme-chalk/display.css';

    export default {
        name:'home',
        data(){
            return {
                userImg: require('../../src/assets/image/headImg.jpeg'),
                tabledata: [
                    {
                        id: '1',
                        url: 'http://ceshi.com',
                        text: '测试文本',
                        type: '其他'
                    },
                    {
                        id: '2',
                        url: 'http://ceshi.com',
                        text: '测试文本',
                        type: '其他'
                    },
                    {
                        id: '3',
                        url: 'http://ceshi.com',
                        text: '测试文本',
                        type: '其他'
                    },
                    {
                        id: '4',
                        url: 'http://ceshi.com',
                        text: '测试文本',
                        type: '其他'
                    }
                ],
                tabledataheader: {
                    id: '序号',
                    url: '网易新闻链接',
                    text: '文本内容',
                    type: '类型'
                }
            }
        }
    }

</script>

<style lang="less" scoped>
    developinfo{
        p{
            display: flex;
            span{
                display: flex;
                margin-left: 20px;
            }
        }
    }
    .userinfo {
        .name{
            font-weight: bold;
            text-align: center;
        }
        .access{
            font-weight: bold;
            text-align: center;
        }
        border-bottom: #42b983 solid thin;
    }
    .user {
        img{
            width: 120px;
            height: 120px;
            border-radius: 50%;
        }

    }
</style>

