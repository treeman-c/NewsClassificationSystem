<template>
    <div class="block">
        <el-card shadow="hover">
            <el-descriptions title="使用介绍" :colon="false">
                <el-descriptions-item label="">
                    机器学习算法部分，采用具有强大机器学习库的python语言开发，我选用sklearn第三库训练模型。
                    分类器选择四种进行训练，分别为贝叶斯、支持向量机、K最近邻算法、BP神经网络。
                    数据集采用的网易新闻的网页内容，python爬虫获取文本内容。
                    数据集、模型、评价得分都保存为文件形式。应用程序采用tkinter第三方库进行编写，页面比较简洁，
                    程序打包使用Pyinstaller，将tkinter写的python程序打包为文件夹，并把依赖一并打包。
                </el-descriptions-item>
            </el-descriptions>
        </el-card>
        <el-card shadow="hover">
                    <div class="demo-image" v-for="item in urls" :key="item.src + ' '">
                        <el-divider><i class="el-icon-picture"/></el-divider>
                        <div class="block" style="margin: 0 auto">
                            <el-image :src="item.src" fit="contain"/>
                        </div>
                    </div>
        </el-card>
        <el-divider><i class="el-icon-download"/></el-divider>
        <el-row>
            <el-col :span="12">
                <el-descriptions title="" >
                    <el-descriptions-item label="下载压缩包">
                        <el-button @click="downloadclick" type="primary" icon="el-icon-download" circle/>
                    </el-descriptions-item>
                </el-descriptions>
            </el-col>
            <el-col :span="12">
                <span class="text">下载后，解压缩，在根目录下找到newsclassify.exe文件，运行即可</span>
            </el-col>
        </el-row>

    </div>
</template>

<script>
    import {downloadfile} from "../../../api/data";

    export default {
        name:'page1',
        data(){
            return {
                urls: [
                    {
                        src : require('../../../src/assets/image/app-introduce/origin.jpg')
                    },
                    {
                        src : require('../../../src/assets/image/app-introduce/step1.jpg')
                    },
                    {
                        src : require('../../../src/assets/image/app-introduce/step2.jpg')
                    }
                ]
            }
        },
        methods:{
            downloadclick(){
                downloadfile().then(res=>{
                    const fn = 'newsclassify.rar'
                    console.log(res.data)
                    const blob = window.URL.createObjectURL(new Blob([res.data]))
                    const a = document.createElement("a")
                    a.href = blob
                    a.style.display="none"
                    a.setAttribute('download', fn)
                    document.body.appendChild(a)
                    a.click()
                }).catch(e=>{
                    console.log(e)
                })
            }
        }
    }

</script>


<style>
    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 150px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
    .text{
        color: #606266;
        font-weight:400;
        line-height:1.5;
    }
</style>

