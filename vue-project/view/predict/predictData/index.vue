<template>
    <div>
        <el-row :gutter="20" style="margin-top: 5px">
            <el-col :span="5">
                <div class="demo-input-suffix">
                    <el-input
                            placeholder="请输入ID"
                            v-model="input.id">
                    </el-input>
                </div>
            </el-col>
            <el-col :span="5">
                <el-select
                        v-model="input.algorithm"
                        multiple
                        filterable
                        allow-create
                        default-first-option
                        placeholder="请选择算法">
                    <el-option
                            v-for="item in algorithm"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-col>
            <el-col :span="5">
                <el-select
                        v-model="input.method"
                        multiple
                        filterable
                        allow-create
                        default-first-option
                        placeholder="请选择方式">
                    <el-option
                            v-for="item in method"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-col>
            <el-col :span="5">
                <el-select
                        v-model="input.pretype"
                        multiple
                        filterable
                        allow-create
                        default-first-option
                        placeholder="请选择类别">
                    <el-option
                            v-for="item in type"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-col>
            <el-col :span="4">
                <el-button @click="serch" type="success" round>搜索</el-button>
            </el-col>
        </el-row>
        <div>
            <el-table
                    ref="filterTable"
                    height="500"
                    :data="newsData"
                    style="width: 100%">
                <el-table-column
                        prop="id"
                        label="ID"
                        sortable
                        width="80"
                        column-key="id">
                </el-table-column>
                <el-table-column
                        prop="algorithm"
                        label="分类算法"
                        width="80">
                </el-table-column>
                <el-table-column
                        prop="method"
                        label="分类方法"
                        width="80">
                </el-table-column>
                <el-table-column
                        prop="pretype"
                        label="新闻类别"
                        width="100"
                        :filters="newstype"
                        :filter-method="filterTag"
                        filter-placement="bottom-end">
                    <template slot-scope="scope">
                        <el-tag
                                type="success"
                                disable-transitions>{{scope.row.pretype}}</el-tag>
                    </template>
                </el-table-column>

                <el-table-column
                        prop="url"
                        label="链接"
                        :show-overflow-tooltip="true"
                        width="200">
                </el-table-column>
                <el-table-column
                        prop="pretext"
                        :show-overflow-tooltip="true"
                        label="新闻文本内容">
                </el-table-column>

                <el-table-column
                        fixed="right"
                        label="操作"
                        width="200">
                    <template slot-scope="scope">
                        <el-button @click="updataRow(scope.row)" type="text" size="small">修改</el-button>
                        <el-button @click="deleteRow(scope.row)" type="danger" size="small">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
<!--dialog对话框-->
        <el-dialog title="修改内容" :visible.sync="dialogFormVisible">
            <el-form :model="form">
                <el-form-item label="链接" :label-width="formLabelWidth">
                    <el-input v-model="form.url" autocomplete="off" :placeholder="form.url"/>
                </el-form-item>
                <el-form-item label="预测类别" :label-width="formLabelWidth">
                    <el-select v-model="form.pretype" :placeholder="form.pretype">
                        <el-option label="体育" value="体育"/>
                        <el-option label="军事" value="军事"/>
                        <el-option label="航空" value="航空"/>
                        <el-option label="政治" value="政治"/>
                        <el-option label="国际" value="国际"/>
                    </el-select>
                </el-form-item>
                <el-form-item label="预测文本" :label-width="formLabelWidth">
                    <el-input v-model="form.pretext" autocomplete="off" :placeholder="form.pretext"/>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="updataPredict">确 定</el-button>
            </div>
        </el-dialog>

        <div class="block">
            <el-pagination
                    background
                    @size-change="changeSize"
                    @current-change="changeCur"
                    :current-page="currentPage"
                    :page-sizes="[10, 15, 20, 25]"
                    :page-size="10"
                    layout="total, sizes, prev, pager, next, jumper"
                    :total="total">

            </el-pagination>

        </div>
    </div>
</template>

<script>
    import {deleteById,updataById,getPredictData,findByOrder} from '../../../api/data';
    export default {
        name:'predcictData',
        data(){
            return {
                newsData:[],
                dialogTableVisible: false,
                dialogFormVisible: false,
                input: {
                    id: '',
                    pretype:'',
                    algorithm:'',
                    method:''
                },
                currentPage:1,
                total:0,
                size:10,
                formLabelWidth: '120px',
                newstype:[
                    {
                        text: '体育',
                        value: '体育'
                    },
                    {
                        text: '军事',
                        value: '军事'
                    },
                    {
                        text: '国际',
                        value: '国际'
                    },
                    {
                        text: '航空',
                        value: '航空'
                    },
                    {
                        text: '政治',
                        value: '政治'
                    }
                ],
                form:{
                    id:1,
                    algorithm:"",
                    method:"",
                    pretype:"体育",
                    pretext:"",
                    url:""
                },
                method:[
                    {
                        label:'文本',
                        value:'text'
                    },
                    {
                        label:"链接",
                        value:'url'
                    }
                ],
                type:[
                    {
                        label:'体育',
                        value:"体育"
                    },
                    {
                        label:'军事',
                        value:"军事"
                    },
                    {
                        label:'国际',
                        value:"国际"
                    },
                    {
                        label:'政治',
                        value:"政治"
                    },
                    {
                        label:'航空',
                        value:"航空"
                    }
                ],
                algorithm:[
                    {
                        label:'支持向量机',
                        value:"svm"
                    },
                    {
                        label:'贝叶斯',
                        value:"bayes"
                    },
                    {
                        label:'K最近邻算法',
                        value:"knn"
                    },
                    {
                        label:'bp神经网络',
                        value:"bp"
                    },
                    {
                        label:'智能预测',
                        value:"intelligent"
                    }

                ],

            }
        },
        mounted() {
            this.getPageData()
            // this.getAllData()
        },
        methods: {
            serch(){
                this.currentPage=1;
                const temp={
                    'id':this.input.id,
                    'algorithm':JSON.stringify(this.input.algorithm),
                    'pretype':JSON.stringify(this.input.pretype),
                    'method':JSON.stringify(this.input.method),
                    'current':this.currentPage,
                    'size':this.size
                };
                findByOrder(temp).then(res=>{
                    console.log(res)
                    const data= res.data
                    this.total =data.total
                    this.newsData = data.records

                }).catch(e=>{
                    console.log(e)
                })
            },
            changeSize(val){
                this.size = val
                this.getPageData()
            },
            changeCur(val){
                this.currentPage = val
                this.getPageData()
            },
            filterTag(value, row) {
                return row.pretype === value;
            },
            getPageData(){
                getPredictData({'current':this.currentPage,'size':this.size}).then(res=>{
                    const data= res.data
                    this.total =data.total
                    this.newsData = data.records
                    console.log(res)
                }).catch(e=>{
                    console.log(e)
                })
            },
            updataRow(row){
                this.dialogFormVisible = true
                this.form.id=row.id
                this.form.algorithm=row.algorithm
                this.form.method=row.method
                this.form.url=row.url
                this.form.pretext=row.pretext
                this.form.pretype=row.pretype
            },
            updataPredict(){
                updataById({'id':this.form.id,'url':this.form.url,'algorithm':this.form.algorithm,'method':this.form.method,'pretext':this.form.pretext,'pretype':this.form.pretype}).then(res=>{
                    this.getPageData()
                    this.dialogFormVisible = false
                }).catch(e=>{
                    this.dialogFormVisible = false
                    console.log(e)
                })
            },
            deleteRow(row){
                deleteById({'id':row.id}).then(res=>{
                    this.getPageData()
                }).catch(e=>{
                    console.log(e)
                })
                console.log(row)
            }
        }

    }

</script>