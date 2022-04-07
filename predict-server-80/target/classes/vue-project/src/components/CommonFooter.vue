<template>
    <header>
        <div class="l-content">
            <p>&copy;treeman-c</p>
            <div>
                <i class="el-icon-chat-line-round"/>
                <span>欢迎留言</span>
            </div>
            <div>
                <i class="el-icon-hot-water"/>
                <span>留言功能未启动</span>
            </div>

        </div>
    </header>
</template>

<script>
    export  default {
        name:'CommonFooter',
        data(){
            return {
                userImg: require('../assets/image/headImg.jpeg')
            }
        },
        methods:{

        }
    }
</script>

<style lang="less" scoped>
    header{
        display: flex;
        height: 100%;
        padding: 0;
        background-color: darkslategrey;
        justify-content: space-between;
        align-items: center;
    }
    .l-content{
        display: flex;
        margin: 0 auto;
        align-items: center;
        div{
            margin-left: 50px;
            font-size: 18px;
        }
    }
</style>
