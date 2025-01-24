<template>
  <div class="admin_wrapper">
      <div class="admin_left">
        <left-bar />       
      </div>
      <div class="admin_right">
        <pub-view />
      </div>
  </div>
</template>



<script>
export default {
  name: 'Public',
  components: {
    PubView: () => import('./View'),
    leftBar: () => import('./LeftBar'),
  },
};
</script>

<style scoped>
    .admin_wrapper {
        display:flex;
    }
    .admin_left {
        width:265px;
    }
    .admin_right {
        flex-grow: 3;
        padding:0 40px;
        margin-top:40px;
    }
</style>
