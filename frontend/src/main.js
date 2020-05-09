import Vue from 'vue';
import SuiVue from 'semantic-ui-vue';
import 'semantic-ui-css/semantic.min.css';
import VueToast from 'vue-toast-notification';
import App from './App.vue';
import router from './router';
import 'vue-toast-notification/dist/theme-sugar.css';

Vue.config.productionTip = false;
Vue.use(SuiVue);
Vue.use(VueToast);

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
