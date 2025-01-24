<template>
    <v-card
        flat
    >
        <Header />
        <Services />
    </v-card>
</template>


<script>
  export default {
    components: {
        Services: () => import('@/components/admin/Services'),
        Header: () => import('@/components/admin/Header'),
    },
    data () {
      return {
      }
    },
  }
</script>
