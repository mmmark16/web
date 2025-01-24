<template>
    <header class="header d-flex justify-space-between align-center">
        <ul class="right_menu d-flex pa-0">
            <li><a href="">Rooms</a></li>
            <li><a href="">Services</a></li>
            <li><a href="">Contacts</a></li>
        </ul>
        <logo />
        <div class="left_menu">
            <div v-if="this.block == 1">
                <v-btn 
                    class="button"
                    elevation="0"
                    color="#ECFAFF"
                    href="/login"
                >
                    Log in
                </v-btn>
                <v-btn 
                    class="button button_signup"
                    elevation="0"
                    color="#7FD4F1"
                    text-color="white"
                    href="/signup"
                >
                    Sign up
                </v-btn>
            </div>

            <div class="profile d-flex" v-else-if="this.block == 2">
                <div class="profile_info">
                    <p class="name">{{username}}</p>
                    <p class="post">{{role}}</p>
                </div>
                <v-avatar color="warning lighten-2" size="35">
                    <v-icon dark>
                        mdi-account-circle
                    </v-icon>
                </v-avatar>
                <v-btn
                    depressed
                    color="orange ml-4 text white--text"
                    @click="logout()"
                >
                    Log out
                </v-btn>
            </div>
        </div>
    </header>
</template>


<script>
    import $ from 'jquery'
  export default {
    data () {
      return {
        block: 1,
        username: '',
        role: ''
      }
    },

    components: {
        Logo: () => import('@/components/Logo'),
    },

    created () {
        this.isLogin()
    },

    methods: {
        async isLogin () {
            let token = localStorage.getItem("auth_token");
            if (token) {
                this.block = 2
                $.ajax({
                    url: `${this.$store.getters.getServerUrl}auth/users/me`,
                    type: "GET",
                    headers: {
                        Authorization: "Token "+token
                    },
                    success: (response) => {
                        this.username = response.username;
                        if (response.post)
                            this.role = response.post;
                        else if (this.username == "Admin")
                            this.role = 'Admin account'
                        else 
                            this.role = 'Guest'
                    },
                    error: (response) => {
                        
                    }
                });
            } else {
                this.block = 1
            }
        },

        logout () {
            localStorage.removeItem("auth_token");
            window.location.replace("/");
        }
    }
  }
</script>


<style scoped>
    .header {
        padding:20px 160px;
        background-color: #d4f2ff;
    }
    .button {
        text-transform: none;
        margin-left:15px;
        padding:10px 20px!important;
    }
    .button_signup {
        color:white!important;
    }
    .right_menu li {
        list-style: none;
        margin-right:30px;
    }
    .right_menu li a {
        color:black;
        text-decoration: none;
    }
    .right_menu li a:hover {
        text-decoration: underline;
    }
    .profile_info {
        margin-right:10px;
    }
    .profile_info p {
        margin-bottom:0;
        font-size: 14px;
        line-height: 17px;
        text-align: right;
    }
    .profile_info .name {
        font-weight: 700;
    }
    .profile_info .post {
        color: #AEAEAE;
    }
</style>