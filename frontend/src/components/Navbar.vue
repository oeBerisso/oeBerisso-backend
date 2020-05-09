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
    <sui-menu-menu position="right">
      <a
        is="sui-menu-item"
        content="Registrarse"
        href='/registrarse'
      />
      <a
        is="sui-menu-item"
        content="Iniciar sesion"
        href='/iniciar-sesion'
      />

    </sui-menu-menu>
  </sui-menu>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
  .navbar {
    background-color: #1a91a1!important;
  }
</style>
