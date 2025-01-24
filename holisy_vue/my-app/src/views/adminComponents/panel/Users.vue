<template>
    <v-card
        flat
    >
        <Header />
        <v-tabs
        v-model="tab"
        background-color="transparent"
        color="basil"
        grow
        >
            <v-tab
                v-for="item in items"
                :key="item"
            >
                {{ item }}
            </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
            <v-tab-item>
                <Guests />
            </v-tab-item>
            <v-tab-item>
                <Staff />                
            </v-tab-item>
        </v-tabs-items>
    </v-card>
</template>


<script>
  export default {
    components: {
        Guests: () => import('@/components/admin/Guests'),
        Staff: () => import('@/components/admin/Staff'),
        Header: () => import('@/components/admin/Header'),
    },
    data () {
      return {
        tab: null,
        items: [
          'Guests', 'Staff',
        ],
      }
    },
  }
</script>


<style scoped>
    .v-tabs-items {
        overflow: visible;
    }
    .v-slide-group__content .v-tab {
        border:0;
        border-bottom: 1px solid #DDDDDD;
        text-transform: none;
        border-radius: 5px 5px 0px 0px;
    }
    .v-slide-group__content .v-tab--active {
        border: 1px solid #E6EAE8;
        border-bottom:0;
    }
</style>

<style>
    .v-slide-group__wrapper {
        flex: 0 0 auto!important;
        width:auto!important;
    }
    .v-tabs-bar {
        height:40px!important;
    }
    .v-tabs-slider-wrapper {
        display:none!important;
    }
</style>