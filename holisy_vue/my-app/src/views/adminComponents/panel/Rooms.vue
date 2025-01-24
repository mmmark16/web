<template>
    <v-card
        flat
    >
        <Header />
        <Rooms />
    </v-card>
</template>


<script>
  export default {
    components: {
        Rooms: () => import('@/components/admin/Rooms'),
        Header: () => import('@/components/admin/Header'),
    },
    data () {
      return {
      }
    },
  }
</script>
