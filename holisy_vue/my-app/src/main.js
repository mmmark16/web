import Vue from 'vue';
import App from '@/App.vue';
import router from '@/router';
import store from '@/store';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.css';


Vue.use(Vuetify);
Vue.component('public_layout', () => import('@/layouts/publicLayout/Index'));
Vue.component('admin_panel', () => import('@/layouts/adminPanel/Index'));
Vue.component('authorization', () => import('@/layouts/authorization/Index'));

new Vue({
  router,
  vuetify: new Vuetify({ iconfont: 'mdi' }),
  render: (h) => h(App),
  store,
}).$mount('#app');
