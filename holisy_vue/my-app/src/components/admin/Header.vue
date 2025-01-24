<template>
    <header class="d-flex justify-space-between">
        <h1>{{ title }}</h1>
        <div class="profile d-flex">
            <div class="profile_info">
                <p class="name">Admin</p>
                <p class="post">Admin account</p>
            </div>
            <v-avatar color="warning lighten-2" size="35">
                <v-icon dark>
                    mdi-account-circle
                </v-icon>
            </v-avatar>
        </div>
    </header>
</template>

<style scoped>
    h1 {
        font-weight: 500;
        font-size: 20px;
        line-height: 1;
        text-transform: capitalize;
    }
    header {
        margin-bottom:40px;
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


<script>
    export default {
        data () {
            return {
                title: window.location.href.split('/')[4],
            }
        }
    }
</script>