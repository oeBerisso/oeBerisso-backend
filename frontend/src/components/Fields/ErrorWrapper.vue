<template>
  <div :class="{ 'has-error': (errors.length > 0) }" class="input-field">
    <slot></slot>
    <p class="err-msg"> {{ errors.join(', ') }} </p>
  </div>
</template>

<script>
export default {
  props: {
    errors: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style lang="scss" scoped>
  .input-field {
    .err-msg {
      font-size: 0.8rem;
      color: red;
      position: absolute;
    }
  }
</style>
