<template>
  <div>
    <sui-modal v-model="open">
      <sui-modal-header>{{user.active ? "Desactivar" : "Activar"}} usuario</sui-modal-header>
      <sui-modal-content>
        <sui-modal-description>
          <sui-header>
            Esta seguro que desea {{user.active ? "desactivar" : "activar"}} a {{user.name}}?
          </sui-header>
          <p v-if="user.active">
            Si lo acepta, este usuario no podra utilizar el sistema hasta que vuelva a ser activado
          </p>
          <p v-else>
            Si lo acepta, este usuario volvera a funcionar en el sistema
          </p>
        </sui-modal-description>
      </sui-modal-content>
      <sui-modal-actions>
        <sui-button positive icon="check" @click="modify">
          Si
        </sui-button>
        <sui-button icon="x" negative @click="toggle">
          no
        </sui-button>
      </sui-modal-actions>
    </sui-modal>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: {
    open: {
      type: Boolean,
      default: false,
    },
    user: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    toggle() {
      this.$emit('close');
    },
    modify() {
      this.$emit('changeStatus');
    },
  },
};
</script>
