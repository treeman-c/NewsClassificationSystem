<template>

    <div style="margin: 20px 0;">
    <el-row :gutter="5">
<!--        左侧url框和按钮-->
        <el-col :span="12">
<!--            输入框部分-->
            <el-row>
                <div class="grid-content bg-purple">
                    <el-input v-model="textarea1" placeholder="请输入URL（仅支持网易新闻链接）"/>
                </div>
            </el-row>
<!--            按钮部分-->
            <el-row style="margin-top: 50px">
                <el-row>
                    <el-col :span="12" style="padding-left: 50px">
                        <el-button @click="bayesU" type="primary" style="width: 200px" round>贝叶斯URL预测</el-button>
                    </el-col>
                    <el-col :span="12">
                        <el-button @click="bayesT" type="primary" style="width: 200px"  round>贝叶斯TEXT预测</el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12" style="padding-left: 50px">
                        <el-button @click="svmU" type="primary" style="width: 200px"  round>支持向量机URL预测</el-button>
                    </el-col>
                    <el-col :span="12">
                        <el-button @click="svmT" type="primary" style="width: 200px"  round>支持向量机TEXT预测</el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12" style="padding-left: 50px">
                        <el-button @click="knnU" type="primary" style="width: 200px"  round>K最近邻URL预测</el-button>
                    </el-col>
                    <el-col :span="12">
                        <el-button @click="knnT" type="primary" style="width: 200px"  round>K最近邻TEXT预测</el-button>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12" style="padding-left: 50px">
                        <el-button @click="bpU" type="primary" style="width: 200px"  round>BP神经网络URL预测</el-button>
                    </el-col>
                    <el-col :span="12">
                        <el-button @click="bpT" type="primary" style="width: 200px"  round>BP神经网络TEXT预测</el-button>
                    </el-col>
                </el-row>
                <el-row type="flex" justify="center">
                    <el-col :span="12">
                        <el-button @click="inT" type="primary" style="width: 200px"  round>智能TEXT预测</el-button>
                    </el-col>
                </el-row>
                <el-row style="margin-left: 80px;margin-top:80px">
                    <el-col :span="5">
                        <div class="tag-group">
                            <el-tag  type="info"  effect="dark">分类结果：</el-tag>
                        </div>
                    </el-col>
                    <el-col :span="1">
                        <div class="tag-group">
                            <el-tag  type="danger"  effect="dark">{{type}}</el-tag>
                        </div>
                    </el-col>
                </el-row>
            </el-row>
        </el-col>
<!--        右侧文本框-->
        <el-col :span="12">
            <div class="grid-content bg-purple">

                    <el-input
                            type="textarea"
                            :autosize="true"
                            placeholder="请输入TEXT内容"
                            v-model="textarea2">
                    </el-input>

            </div>
        </el-col>
    </el-row>
    </div>
</template>

<script>
    import {bayes_url,bayes_text,svm_url, svm_text, knn_url,knn_text,bp_url,bp_text,in_text} from "../../api/data";

    export default {
        name:'predict',
        data() {
            return {
                textarea1: '',
                textarea2: '',
                type:'待执行'
            }
        },
        methods:{
            UrlisVaild(){
                if(this.textarea1.indexOf('163.com')<0){
                    this.$message({
                        message: '链接非网易新闻链接或不合法，暂不支持',
                        type: 'warning'
                    });
                    return false
                }
                return true
            },

            TextisVaild(){
                if(this.textarea2.length<=20){
                    this.$message({
                        message: '文本字符数过少，需大于20个字符',
                        type: 'warning'
                    });
                    return false
                }
                return true
            },
            bayesU(){
                this.type='待执行'
                if (!this.UrlisVaild()){
                    return
                }
                bayes_url({url: this.textarea1}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            },
            bayesT(){
                this.type='待执行'
                if (!this.TextisVaild()){
                    return
                }
                bayes_text({text: this.textarea2}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            },
            svmU(){
                this.type='待执行'
                if (!this.UrlisVaild()){
                    return
                }
                svm_url({url: this.textarea1}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            },
            svmT(){
                this.type='待执行'
                if (!this.TextisVaild()){
                    return
                }
                svm_text({text: this.textarea2}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            },
            knnU(){
                this.type='待执行'
                if (!this.UrlisVaild()){
                    return
                }
                knn_url({url: this.textarea1}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            },
            knnT(){
                this.type='待执行'
                if (!this.TextisVaild()){
                    return
                }
                knn_text({text: this.textarea2}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            },
            bpU(){
                this.type='待执行'
                if (!this.UrlisVaild()){
                    return
                }
                bp_url({url: this.textarea1}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            },
            bpT(){
                this.type='待执行'
                if (!this.TextisVaild()){
                    return
                }
                bp_text({text: this.textarea2}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            },
            inT(){
                in_text({text: this.textarea2}).then(res=>{
                    console.log(res)
                    this.textarea2=res.data.text
                    this.type=res.data.type.replace(/\"/g,'')
                }).catch(res=>{
                    console.log(res)
                    this.textarea2="分类出现错误，请检查数据"
                })
            }


        }
    }

</script>


<style>
    .el-row {
        margin-bottom: 20px;
    }
    .el-col {
        border-radius: 4px;
    }
    .bg-purple-dark {
        background: #99a9bf;
    }
    .bg-purple {
        background: #d3dce6;
    }
    .bg-purple-light {
        background: #e5e9f2;
    }
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>
