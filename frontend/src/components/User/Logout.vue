<script>
export default {
  name: 'logout',
  beforeCreate() {
    localStorage.setItem('token', '');
    window.location = '/';
  },
};
</script>
