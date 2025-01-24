<template>
  <v-app class="auth_wrapper">
      <img src="@/assets/fon.jpg" alt="fon" class="fon">
      <auth-view />
  </v-app>
</template>



<script>
export default {
  name: 'Authorization',
  components: {
    AuthView: () => import('./View'),
  },
};
</script>


<style>
    .auth_wrapper {
        width:100vw;
        height:100vh;
        position:relative;
    }
    .auth_wrapper .fon {
        position:absolute;
        width:100%;
        height:100%;
        object-fit: cover;
        object-position: center bottom;
        left:0;
        top:0;
    }
    .theme--light.v-application {
        background: none!important;
    }
</style>