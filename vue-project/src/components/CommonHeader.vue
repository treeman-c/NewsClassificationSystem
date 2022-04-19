<template>
    <header>
        <div class="l-content">
            <el-button @click="ctrMenu()" plain icon="el-icon-menu" size="mini"/>
            <h3 style="color: #fff">首页</h3>
        </div>
        <div class="r-content" >
            <el-dropdown trigger="click" size="mini">
                <span>
                    <img class="user" :src="userImg"/>
                </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="a">demo(center)</el-dropdown-item>
                    <el-dropdown-item command="b">demo(exit)</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>
    </header>
</template>

<script>
    export  default {
        name:'CommonHeader',
        data(){
            return {
                userImg: require('../assets/image/headImg.jpeg')
            }
        },
        methods:{
            ctrMenu(){
                this.$store.commit('collapseMenu')
            }
        }
    }
</script>

<style lang="less" scoped>
    header{
        display: flex;
        height: 100%;
        justify-content: space-between;
        align-items: center;
    }
    .l-content{
        display: flex;
        align-items: center;
        .el-button{
            margin-right: 20px;
        }
    }
    .r-content{
        .user{
            width: 40px;
            height: 40px;
            border-radius: 50%;
        }
    }
</style>
