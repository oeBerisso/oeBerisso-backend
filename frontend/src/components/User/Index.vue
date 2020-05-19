<template>
  <sui-container class='form-container'>
    <sui-segment raised>
      <sui-form @submit.prevent="filterUsers">
        <sui-form-fields fields="five">
          <sui-form-field>
            <label>Nombre de usuario</label>
            <sui-input
              placeholder="Usuario"
              v-model="filter.username"
            />
          </sui-form-field>
          <sui-form-field>
            <label>Email</label>
            <sui-input
              placeholder="Correo electrónico"
              v-model="filter.email"
            />
          </sui-form-field>
          <sui-form-field>
            <label>Apellido o nombre</label>
            <sui-input
              placeholder="Apellido o nombre"
              v-model="filter.name"
            />
          </sui-form-field>
          <sui-form-field>
            <label>Activo</label>
            <sui-dropdown
              selection
              :options="options"
              placeholder="Activo"
              v-model="filter.active"
            />
          </sui-form-field>
          <sui-form-field>
            <label> Filtrar </label>
            <sui-button primary icon="search" />
            <sui-button color="red" icon="x" type="button" @click="clear" />
          <sui-form-field>
        </sui-form-fields>
      </sui-form>
      <modal
        :user="selectedUser"
        :active="activeModal"
        @close="close"
        @changeStatus="changeStatus"
      />
      <sui-divider />

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
                color="red"
                icon="user plus"
                @click="openModal(user)"
                v-if="user.active"
              >
                Desactivar usuario
              </sui-button>
              <sui-button
                color="green"
                icon="user times"
                v-else
                @click="openModal(user)"
              >
                Activar usuario
              </sui-button>
              <div style="text-align: rigth, float: left">
                <sui-button
                  primary
                  icon="pencil"
                  @click="openModal(user)"
                >
                  Modificar roles
                </sui-button>
              </div>
            </sui-table-cell>
          </sui-table-row>
        </sui-table-body>
      </sui-table>
      <paginate
        :page-count="pages"
        :click-handler="pageChanged"
        :prev-text="'Anterior'"
        :next-text="'Siguiente'"
        :container-class="'pagination'">
      </paginate>
    </sui-segment>
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
    this.fetchUsers();
  },
  computed: {
    selectedUser() {
      return this.currentUser;
    },
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
      let url;
      if (this.useFilter) {
        url = `/usuarios?name=${this.filter.name}&email=${this.filter.email}&active=${this.filter.active}&username=${this.filter.username}&page=${this.actualPage}`;
      } else {
        url = `/usuarios?page=${this.actualPage}`;
      }
      await axios({
        url,
        method: 'get',
      }).then((response) => {
        this.users = response.data.users;
        this.pages = response.data.pages;
      }).catch(() => {
        this.$toast.error('Ocurrio un error en el servidor, intentá ms tarde', {
          type: 'error',
          duration: 3000,
          position: 'top-left',
        });
        this.saving = false;
      });
    },
    filterUsers() {
      this.useFilter = true;
      this.actualPage = 1;
      this.fetchUsers();
    },
    openModal(user) {
      this.currentUser = user;
      this.activeModal = true;
    },
    close() {
      this.currentUser = {};
      this.activeModal = false;
    },
    clear() {
      this.actualPage = 1;
      this.useFilter = false;
      this.filter = {
        username: '',
        email: '',
        active: '',
        name: '',
      };
      this.fetchUsers();
    },
    async changeStatus() {
      await axios({
        url: `/usuarios/${this.currentUser.id}/${this.currentUser.active ? 'desactivar' : 'activar'}`,
        method: 'post',
      });
      this.actualPage = 1;
      this.fetchUsers();
      this.close();
    },
    pageChanged(page) {
      this.actualPage = page;
      this.fetchUsers();
    },
  },
  data() {
    return {
      users: [],
      activeModal: false,
      currentUser: {},
      saving: false,
      pages: '',
      actualPage: 1,
      useFilter: false,
      filter: {
        username: '',
        email: '',
        active: '',
        name: '',
      },
      options: [
        {
          text: 'Activo',
          value: 1,
        },
        {
          text: 'No activo',
          value: 0,
        },
      ],
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

.pagination {
  display: inline-block;
}

.pagination li {
    color: black;
    float: left;
    padding: 8px 16px;
    text-decoration: none;
    list-style-type: none;
    position: relative;
    left: -30px;
    border: 1px solid rgb(83, 120, 187);
}

.pagination li.active {
    background-color: #4CAF50;
    color: white;
}

.pagination a{
    color: black;
    float: left;
    display: inline-block;
    position: relative;
    z-index: 1;
    padding: 0.75em;
    margin: -0.75em;
}

</style>
