<template>
  <v-card
    class="mx-auto left_bar"
    flat
  >
    <v-navigation-drawer permanent
        width="100%"
    >
      <logo />

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <router-link :to="item.value">
            <v-list-item-icon>
              <v-icon
                  color="#C7C7C7"
              >{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </router-link> 
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          { title: 'Users', icon: 'mdi-account-box-multiple', value: 'users'},
          { title: 'Rooms', icon: 'mdi-bed-king', value: 'rooms'},
          { title: 'Services', icon: 'mdi-room-service', value: 'services'},
          { title: 'Bookings', icon: 'mdi-bed', value: 'bookings'},
          { title: 'Applications', icon: 'mdi-format-list-bulleted', value: 'applications'},
        ],
        right: null,
      }
    },

    components: {
        Logo: () => import('@/components/Logo'),
    },
  }
</script>

<style scoped>
    .left_bar { 
      height: 100vh;
      width: 100%;
    }
    .v-list--nav {
      margin-top:40px;
      padding:0;
    }
    .v-list-item {
      padding:0!important;
      border-radius: 5px;
    }
    .v-list-item a {
      display: flex;
      width: 100%;
      text-decoration: none;
      padding: 2px 18px!important;
      border-radius: 5px;
    }
    .v-list-item a.router-link-active {
      background: #F0F7FF;
      color:#197BBD;
    }
    .v-list-item a.router-link-active i {
      color:#197BBD!important;
    }
    .v-list-item > * {
       color: #C7C7C7;
    }
    .v-list-item__icon {
      margin-right:18px;
    }
</style>

<style>
    .v-navigation-drawer__content {
        padding:40px;
    }
</style>