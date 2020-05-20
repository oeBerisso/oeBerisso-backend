<template>
  <sui-modal v-model="activeRol">
    <sui-modal-header>Modificar roles de {{name}}</sui-modal-header>
    <sui-modal-content>
      <sui-checkbox label="Administrador" toggle v-model="permission.Administrador" />
      <br />
      <br />
      <sui-checkbox label="Profesor" toggle v-model="permission.Profesor" />
      <br />
      <br />
      <sui-checkbox label="Preceptor" toggle v-model="permission.Preceptor" />
    </sui-modal-content>
    <sui-modal-actions>
      <sui-button positive icon="check" @click="changeRol">
        Modificar
      </sui-button>
      <sui-button icon="x" negative @click="close">
        No
      </sui-button>
    </sui-modal-actions>
  </sui-modal>
</template>

<script>
export default {
  name: 'rolModal',
  props: {
    activeRol: {
      type: Boolean,
      default: false,
    },
    permission: {
      type: Object,
      default: () => ({
        Administrador: false,
        Profesor: false,
        Preceptor: false,
      }),
    },
    name: {
      type: String,
      default: 'pepe',
    },
  },
  methods: {
    close() {
      this.$emit('closeRoles');
    },
    changeRol() {
      this.$emit('modifyRoles', { permissions: this.permission });
    },
  },
};
</script>
