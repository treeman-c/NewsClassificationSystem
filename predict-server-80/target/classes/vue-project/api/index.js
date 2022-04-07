import axios from "axios";
import config from '../conf'
import {Loading} from "element-ui";

const baseUrl = process.env.NODE_ENV === 'development' ? config.baseUrl.dev : config.baseUrl.pro

class HttpRequest{
    constructor(baseUrl) {
        this.baseUrl = baseUrl
    }
    getInsideConfig(){
        const config = {
            baseUrl: this.baseUrl,
            header:{}
        }
        return config
    }
    interceptors(instance){
        // 添加请求拦截器
        instance.interceptors.request.use(function (config) {
            // 在发送请求之前做些什么
            const load = Loading.service({
                fullscreen:true,
                text: '正在拼了老命请求数据中...',
                background:'rgba(0, 0, 0, 0.8)',
            })
            return config;
        }, function (error) {
            // 对请求错误做些什么
            const load = Loading.service({})
            load.close()
            this.$message('数据请求失败，失败原因'+error);
            return Promise.reject(error);
        });

// 添加响应拦截器
        instance.interceptors.response.use(function (response) {
            // 对响应数据做点什么
            const load = Loading.service({})
            load.close()
            return response;
        }, function (error) {
            // 对响应错误做点什么
            const load = Loading.service({})
            load.close()
            this.$message('数据响应失败，失败原因'+error);
            return Promise.reject(error);
        });
    }
    request(option){
        const instance  = axios.create()
        option = {...this.getInsideConfig(), ...option}
        this.interceptors(instance)
        return instance(option)
    }
}

export default new HttpRequest(baseUrl)
