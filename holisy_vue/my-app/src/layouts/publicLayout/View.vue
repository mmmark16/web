<template>
  <v-main>
    <router-view />
  </v-main>
</template>

<script>
export default {
  name: 'Publicview',
  data() {
    return {
      visible: true,
    };
  },
  computed: {},
};
</script>