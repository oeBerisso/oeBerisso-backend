<template>
  <sui-container class='form-container'>
  <modal :user="currentUser" :open="open" />
    <sui-table celled>
      <sui-table-header>
        <sui-table-row>
          <sui-table-header-cell>Usuario</sui-table-header-cell>
          <sui-table-header-cell>Apellido, nombre</sui-table-header-cell>
          <sui-table-header-cell>Email</sui-table-header-cell>
          <sui-table-header-cell>Activo</sui-table-header-cell>
          <sui-table-header-cell>Opciones</sui-table-header-cell>
        </sui-table-row>
      </sui-table-header>
      <sui-table-body>
        <sui-table-row v-for="(user, index) in users" v-bind:key="index">
          <sui-table-cell>{{user.username}}</sui-table-cell>
          <sui-table-cell>{{user.last_name}}, {{user.first_name}}</sui-table-cell>
          <sui-table-cell>{{user.email}}</sui-table-cell>
          <sui-table-cell>{{active(user.active)}}</sui-table-cell>
          <sui-table-cell>
            <sui-button
              color="green"
              icon="user plus"
              v-if="user.active"
              @click="openModal(user)"
            />
            <sui-button
              color="red"
              icon="user times"
              v-else
              @click="openModal(user)"
            />
            <sui-button primary icon="pencil" />
          </sui-table-cell>
        </sui-table-row>
      </sui-table-body>

    </sui-table>
  </sui-container>

</template>

<script>
import axios from '../../helper/axios';
import modal from './activate-modal.vue';

export default {
  name: 'index',
  components: {
    modal,
  },
  created: async function fetch() {
    this.token = localStorage.getItem('token');
    if (!this.token) window.location = '/';
    this.fetchUsers();
  },
  methods: {
    active(number) {
      if (number) {
        return 'Si';
      }
      return 'No';
    },
    async fetchUsers() {
      this.saving = true;

      await axios({
        url: '/usuarios',
        method: 'get',
        headers: {
          Authorization: this.token,
        },
      }).then((response) => {
        this.users = response.data.users;
      }).catch(() => {
        this.$toast.error('Ocurrio un error en el servidor, intentá ms tarde', {
          type: 'error',
          duration: 3000,
          position: 'top-left',
        });
        this.saving = false;
      });
    },
    openModal(user) {
      this.currentUser = user;
      this.open = true;
    },
    close() {
      this.open = false;
      this.currentUser = {};
    },
    async changeStatus() {
      await axios({
        url: `/usuarios/${this.currentUser.id}/${this.currentUser.active ? 'desactivar' : 'activar'}`,
        method: 'post',
        headers: {
          Authorization: this.token,
        },
      }).then((response) => {
        this.users = response.data.users;
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
      token: '',
      users: [],
      open: false,
      currentUser: {},
      saving: false,
    };
  },
};
</script>

<style>
  .form-container {
    margin-top: 1rem!important;
    margin-bottom: 1rem!important;
    text-align: center;
  }
</style>
