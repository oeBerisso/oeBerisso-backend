import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Register from '../components/User/Register.vue';
import Login from '../components/User/Login.vue';
import Logout from '../components/User/Logout.vue';
import Users from '../components/User/Index.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/v/logout',
    name: 'Logout',
    component: Logout,
  },
  {
    path: '/v/registrarse',
    name: 'register',
    component: Register,
  },
  {
    path: '/v/iniciar-sesion',
    name: 'login',
    component: Login,
  },
  {
    path: '/v/usuarios',
    name: 'index_users',
    component: Users,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
