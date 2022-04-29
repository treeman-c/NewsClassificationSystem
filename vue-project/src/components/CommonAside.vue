<template>
    <el-menu default-active="1-4-1" class="el-menu-vertical-demo" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b" :unique-opened="true" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
        <h3>{{isCollapse ? '分类' : '新闻文本分类'}}</h3>
        <el-menu-item @click="clickMenu(item)" v-for="item in noChildren" :index="item.path+ ' '" :key="item.path+ ' '">
            <i :class="'el-icon-' + item.icon"/>
            <span slot="title">{{item.label}}</span>
        </el-menu-item>
        <el-submenu v-for="item in hasChildren" :index="item.path + ' '" :key="item.icon+'1'">
            <template slot="title">
                <i :class="'el-icon-' + item.icon"/>
                <span slot="title">{{item.label}}</span>
            </template>
            <el-menu-item-group  v-for="(subitem, subindex) in item.children" :key="subitem.path+ ' '">
                <el-menu-item @click="clickMenu(subitem)" :index="subitem.path+ ' '">{{subitem.label}}</el-menu-item>
            </el-menu-item-group>
        </el-submenu>
    </el-menu>

</template>


<style lang="less" scoped>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        min-height: 400px;
    }
    .el-menu{
        height: 100%;
        border: none;
        h3{
            color: #ffffff;
            text-align: center;
            line-height: 48px;
        }
    }
</style>

<script>
    export default {
        data() {
            return {
                menu: [
                    {
                        path: '/home',
                        name: 'home',
                        icon: 's-home',
                        label: '首页',
                        url: 'Home/Home'
                    },
                    {
                        label: '预测',
                        icon: 'star-on',
                        children: [
                            {
                                path: '/predict',
                                name: 'predict',
                                label: '功能',
                                icon:'s-promotio',
                                url: 'predict/predict'
                            },
                            {
                                path: '/predictData',
                                name: 'predictData',
                                icon:'tickets',
                                label: '预测集',
                                url: 'predict/predictData'
                            }
                        ]
                    },
                    {
                        path: '/charts',
                        name: 'charts',
                        icon: 's-marketing',
                        label: '图形',
                        url: 'charts/charts'
                    },
                    {
                        icon: 'download',
                        label: '下载',
                        children: [
                            {
                                path: '/page1',
                                name: 'page1',
                                label: '免安装应用程序',
                                icon: 'position',
                                url: 'download/application'
                            },
                            {
                                path: '/page2',
                                name: 'page2',
                                label: '数据集',
                                icon: 's-management',
                                url: 'download/dataset'
                            }
                        ]
                    }
                ]
            };
        },
        methods: {
            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },
            clickMenu(item){
                this.$router.push({
                    name: item.name
                })
            }
        },
        computed: {
            noChildren() {
                return this.menu.filter(item=>!item.children)  //把没有子项目的获取出来
            },
            hasChildren(){
                return this.menu.filter(item=>item.children)
            },
            isCollapse(){
                return this.$store.state.tab.isCollapse
            }
        }
    }
</script>