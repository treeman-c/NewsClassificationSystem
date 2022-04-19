import axios from "./index";


export const  getMenu = (param)=>{
    return axios.request({
        url:'http://localhost/java-user',
    method:'post',
    data:param
})
};
export const  bayes_url= (param)=>{
    return axios.request({
    url:'http://localhost/bayes-url',
    method:'post',
    data:param
})
};
export const  bayes_text= (param)=>{
    return axios.request({
        url:'http://localhost/bayes-text',
        method:'post',
        data:param
    })
};
export const  svm_url= (param)=>{
    return axios.request({
        url:'http://localhost/svm-url',
        method:'post',
        data:param
    })
};
export const  svm_text= (param)=>{
    return axios.request({
        url:'http://localhost/svm-text',
        method:'post',
        data:param
    })
};
export const  knn_url= (param)=>{
    return axios.request({
        url:'http://localhost/knn-url',
        method:'post',
        data:param
    })
};
export const  knn_text= (param)=>{
    return axios.request({
        url:'http://localhost/knn-text',
        method:'post',
        data:param
    })
};
export const  bp_url= (param)=>{
    return axios.request({
        url:'http://localhost/bp-url',
        method:'post',
        data:param
    })
};
export const  bp_text= (param)=>{
    return axios.request({
        url:'http://localhost/bp-text',
        method:'post',
        data:param
    })
};
export const  updataById= (param)=>{
    return axios.request({
        url:'http://localhost/updataById',
        method:'post',
        data:param
    })
};
export const  deleteById= (param)=>{
    return axios.request({
        url:'http://localhost/deleteById',
        method:'post',
        data:param
    })
};
export const  getPredictData= (param)=>{
    return axios.request({
        url:'http://localhost/predictData',
        method:'post',
        data:param
    })
};

export const  findByOrder= (param)=>{
    return axios.request({
        url:'http://localhost/findByOrder',
        method:'post',
        data:param
    })
};
export const  get_data= ()=>{
    return axios.request({
        url:'http://localhost:8002/get-ch-data',
        method:'get',
    })
};
export const  train_model= ()=>{
    return axios.request({
        url:'http://localhost:8002/train-model',
        method:'get',
    })
};
export const  downloadfile= ()=>{
    return axios.request({
        url:'http://localhost:8003/download-file',
        method:'post',
        responseType:'arraybuffer'
    })
};
export const  downloaddataset= ()=>{
    return axios.request({
        url:'http://localhost:8003/download-dataset',
        method:'post',
        responseType:'arraybuffer'
    })
};
export const  getPageData= (param)=>{
    return axios.request({
        url:'http://localhost:8003/getData',
        method:'post',
        data:param
    })
};
export const  getData= ()=>{
    return axios.request({
        url:'http://localhost:8003/getData',
        method:'get',
    })
};
export const  in_text= (param)=>{
    return axios.request({
        url:'http://localhost/intelligent-text',
        method:'post',
        data:param
    })
};
