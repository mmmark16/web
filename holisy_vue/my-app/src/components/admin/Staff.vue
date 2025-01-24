<template>
  <v-data-table
    :search="search"
    :headers="headers"
    :items="listStaffs"
    flat
  >
    <template v-slot:top>
      <v-toolbar
        height="0"
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
                        ref="user_id"
                        v-model="employee.user_id"
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
                        v-model="employee.username"
                        label="Username"
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
                        v-model="employee.first_name"
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
                        :rules="[rules.required]"
                        v-model="employee.last_name"
                        label="Surname"
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
                        class="input_date"
                        v-model="employee.birth_date"
                        label="Birth date"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        type="email"
                        :rules="[rules.required]"
                        v-model="employee.email"
                        label="Email"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        type="tel"
                        :rules="[rules.required]"
                        v-model="employee.phone"
                        label="Phone"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col
                      cols="12"
                      sm="6"
                      md="4"
                    >
                      <v-text-field
                        v-model="employee.password"
                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                        :rules="[rules.required, rules.min]"
                        :type="show1 ? 'text' : 'password'"
                        label="Password"
                        required
                        @click:append="show1 = !show1"
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
                value: 'user_id',
            },
            { text: 'Name', value: 'first_name' },
            { text: 'Surname', value: 'last_name' },
            { text: 'Birthdate', value: 'birth_date' },
            { text: 'Email', value: 'email' },
            { text: 'Phone', value: 'phone' },
            { text: 'Post', value: 'post' },
            { text: 'Salary', value: 'salary' },
            { text: 'Actions', value: 'actions', sortable: false },
        ],
        listStaffs: [ ],
        editedIndex: -1,
        employee: {
            user_id: 0,
            first_name: '',
            last_name: '',
            birth_date: '',
            email: '',
            phone: '',
            password: '',
            post: '',
            salary: 0,
            username: '',
        },
        defaultItem: {
            user_id: 0,
            first_name: '',
            last_name: '',
            birth_date: '',
            email: '',
            phone: '',
            password: '',
            post: '',
            salary: 0,
            username: '',
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
        return this.editedIndex === -1 ? 'New employee' : 'Edit employee'
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
        this.loadListStaffs()
    },

    methods: {
        async loadListStaffs() {
            this.listStaffs = await fetch(
                `${this.$store.getters.getServerUrl}employees/`
            ).then(response => response.json())
        },

        editItem (item) {
            this.editedIndex = this.listStaffs.indexOf(item)
            this.employee = Object.assign({}, item)
            this.dialog = true
        },

        deleteItem (item) {
            this.editedIndex = this.listStaffs.indexOf(item)
            this.employee = Object.assign({}, item)
            this.dialogDelete = true
        },

        async deleteItemConfirm () {
            await this.loadListStaffs();
            await fetch(
                `${this.$store.getters.getServerUrl}user/delete/${this.employee.user_id}/`,
                {
                  method: 'delete',
                  headers: {
                      'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(this.employee)
                }
            );
            await this.loadListStaffs();
            this.closeDelete()
        },

        close () {
            this.dialog = false
            this.$nextTick(() => {
            this.employee = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        closeDelete () {
            this.dialogDelete = false
            this.$nextTick(() => {
            this.employee = Object.assign({}, this.defaultItem)
            this.editedIndex = -1
            })
        },

        async submitForm() {
            await this.loadListStaffs();
            if (this.editedIndex > -1) {
              this.editStaff();              
            } else {
              this.addStaff();
            }
            this.close()

            //this.formHasErrors = false

            //Object.keys(this.form).forEach(f => {
              //if (!this.form[f]) this.formHasErrors = true
              //this.$refs[f].validate(true)
            //})

            // console.log(this.formHasErrors);

            // if (this.formHasErrors = false)
            //   this.close()
        },

        async addStaff () {
          await fetch(
              `${this.$store.getters.getServerUrl}user/create/`,
              {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.employee)
              }
          );
          await this.loadListStaffs();
        },

        async editStaff () {
          await fetch(
              `${this.$store.getters.getServerUrl}user/update/${this.employee.user_id}/`,
              {
                method: 'put',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.employee)
              }
          );
          await this.loadListStaffs();
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
        position:absolute;
        bottom:100%;
        right:0;
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
