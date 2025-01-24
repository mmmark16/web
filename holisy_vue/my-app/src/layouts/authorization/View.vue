<template>
  <v-main>
    <v-app>
      <router-view />
    </v-app>
  </v-main>
</template>

<script>
export default {
  name: 'Authview',
  data() {
    return {
      visible: true,
    };
  },
  computed: {},
};
</script>