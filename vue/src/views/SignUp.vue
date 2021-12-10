<template>
  <div class="signup">

    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Sign in EduSys</h1>
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

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="passcheck">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                      <p v-for="e in errors" v-bind:key="e">
                        {{ e }}
                      </p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-warning">Sign up</button>
                        </div>
                    </div>

                    <router-link to="/login">Or click here to login </router-link>

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
      passcheck: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Sign up | EduSys'
  },
  methods: {
    submitForm() {
      this.errors = []

      if (this.username == ''){
        this.errors.push('The user is missing')
      }

      if (this.password == ''){
        this.errors.push('The password is missing')
      }

      if (this.password !== this.passcheck){
        this.errors.push('The password does not match')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password
        }

        axios
            .post('/api/v1/users/', formData)
            .then(response => {
              this.$router.push('/login')
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

      }

    }
  }
}
</script>
