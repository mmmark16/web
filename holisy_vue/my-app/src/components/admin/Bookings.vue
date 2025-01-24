<template>
  <v-data-table
    :search="search"
    :headers="headers"
    :items="listBookings"
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
                        ref="booking_id"
                        v-model="booking.booking_id"
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
                        type="number"
                        ref="client_id"
                        v-model="booking.client_id"
                        :rules="[rules.required]"
                        label="Client"
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
                        ref="room_number"
                        v-model="booking.room_number"
                        :rules="[rules.required]"
                        label="Room"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        type="date"
                        :rules="[rules.required]"
                        v-model="booking.arrival_date"
                        label="Arrival date"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        type="date"
                        :rules="[rules.required]"
                        v-model="booking.departure_date"
                        label="Departure date"
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
                        v-model="booking.result_cost"
                        label="Result cost"
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-autocomplete
                        :rules="[rules.required]"
                        v-model="booking.status"
                        :items="statuses"
                        label="Status"
                        required
                      ></v-autocomplete>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="booking.services"
                        label="Services"
                      ></v-text-field>
                    </v-col>
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
                text: 'ID',
                align: 'start',
                sortable: false,
                value: 'booking_id',
            },
            { text: 'Client', value: 'client_id' },
            { text: 'Room', value: 'room_number' },
            { text: 'Arrival date', value: 'arrival_date' },
            { text: 'Departure date', value: 'departure_date' },
            { text: 'Result cost', value: 'result_cost' },
            { text: 'Status', value: 'status' },
            { text: 'Services', value: 'services' },
            { text: 'Actions', value: 'actions', sortable: false },
        ],
        listBookings: [ ],
        statuses: ['Ожидает оплаты', 'На подтверждении', 'В процессе', 'Завершен'],
        editedIndex: -1,
        booking: {
            booking_id: 0,
            client_id: 0,
            arrival_date: '',
            departure_date: '',
            result_cost: 0,
            status: '',
            services: [],
        },
        defaultItem: {
            booking_id: 0,
            client_id: 0,
            arrival_date: '',
            departure_date: '',
            result_cost: 0,
            status: '',
            services: [],
        },
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 6 || 'Min 6 characters',
          emailMatch: () => (`The email and password you entered don't match`),
        },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New booking' : 'Edit booking'
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
        this.loadListBookings()
    },

    methods: {
        async loadListBookings() {
            this.listBookings = await fetch(
                `${this.$store.getters.getServerUrl}bookings/`
            ).then(response => response.json())
        },

        editItem (item) {
            this.editedIndex = this.listBookings.indexOf(item)
            this.booking = Object.assign({}, item)
            this.dialog = true
        },

        deleteItem (item) {
            this.editedIndex = this.listBookings.indexOf(item)
            this.booking = Object.assign({}, item)
            this.dialogDelete = true
        },

        async deleteItemConfirm () {
            await this.loadListBookings();
            await fetch(
                `${this.$store.getters.getServerUrl}booking/delete/${this.booking.booking_id}/`,
                {
                  method: 'delete',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(this.booking)
                }
            );
            await this.loadListBookings();
            this.closeDelete()
        },

        close () {
            this.dialog = false
            this.$nextTick(() => {
            this.booking = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        closeDelete () {
            this.dialogDelete = false
            this.$nextTick(() => {
            this.booking = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        async submitForm() {
            await this.loadListBookings();
            if (this.editedIndex > -1) {
              this.editGuest();              
            } else {
              this.addGuest();
            }
            this.close()
        },

        async addGuest () {
          switch (this.booking.status) {
            case 'Ожидает оплаты':
              this.booking.status = 'p'
              break;
            case 'На подтверждении':
              this.booking.status = 'v'
              break;
            case 'В процессе':
              this.booking.status = 'l'
              break;
            case 'Завершен':
              this.booking.status = 'c'
              break;
          }
          await fetch(
              `${this.$store.getters.getServerUrl}booking/create/`,
              {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.booking)
              }
          );
          await this.loadListBookings();
        },

        async editGuest () {
          switch (this.booking.status) {
            case 'Ожидает оплаты':
              this.booking.status = 'p'
              break;
            case 'На подтверждении':
              this.booking.status = 'v'
              break;
            case 'В процессе':
              this.booking.status = 'l'
              break;
            case 'Завершен':
              this.booking.status = 'c'
              break;
          }
          await fetch(
              `${this.$store.getters.getServerUrl}booking/update/${this.booking.booking_id}/`,
              {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.booking)
              }
          );
          await this.loadListBookings();
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