<template>
    <div>
        <el-row :gutter="2">
            <el-col :span="20">
                <el-card class="graphtop">
                    <div style="width:1000px;height: 300px" ref="top"></div>
                </el-card>
            </el-col>
            <el-col :span="4" style="margin-top: 320px">
                <el-button
                        type="primary"
                        @click="openFullScreen2">
                    重新训练模型
                </el-button>
            </el-col>

        </el-row>

        <el-row :gutter="2">
            <el-col :span="12">
                <el-card style="width:600px;height: 300px">
                    <div style="width:600px;height: 300px" ref="left"></div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card style="width:600px;height: 300px">
                    <div style="width:600px;height: 300px" ref="right"></div>
                </el-card>
            </el-col>
        </el-row>
    </div>

</template>

<script>
    import * as echarts from 'echarts'
    import * as  chart from "../../api/data";
    export default {
        name:'charts',
        data(){
            return {
                tableData:[],

            }
        },
        mounted(){
            this.getData()
        },
        methods:{
            getData(){
                chart.get_data().then(res=>{
                    const data = res.data
                    const pre = data.pre
                    const f1 = data.f1
                    const rel = data.rel
                    const pre_series=this.getSeties(pre[1],'line')
                    const rel_series=this.getSeties(rel[1],'bar')
                    const f1_series=this.getSeties(f1[1],'bar')
                    const E = echarts.init(this.$refs.top)
                        E.setOption({
                            title: { text: 'precision准确率' },
                            tooltip: {},
                            xAxis: {
                                data: pre[0].slice(1)
                            },
                            legend: {
                                // Try 'horizontal'
                                orient: 'vertical',
                                right: 10,
                                top: 'center'
                            },
                            yAxis: {},
                            series: pre_series
                        });
                    const R= echarts.init(this.$refs.left)
                    R.setOption({
                        title: { text: 'recall召回率' },
                        tooltip: {},
                        xAxis: {
                            data: rel[0].slice(1)
                        },
                        legend: {
                            // Try 'horizontal'
                            orient: 'vertical',
                            right: 10,
                            top: 'center'
                        },
                        yAxis: {},
                        series: rel_series
                    });
                   const F = echarts.init(this.$refs.right)
                    F.setOption({
                        title: { text: 'f1得分' },
                        tooltip: {},
                        xAxis: {
                            data: f1[0].slice(1)
                        },
                        legend: {
                            // Try 'horizontal'
                            orient: 'vertical',
                            right: 10,
                            top: 'center'
                        },
                        yAxis: {},
                        series: f1_series
                    });
                }).catch(res=>{
                    console.log("数据解析失败"+res)
                })
            },
            getSeties(predata,type){
                const series=[]
                for(let i=0;i<4;i++){
                    const alogrithm = predata[0]
                    const list = []
                    for(let j=1;j<6;j++){
                        const temp = predata[j]
                        list.push(temp[i])
                    }
                    series.push({
                        name:alogrithm[i],
                        type: type,
                        data:list
                    })
                }
                return series
            },
            openFullScreen2() {
                const loading = this.$loading({
                    lock: true,
                    text: '后台训练模型中，预计10多分钟后结束，你可先查看其他功能',
                    spinner: 'el-icon-loading',
                    background: 'rgba(0, 0, 0, 0.7)'
                });
                setTimeout(() => {
                    chart.train_model().then(res=>{
                        loading.text = '训练模型成功'
                    }).catch(res=>{
                        loading.text = '模型训练失败'
                    })
                    loading.close();
                }, 2000);
            }
        }
    }

</script>

<style lang="less" scoped>
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
    .graphtop{
        width: 1000px;
        height: 300px;
        display: flex;
        flex-direction: row;
        justify-content: center;

        div{
            margin: 0 auto;
        }
    }
</style>