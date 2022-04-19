import Vue from 'vue'
import VueRouter from 'vue-router'
import vueHome from '../view/vueHome.vue'



Vue.use(VueRouter)

const routes = [
    {
        path : '/',
        name : 'vueHome',
        component : () => import('../view/vueHome.vue'),
        children:[
            {
                path: '/home',
                name:'home',
                component: ()=> import('../view/home/index')
            },
            {
                path: '/predict',
                name:'predict',
                component: ()=> import('../view/predict/index')
            },
            {
                path: '/predictData',
                name:'predictData',
                component: ()=> import('../view/predict/predictData/index')
            },
            {
                path: '/charts',
                name:'charts',
                component: ()=> import('../view/charts/index')
            },
            {
                path: '/page1',
                name:'page1',
                component: ()=> import('../view/download/application/index')
            },
            {
                path: '/page2',
                name:'page2',
                component: ()=> import('../view/download/dataset/index')
            }
        ],
        redirect: "/home"
    }
];

const router = new VueRouter(
    {
        mode: 'history',
        routes
    }
);

export default  router