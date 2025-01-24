<template>
  <v-card
    class="mx-auto container"
    tile
    flat
  >
    <h1>Rooms</h1>
    <v-list dense class="v-lists">
      <v-list-item-group
        color="primary" 
        @click:row="goTo"
      >
        <v-list-item class="v-list-items pa-0 ml-2 mr-2 mb-4"
            v-for="room in listRooms" :key="room.room_number"
        >
          <v-hover v-slot="{ hover }">
            <v-card
              class="mx-auto"
              color="grey lighten-4"
              width="100%"
              flat
            >
              <v-img
                :aspect-ratio="16/9"
                :src="room.photo"
              >
                <v-expand-transition>
                  <div
                    v-if="hover"
                    class="d-flex transition-fast-in-fast-out darken-2 v-card--reveal text-h4 white--text"
                    style="height: 100%;"
                  >
                    ${{ room.day_cost }}
                  </div>
                </v-expand-transition>
              </v-img>
              <v-card-text
                class="pt-4"
                style="position: relative;"
              >
                <v-btn
                  absolute
                  color="#20DF7F"
                  class="white--text"
                  fab
                  large
                  right
                  top
                  :to="`/room/${room.room_number}`"
                >
                  <v-icon>mdi-eye</v-icon>
                </v-btn>
                <div class="font-weight-light grey--text text-h8 mb-1">
                  {{ room.room_class }}
                </div>
                <h3 class="text-h5 font-weight-light mb-1">
                  {{ room.name }}
                </h3>
                <div class="font-weight-light text-h8 mb-1">
                  {{ room.description.substr(0, 95)+"..." }}
                </div>
              </v-card-text>
            </v-card>
          </v-hover>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
  
</template>

<script>
    export default {
        name: 'Rooms',
        data: () => ({
          listRooms: [ ],
        }),
        created () {
            this.loadListRooms()
        },
        methods: {
          async loadListRooms() {
              this.listRooms = await fetch(
                  `${this.$store.getters.getServerUrl}rooms/`
              ).then(response => response.json())
          },
        }
    }
</script>

<style scoped>
  .text-h5 {
    color:#20DF7F;
  }
  .v-card--reveal {
    background-color: #20DF7F;
  }
  .v-item-group {
    display: flex;
    flex-wrap: wrap;
  }
  .v-list-items {
    flex: 0 0 31.9%;
  }
  h1 {
    color:#445964;
    margin:30px 0 15px 5px;
  }
</style>

<style>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 1;
  position: absolute;
  width: 100%;
}
.container {
  padding:0 160px;
}
</style>