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
                <a href="test">this is a test</a>
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
export default {
  name: 'Footer',
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
