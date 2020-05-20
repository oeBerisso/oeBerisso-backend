<template>
  <sui-menu attached="top" class='navbar'>
    <sui-menu-item>
      <a
        is="sui-image"
        href="/"
        :src="require('../assets/logo_flat.png')"
        size="tiny"
      />
    </sui-menu-item>
    <sui-menu-item position="right">
      <sui-button basic primary inverted @click="goToMap">Mapa de los nucleos</sui-button>
    </sui-menu-item>
    <div v-if="this.hasSession">

      <sui-menu-item v-if="this.roles.includes('config_index')">
        <sui-dropdown text="Administración">
        <sui-dropdown-menu>
          <sui-dropdown-item>
          <a href="/admin">Cambiar configuracion</a>
          </sui-dropdown-item>
      </sui-dropdown>
      <sui-menu-item v-if="this.roles.includes('users_index')">
        <sui-dropdown text="Usuarios">
        <sui-dropdown-menu>
          <sui-dropdown-item>
          <a href="/usuarios">Listar usuarios</a>
          </sui-dropdown-item>
      </sui-dropdown>
      <sui-menu-item
        v-if="this.roles.some((role) => ['teacher_new', 'teacher_index'].includes(role))"
      >
        <sui-dropdown text="Profesores">
        <sui-dropdown-menu>
          <sui-dropdown-item v-if="this.roles.includes('teacher_new')">
            <a href="/registrar_profesor">Registrar Profesor</a>
          </sui-dropdown-item>
          <sui-dropdown-item v-if="this.roles.includes('teacher_index')">
            <a href="/profesores">Listar Profesores</a>
          </sui-dropdown-item>
      </sui-dropdown>
      </sui-menu-item>
      <sui-menu-item
        v-if="this.roles.some(
          (role) => ['student_new', 'student_index', 'assistace_list'].includes(role)
        )"
      >
        <sui-dropdown text="Estudiantes">
        <sui-dropdown-menu>
          <sui-dropdown-item v-if="this.roles.includes('student_new')">
            <a href="/registrar_alumno">Registrar Estudiantes</a>
          </sui-dropdown-item>
          <sui-dropdown-item v-if="this.roles.includes('student_index')">
            <a href="/estudiantes">Listar Estudiantes</a>
          </sui-dropdown-item>
          <sui-dropdown-item v-if="this.roles.includes('assistace_list')">
            <a href="/asistencia">Pasar Asistencia</a>
          </sui-dropdown-item>
      </sui-dropdown>
      </sui-menu-item>
      <sui-menu-item
        v-if="this.roles.some(
          (role) => ['instrument_new', 'instrument_index'].includes(role)
        )"
      >
        <sui-dropdown text="Instrumentos">
        <sui-dropdown-menu>
          <sui-dropdown-item v-if="this.roles.includes('instrument_new')">
            <a href="/registrar_instrumento">Registrar Instrumento</a>
          </sui-dropdown-item>
          <sui-dropdown-item v-if="this.roles.includes('instrument_index')">
            <a href="/instrumentos">Listar Instrumentos</a>
          </sui-dropdown-item>
      </sui-dropdown>
      </sui-menu-item>
      <sui-menu-item
        v-if="this.roles.some(
          (role) => [
            'school_year_show',
            'school_year_new',
            'workshop_index',
            'schedules_index',
          ].includes(role)
        )"
      >
        <sui-dropdown text="Cursos">
        <sui-dropdown-menu>
          <sui-dropdown-item v-if="this.roles.includes('school_year_show')">
            <a href="/ciclo_lectivo/lista">Ver ciclos lectivo</a>
          </sui-dropdown-item>
          <sui-dropdown-item v-if="this.roles.includes('school_year_new')">
            <a href="/ciclo_lectivo">Cargar ciclo lectivo</a>
          </sui-dropdown-item>
          <sui-divider />
          <sui-dropdown-item v-if="this.roles.includes('workshop_index')">
            <a href="/talleres">Ver talleres</a>
          </sui-dropdown-item>
          <sui-divider />
          <sui-dropdown-item v-if="this.roles.includes('schedules_index')">
            <a href="/horarios">Ver horarios</a>
          </sui-dropdown-item>
          <sui-dropdown-item v-if="this.roles.includes('schedules_new')">
            <a href="/horarios/nuevo">Cargar horarios</a>
          </sui-dropdown-item>
      </sui-dropdown>
      </sui-menu-item>

      <sui-menu-item v-if="this.hasSession">
        <sui-dropdown :text="name">
        <sui-dropdown-menu>
          <sui-dropdown-item>
            <a href="/perfil">Ver perfil</a>
          </sui-dropdown-item>
          <sui-dropdown-item>
            <a href="/v/logout">Cerrar Sesión</a>
          </sui-dropdown-item>
      </sui-dropdown>
      </sui-menu-item>
    </div>
    <div v-else>
      <sui-menu-menu position="right">
        <a
          is="sui-menu-item"
          content="Registrarse"
          href='/v/registrarse'
        />
        <a
          is="sui-menu-item"
          content="Iniciar sesion"
          href='/v/iniciar-sesion'
        />
      </sui-menu-menu>
    </div>
  </sui-menu>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Navbar',
  created() {
    axios({
      url: '/api/v1.0/me',
      method: 'get',
    }).then((res) => {
      if (res.data.token) {
        this.hasSession = true;
      }
    });
    axios({
      url: '/api/v1.0/permissions',
      method: 'get',
    }).then((res) => {
      if (res.data.code === 200) {
        this.roles = res.data.roles;
        this.name = res.data.name;
        console.log(res.data.roles);
      }
    });
  },
  methods: {
    goToMap: () => {
      window.location = '/nucleos';
    },
  },
  data() {
    return {
      name: '',
      hasSession: false,
      roles: [],
    };
  },
};
</script>

<style scoped>
  .navbar {
    background-color: #1a91a1!important;
  }
</style>
