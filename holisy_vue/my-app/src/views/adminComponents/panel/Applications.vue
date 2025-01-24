<template>
    <v-card
        flat
    >
        <Header />
        <Applications />
    </v-card>
</template>


<script>
  export default {
    components: {
        Applications: () => import('@/components/admin/Applications'),
        Header: () => import('@/components/admin/Header'),
    },
    data () {
      return {
      }
    },
  }
</script>
