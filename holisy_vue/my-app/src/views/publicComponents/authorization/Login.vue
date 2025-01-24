<template>
  <div>
  <logo />
  <v-card
    class="mx-auto"
    style="max-width: 500px;"
    flat
  >
    <h1>Log in</h1>
    <v-form
      ref="form"
      class="pa-0 pt-3"
    >
      <v-text-field
        v-model="username"
        filled
        color="deep-purple"
        label="Username"
        required
      ></v-text-field>
      <v-text-field
        v-model="password"
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
        @click="setLogin()"
      >
        Submit
      </v-btn>
    </v-card-actions>
    <a href="/signup">Go to registration</a>
  </v-card>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: 'Login',
    data: () => ({
      username: undefined,
      password: undefined,
    }),
    components: {
        Logo: () => import('@/components/Logo'),
    },
    methods: {
      async setLogin() {
        $.ajax({
          url: `${this.$store.getters.getServerUrl}auth/token/`,
          type: "POST",
          data: {
            username: this.username,
            password: this.password
          },
          success: (response) => {
            localStorage.setItem("auth_token", response.token);
            if (this.username == "Admin")
              window.location.replace("/admin");
            else {
              window.location.replace("/");
            }
          },
          error: (response) => {
            if (response.status === 400) {
              alert("Логин или пароль неверный");
            }
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