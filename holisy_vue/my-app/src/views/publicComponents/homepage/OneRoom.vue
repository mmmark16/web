<template>
    <div class="container mt-10">
        <v-card flat class="d-flex">
            <img :src="room.photo" alt="room">
            <div class="room_info">
                <h1>{{room.name}}</h1>
                <div class="info_item">
                    <span>Class: </span>
                    {{room.room_class}}
                </div>
                <div class="info_item">
                    <span>Beds number: </span>
                    {{room.beds_number}}
                </div>
                <div class="info_item">
                    <span>Day cost: </span>
                    {{room.day_cost}}
                </div>
                <div class="info_item">
                    <span>Description: </span>
                    {{room.description}}
                </div>
                <v-btn
                    class="book_button"
                    @click="bookRoom()"
                >
                    Book a room
                </v-btn>
                <v-dialog
                    v-model="dialog"
                    max-width="600px"
                >
                <v-card ref="form">
                    <v-form @submit.prevent="addBooking"> 
                    <v-card-title>
                    <span class="headline">Book a room</span>
                    </v-card-title>

                    <v-card-text>
                        <v-container>
                        <v-row>
                            <v-col
                            cols="12"
                            sm="12"
                            md="12"
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
                            sm="12"
                            md="12"
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
                            sm="12"
                            md="12"
                            >
                            <v-text-field
                                type="number"
                                :rules="[rules.required]"
                                v-model="booking.person_count"
                                label="Person Count"
                                required
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
                        Book
                    </v-btn>
                    </v-card-actions>
                    </v-form>
                </v-card>
                </v-dialog>
            </div>
        </v-card>
        
    </div>
</template>

<script>
import $ from 'jquery'  
export default {
    name: 'oneRoom',
    data () {
      return {
        dialog: false,
        id: this.$route.params['id'],
        room: {},
        bookings: [],
        booking: {
            booking_id: 0,
            client_id: 0,
            room_number: 0,
            arrival_date: '',
            departure_date: '',
            person_count: 0,
            result_cost: 0,
        },
        defaultItem: {
            booking_id: 0,
            client_id: 0,
            room_number: 0,
            arrival_date: '',
            departure_date: '',
            person_count: 0,
            result_cost: 0,
        },
        rules: {
          required: value => !!value || 'Required.',
        },
      }
    },
    watch: {
      dialog (val) {
        val || this.close()
      },
    },
    created(){
        this.LoadRoom()
        let token = localStorage.getItem("auth_token");
        $.ajax({
            url: `${this.$store.getters.getServerUrl}auth/users/me`,
            type: "GET",
            headers: {
                Authorization: "Token "+token
            },
            success: (response) => {
                this.booking.client_id = response.user_id;
            },
            error: (response) => {
                
            }
        });
    },
    methods: {
        async LoadRoom(){
            this.room = await fetch(
                `${this.$store.getters.getServerUrl}room/${this.id}/`
            ).then(response => response.json())
            this.booking.room_number = this.room.room_number;
            this.defaultItem.room_number = this.room.room_number;
            this.bookings = await fetch(
                `${this.$store.getters.getServerUrl}bookings/`
            ).then(response => response.json())
            this.booking.booking_id = this.bookings['length'] + 1;
            this.defaultItem.booking_id = this.bookings['length'] + 1;
        }, 

        bookRoom () {
            let token = localStorage.getItem("auth_token");
            if (token) {
                this.dialog = true
            } else {
                window.location.replace("/login");
            }
        },

        close () {
            this.dialog = false
            this.$nextTick(() => {
                this.booking = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },

        async addBooking () {
            await fetch(
                `${this.$store.getters.getServerUrl}booking/create/`,
                {
                    method: 'post',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.booking),
                },
                alert('Номер забронирован!')
            );
            this.dialog = false;
        },
    }
  }
</script>

<style scoped>
    .container {
        padding:0;
    }
    img {
        border-radius: 5px;
        width:550px;
        height: 460px;
        object-fit: cover;
    }
    .room_info {
        padding-left:40px;
    }
    .info_item {
        font-size:18px;
        color:black;
        margin-top: 20px;
    }
    .info_item span {
        font-weight: 600;
    }
    .book_button {
        padding: 0 25px!important;
        margin-top:20px;
        background: #5c6bc0!important;
        color:white!important;
        text-transform: none;
    }
    .headline {
        text-align:center;
        width:100%;
    }
</style>