<template>
    <div>
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
                        width="180"
                        column-key="id"
                >
                </el-table-column>
                <el-table-column
                        prop="type"
                        label="新闻类别"
                        width="100"
                        :filters="newstype"
                        :filter-method="filterTag"
                        filter-placement="bottom-end">
                    <template slot-scope="scope">
                        <el-tag
                                type="success"
                                disable-transitions>{{scope.row.type}}</el-tag>
                    </template>
                </el-table-column>

                <el-table-column
                        prop="text"
                        label="新闻文本内容">
                </el-table-column>

            </el-table>
        </div>

        <div class="block">
            <el-pagination
                    background
                    @size-change="changeSize"
                    @current-change="changeCur"
                    :current-page="currentPage"
                    :page-sizes="[100, 200, 300, 400]"
                    :page-size="100"
                    layout="total, sizes, prev, pager, next, jumper"
                    :total="total">
            </el-pagination>
        </div>
    </div>
</template>

<script>
    import {getPageData,getData} from '../../../api/data';
    export default {
        name:'page2',
        data(){
            return {
                newsData:[],
                currentPage:1,
                total:0,
                size:100,
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
                ]
            }
        },
        mounted() {
            this.getPageData()
            // this.getAllData()
        },
        methods: {
            changeSize(val){
                this.size = val
                this.getPageData()
            },
            changeCur(val){
                this.currentPage = val
                this.getPageData()
            },
            filterTag(value, row) {
                return row.type === value;
            },
            getPageData(){
                getPageData({'current':this.currentPage,'size':this.size}).then(res=>{
                    const data= res.data
                    this.total =data.total
                    this.newsData = data.records
                    console.log(res)
                }).catch(e=>{
                    console.log(e)
                })
            },
            getAllData(){
                getData().then(res=>{
                    this.newsData = res.data
                    this.total =res.data.length
                    console.log(res)
                }).catch(e=>{
                    console.log(e)
                })
            }
        }

    }

</script>