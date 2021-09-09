<template>
  <div class="login">

    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Log in EduSys</h1>
      </div>
    </div>
    
    <section class="section">
      <div class="container">
          <div class="columns">
              <div class="column is-4 is-offset-4">
                  <form v-on:submit.prevent="submitForm">
                      <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                      <p v-for="e in errors" v-bind:key="e">
                        {{ e }}
                      </p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-warning">Log in</button>
                        </div>
                    </div>
                  </form>
              </div>
          </div>
      </div>
    </section>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  methods: {
    async submitForm() {
      this.errors = []

      axios.defaults.headers.common['Authorization'] = '' // reset auth

      localStorage.removeItem('token') // remove token from different session

      if (this.username == ''){
        this.errors.push('The user is missing')
      }

      if (this.password == ''){
        this.errors.push('The password is missing')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        await axios
            .post('/api/v1/token/login/', formData)
            .then(response => {
              const token = response.data.auth_token
              this.$store.commit('setToken',token)
              axios.defaults.headers.common['Authorization'] = 'Token ' + token
              localStorage.setItem('token', token)
            })
            .catch(error => {
              if(error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
                console.log(JSON.stringify(error.response.data))
              } else if (error.message) {
                  this.errors.push('Something went wrong. Try again later')
                  console.log(JSON.stringify(error.message))
              } else {
                  console.log(JSON.stringify(error))
              }
            })

        axios
            .get('/api/v1/users/me/')
            .then(response => {
                this.$store.commit('setUser', {
                    'id': response.data.id,
                    'username': response.data.username
                })
                localStorage.setItem('username', response.data.username)
                localStorage.setItem('userid', response.data.id)
                this.$router.push('/dashboard/account') // redirect to dashboard
            })
            .catch(error => {
                console.log(JSON.stringify(error))
            })

      }

    }
  }
}
</script>