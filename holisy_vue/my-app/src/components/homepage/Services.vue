<template>
<v-card class="container" flat>
    <h1>Services</h1>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left">
              Name
            </th>
            <th class="text-left">
              Description
            </th>
            <th class="text-left">
              Cost
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in servicesList"
            :key="item.name"
          >
            <td>{{ item.name }}</td>
            <td>{{ item.description }}</td>
            <td>{{ item.cost }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </v-card>
</template>


<script>
  export default {
    data () {
      return {
        servicesList: [],
      }
    },
    created () {
        this.loadListServices()
    },
    methods: {
        async loadListServices() {
            this.servicesList = await fetch(
                `${this.$store.getters.getServerUrl}services/`
            ).then(response => response.json())
        },
    }
  }
</script>

<style scoped>

  h1 {
    color:#445964;
    margin:30px 0 15px 5px;
  }
  td, th {
    padding:20px!important;
  }
</style>