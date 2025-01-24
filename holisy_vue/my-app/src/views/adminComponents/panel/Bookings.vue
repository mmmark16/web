<template>
    <v-card
        flat
    >
        <Header />
        <Bookings />
    </v-card>
</template>


<script>
  export default {
    components: {
        Bookings: () => import('@/components/admin/Bookings'),
        Header: () => import('@/components/admin/Header'),
    },
    data () {
      return {
      }
    },
  }
</script>
