<template>
  <sui-container class='form-container'>
    <sui-dimmer :active="saving">
      <sui-loader size="medium">Cargando</sui-loader>
    </sui-dimmer>
    <sui-grid centered vertical-align="middle">
      <sui-grid-column>
        <h2 is="sui-header">
          <sui-header-content>Inicia sesión</sui-header-content>
        </h2>
        <sui-segment stacked>
          <sui-form @submit.prevent="handleSubmit">
            <sui-form-field>
              <label>Usuario</label>
              <sui-input
                placeholder="Usuario"
                icon="user"
                v-model="user.username"
                required
                icon-position="left"
              />
            </sui-form-field>
            <sui-form-field>
              <label>Contraseña</label>
              <sui-input
                type="password"
                placeholder="Contraseña"
                icon="lock"
                v-model="user.password"
                required
                icon-position="left"
              />
            </sui-form-field>
            <sui-button size="large" primary fluid>Inicia sesión</sui-button>
          </sui-form>
            <sui-divider section />
            <sui-button
              fluid
              social="google"
              content="Continuar con Google"
              icon="google"
              @click="googleLogin"
            />
        </sui-segment>
        <sui-message>
          ¿No poseés cuenta?
          <a href="/registrarse">Registrate aqui</a>
        </sui-message>
      </sui-grid-column>
    </sui-grid>
  </sui-container>
</template>

<script>
import User from '../../models/user';
import axios from '../../helper/axios';

export default {
  name: 'login',
  beforeCreate() {
    const token = localStorage.getItem('token');
    if (token) window.location = '/';
    if (!token) {
      axios({
        url: '/me',
        method: 'get',
      }).then((res) => {
        if (res.data.token) {
          localStorage.setItem('token', res.data.token);
          window.location = '/';
        }
      });
    }
  },
  methods: {
    googleLogin: () => {
      window.location = '/glogin';
    },
    handleSubmit: async function register() {
      this.saving = true;
      await axios({
        url: '/auth',
        method: 'post',
        data: this.user,
      }).then((response) => {
        localStorage.setItem('token', response.data.token);
        setTimeout(() => window.location = '/', 3500);
      }).catch((e) => {
        if (e.response && e.response.status === 422) {
          this.$toast.error(e.response.data.msg, {
            type: 'error',
            duration: 3000,
            position: 'top-left',
          });
        } else {
          this.$toast.error('Ocurrio un error en el servidor, intentá ms tarde', {
            type: 'error',
            duration: 3000,
            position: 'top-left',
          });
        }
        this.saving = false;
      });
    },
  },
  data() {
    return {
      user: new User(),
      saving: false,
    };
  },
};
</script>

<style lang='scss'>
  .form-container {
    margin-top: 1rem!important;
    margin-bottom: 1rem!important;

    .grid {
      height: 100%;
    }
    .column {
      max-width: 450px;
      text-align: center !important;
    }
  }

</style>
