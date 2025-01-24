<template>
  <v-app>
      <Header />
       <pub-view />
      <Footer />
  </v-app>
</template>



<script>
export default {
  name: 'Public',
  components: {
    Header: () => import('./Header'),
    PubView: () => import('./View'),
    Footer: () => import('./Footer'),
  },
};
</script>


<style>
  /* .v-application--wrap {
    min-height:auto;
  } */
</style>
