<template>
  <div>
  <logo />
  <v-card
    class="mx-auto"
    style="max-width: 500px;"
    flat
  >
    <h1>Sign up</h1>
    <v-form
      ref="form"
      class="pa-0 pt-3"
    >
      <v-text-field
        v-model="username"
        :rules="[rules.required]"
        filled
        color="deep-purple"
        label="Username"
        required
      ></v-text-field>
      <v-text-field
        v-model="phone"
        :rules="[rules.required]"
        filled
        color="deep-purple"
        label="Phone number"
        required
      ></v-text-field>
      <v-text-field
        v-model="email"
        :rules="[rules.email]"
        filled
        color="deep-purple"
        label="Email address"
        type="email"
        required
      ></v-text-field>
      <v-text-field
        v-model="password"
        :rules="[rules.required]"
        filled
        color="deep-purple"
        label="Password"
        type="password"
        required
      ></v-text-field>
    </v-form>
    <v-card-actions>
      <v-btn
        class="white--text"
        color="accent-4"
        depressed
        @click="setSignup()"
      >
        Submit
      </v-btn>
    </v-card-actions>
    <a href="/login">Go to login</a>
  </v-card>
  </div>
</template>

<script>
  import $ from 'jquery'
  export default {
    name: 'Signup',
    data: () => ({
      username: undefined,
      email: undefined,
      password: undefined,
      phone: undefined,
      user_id: null,
      rules: {
        email: v => !!(v || '').match(/@/) || 'Please enter a valid email',
        length: len => v => (v || '').length >= len || `Invalid character length, required ${len}`,
        password: v => !!(v || '').match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$/) ||
          'Password must contain an upper case letter, a numeric character, and a special character',
        required: v => !!v || 'This field is required',
      },
    }),
    components: {
        Logo: () => import('@/components/Logo'),
    },


    methods: {
      async setSignup() {
        let users = await fetch(
            `${this.$store.getters.getServerUrl}users/`
        ).then(response => response.json())
        this.user_id = users['length'] + 1;
        $.ajax({
          url: `${this.$store.getters.getServerUrl}auth/users/`,
          type: "POST",
          data: {
            username: this.username,
            password: this.password,
            email: this.email,
            phone: this.phone,
            user_id: this.user_id,
          },
          success: (response) => {
            window.location.replace("/login");
          },
          error: (response) => {
              alert("Ошибка");
          }
        })
      }
    }
  }
</script>


<style scoped>
  .v-card {
    background:none!important;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position:fixed;
    top:0;
    bottom:10vh;
    left:0;
    right:15vw;
  }
  h1 {
    color:#445964;
  }
  a {
    color:#445964;
    text-decoration: none;
    font-size: 14px;
  }
  a:hover {
    text-decoration: underline;
  }
  .logo_wrapper {
    margin-top:40px;
    margin-left:100px;
  }
</style>

<style>
.theme--light.v-text-field--filled > .v-input__control > .v-input__slot {
    background: #224957!important;
    width:300px;
  }
  .theme--light.v-label {
    color:white!important;
  }
  .v-text-field--filled {
    border-radius: 5px!important;
  }
  .theme--light.v-text-field > .v-input__control > .v-input__slot:before {
    content:none;
  }
  .v-card__actions > .v-btn.v-btn {
    width:300px;
    background-color: #20DF7F!important;
  }
  .v-messages__message {
    max-width:276px;
  }
</style>