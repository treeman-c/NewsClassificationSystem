import axios from "./index";


export const  getMenu = (param)=>{
    return axios.request({
        url:'http://localhost:8004/java-user',
    method:'post',
    data:param
})
};
export const  bayes_url= (param)=>{
    return axios.request({
    url:'http://localhost:8004/bayes-url',
    method:'post',
    data:param
})
};
export const  bayes_text= (param)=>{
    return axios.request({
        url:'http://localhost:8004/bayes-text',
        method:'post',
        data:param
    })
};
export const  svm_url= (param)=>{
    return axios.request({
        url:'http://localhost:8004/svm-url',
        method:'post',
        data:param
    })
};
export const  svm_text= (param)=>{
    return axios.request({
        url:'http://localhost:8004/svm-text',
        method:'post',
        data:param
    })
};
export const  knn_url= (param)=>{
    return axios.request({
        url:'http://localhost:8004/knn-url',
        method:'post',
        data:param
    })
};
export const  knn_text= (param)=>{
    return axios.request({
        url:'http://localhost:8004/knn-text',
        method:'post',
        data:param
    })
};
export const  bp_url= (param)=>{
    return axios.request({
        url:'http://localhost:8004/bp-url',
        method:'post',
        data:param
    })
};
export const  bp_text= (param)=>{
    return axios.request({
        url:'http://localhost:8004/bp-text',
        method:'post',
        data:param
    })
};
export const  updataById= (param)=>{
    return axios.request({
        url:'http://localhost:8004/updataById',
        method:'post',
        data:param
    })
};
export const  deleteById= (param)=>{
    return axios.request({
        url:'http://localhost:8004/deleteById',
        method:'post',
        data:param
    })
};
export const  getPredictData= (param)=>{
    return axios.request({
        url:'http://localhost:8004/predictData',
        method:'post',
        data:param
    })
};

export const  findByOrder= (param)=>{
    return axios.request({
        url:'http://localhost:8004/findByOrder',
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
        url:'http://localhost:8004/intelligent-text',
        method:'post',
        data:param
    })
};
