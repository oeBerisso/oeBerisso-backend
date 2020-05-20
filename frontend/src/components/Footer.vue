<template>
  <sui-segment inverted class='footer'>
    <sui-grid>
      <sui-grid-row>
        <sui-grid-column :width="8">
          <sui-list class='footer-list'>
            <sui-list-item>
              <sui-list-icon name="users" />
              <sui-list-content>
                Orquesta Escuela de Berisso
              </sui-list-content>
            </sui-list-item>
            <sui-list-item>
              <sui-list-icon name="marker" />
              <sui-list-content>
                Berisso, Argentina
              </sui-list-content>
            </sui-list-item>
            <sui-list-item>
              <sui-list-icon name="mail" />
              <sui-list-content>
                <a href="test">{{email}}</a>
              </sui-list-content>
            </sui-list-item>
            <sui-list-item>
              <sui-list-icon name="linkify" />
              <sui-list-content>
                <a href="http://oeberisso.com.ar">oeberisso.com.ar</a>
              </sui-list-content>
            </sui-list-item>
          </sui-list>
        </sui-grid-column>

        <sui-grid-column :width="8" class='footer-buttons'>
          <sui-button social="facebook" content="Facebook" icon="facebook" onclick ="location='https://www.facebook.com/OrquestaEscuelaBerisso/'" />
          <sui-button social="twitter" content="Twitter" icon="twitter" onclick ="location='https://twitter.com/oeberisso/'" />
          <sui-button social="instagram" content="Instagram" icon="instagram" onclick ="location='https://www.instagram.com/orquesta_escuela_berisso'" />
        </sui-grid-column>
      </sui-grid-row>
    </sui-grid>
  </sui-segment>
</template>

<script>
import axios from '../helper/axios';

export default {
  name: 'Footer',
  methods: {
    async fetchUsers() {
      const currentPath = window.location.pathname;
      await axios({
        url: '/api/v1.0/config/footer',
        method: 'get',
      }).then((response) => {
        const { maintenance, email } = response.data;
        if (maintenance === 1 && currentPath !== 'v/iniciar-sesion') {
          window.location = '/503';
        }
        this.email = email;
      }).catch(() => {
        this.$toast.error('Ocurrio un error en el servidor, intentá ms tarde', {
          type: 'error',
          duration: 3000,
          position: 'top-left',
        });
      });
    },
  },
  data() {
    return {
      email: '',
    };
  },
};
</script>

<style scoped>
  .footer-buttons {
    text-align: right;
    vertical-align: middle;
  }

  .footer{
    position:absolute;
    width:100%;
  }

  .footer-list {
    text-align: left;
  }
</style>
