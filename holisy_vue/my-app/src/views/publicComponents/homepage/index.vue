<template>
  <v-card flat>
    <Rooms />
    <Services />
  </v-card>
</template>


<style>

</style>


<script>
export default {
  name: 'Home',

  components: {
      Rooms: () => import('@/components/homepage/Rooms'),
      Services: () => import('@/components/homepage/Services'),
  },

  data: () => ({
      reveal: false,
    }),

}
</script>
