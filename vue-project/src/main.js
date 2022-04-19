import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from '../router'
import store from "../store";
import http from "axios";


// const cors = require('koa2-cors');
// Vue.use(cors());
Vue.config.productionTip = false
Vue.use(ElementUI)
http.defaults.withCredentials=true;
Vue.prototype.$http = http

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')






