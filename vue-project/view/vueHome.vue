<template>

    <el-container style="height: 100%">
        <el-aside width="auto">
            <common-aside/>
        </el-aside>
        <el-container>
            <el-header>
                <common-header />
            </el-header>
            <el-main>
                <router-view/>
            </el-main>
            <el-footer>
                <common-footer/>
            </el-footer>
        </el-container>
    </el-container>
</template>

<script>
    import CommonAside from "../src/components/CommonAside";
    import CommonHeader from "../src/components/CommonHeader";
    import CommonFooter from "../src/components/CommonFooter"

    export default {
        name: 'vueHome',
        components: {
            CommonAside,
            CommonHeader,
            CommonFooter
        },
        data(){
            return {}
        }
    }
</script>

<style lang="less" scoped>
    .el-header{
        background-color: #2c3e50;
    }
    .el-main{
        padding-top: 0;
    }
    .el-footer{
        padding: 0;
    }
</style>
