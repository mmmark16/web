<template>
  <v-data-table
    :search="search"
    :headers="headers"
    :items="listRooms"
    flat
  >
    <template v-slot:top>
      <v-toolbar
        height="40px"
        flat
      >
        <v-dialog
          v-model="dialog"
          max-width="600px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-card-title class="data_search_input">
                <v-text-field
                    v-model="search"
                    append-icon="mdi-magnify"
                    label="Search"
                    single-line
                    hide-details
                    class="data_search pa-0 ma-0"
                ></v-text-field>
                <v-btn
                    width="120px"
                    height="40px"
                    color="#7FD4F1"
                    elevation="0"
                    v-bind="attrs"
                    v-on="on"
                    >
                    Add    
                </v-btn>
            </v-card-title>
          </template>
          <v-card ref="form">
            <v-form @submit.prevent="submitForm"> 
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        type="number"
                        ref="room_number"
                        v-model="room.room_number"
                        :rules="[rules.required]"
                        label="ID"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        :rules="[rules.required]"
                        v-model="room.name"
                        label="Name"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        type="number"
                        :rules="[rules.required]"
                        v-model="room.beds_number"
                        label="Room beds"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        type="number"
                        :rules="[rules.required]"
                        v-model="room.day_cost"
                        label="Day cost"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        :rules="[rules.required]"
                        v-model="room.room_class"
                        label="Class"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        :rules="[rules.required]"
                        v-model="room.description"
                        label="Description"
                        required
                      ></v-text-field>
                    </v-col>
                    <!-- <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        type="file"
                        :rules="[rules.required]"
                        v-model="room.photo"
                        label="Photo"
                        required
                      ></v-text-field>
                    </v-col> -->
                  </v-row>
                </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                type="submit"
              >
                Save
              </v-btn>
            </v-card-actions>
            </v-form>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Are you sure you want to delete?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>



<script>
  export default {
    data: () => ({
        dialog: false,
        dialogDelete: false,
        search: '',
        headers: [
            {
                text: 'Number',
                align: 'start',
                sortable: false,
                value: 'room_number',
            },
            { text: 'Name', value: 'name' },
            { text: 'Beds', value: 'beds_number' },
            { text: 'Day cost', value: 'day_cost' },
            { text: 'Class', value: 'room_class' },
            { text: 'Actions', value: 'actions', sortable: false },
        ],
        listRooms: [ ],
        editedIndex: -1,
        room: {
            room_number: 0,
            name: '',
            beds_number: 0,
            day_cost: 0,
            room_class: '',
            //photo: '',
            description: '',
        },
        defaultItem: {
            room_number: 0,
            name: '',
            beds_number: 0,
            day_cost: 0,
            room_class: '',
            //photo: '',
            description: '',
        },
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 6 || 'Min 6 characters',
          emailMatch: () => (`The email and password you entered don't match`),
        },
        //formHasErrors: false,
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New room' : 'Edit room'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
        this.loadListRooms()
    },

    methods: {
        async loadListRooms() {
            this.listRooms = await fetch(
                `${this.$store.getters.getServerUrl}rooms/`
            ).then(response => response.json())
        },

        editItem (item) {
            this.editedIndex = this.listRooms.indexOf(item)
            this.room = Object.assign({}, item)
            this.dialog = true
        },

        deleteItem (item) {
            this.editedIndex = this.listRooms.indexOf(item)
            this.room = Object.assign({}, item)
            this.dialogDelete = true
        },

        async deleteItemConfirm () {
            await this.loadListRooms();
            await fetch(
                `${this.$store.getters.getServerUrl}room/delete/${this.room.room_number}/`,
                {
                  method: 'delete',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(this.room)
                }
            );
            await this.loadListRooms();
            this.closeDelete()
        },

        close () {
            this.dialog = false
            this.$nextTick(() => {
            this.room = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        closeDelete () {
            this.dialogDelete = false
            this.$nextTick(() => {
            this.room = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        async submitForm() {
            await this.loadListRooms();
            if (this.editedIndex > -1) {
              this.editGuest();              
            } else {
              this.addGuest();
            }
            this.close()

        },

        async addGuest () {
          await fetch(
              `${this.$store.getters.getServerUrl}room/create/`,
              {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.room)
              }
          );
          await this.loadListRooms();
        },

        async editGuest () {
          console.log(this.room)
          await fetch(
              `${this.$store.getters.getServerUrl}room/update/${this.room.room_number}/`,
              {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.room)
              }
          );
          await this.loadListRooms();
          this.stusent = {};
        }
    },
  }
</script>


<style scoped>
    .v-btn {
        color:white!important;
        text-transform: none;
        font-weight: 500;
        font-size: 14px;
    }
    .data_search_input {
        padding:0;
    }
    .v-card__text {
        box-shadow: none!important;
    }
    .data_search {
        background: #F2F4F8;
        border-radius: 5px;
        margin-right:20px!important;
        height:40px;
        padding:0 20px!important;
        display: flex;
        align-items: center;
        max-width:300px;
    }
    .v-card__title {
      justify-content: center;
    }
</style>

<style>
    .v-data-table__wrapper {
        margin-top:30px;
    }
    .v-text-field > .v-input__control > .v-input__slot:before, .v-text-field > .v-input__control > .v-input__slot:after {
        content: none!important;
    }
    .v-toolbar__content {
        padding:0!important;
        display:flex;
        justify-content: flex-end;
    }
    .input_date input {
      width:136px!important;
    }
    .v-dialog .v-card{
      padding:10px;
    }
    .v-application .headline {
      font-family: 'Montserrat', sans-serif!important;
    }
</style>