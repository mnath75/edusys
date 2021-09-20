<template>
  <div class="about">

    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Your account</h1>
      </div>
    </div>
    
    <section class="section">
        <h2 class="subtitle">This is account page of: {{ $store.state.user.username }}</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
        <hr>
        <button @click="logout()" class="button is-danger">Log out</button>
    </section>

  </div>
</template>

<script>
import axios from 'axios'
export default {
    methods: {
        async logout() {
          await axios
                    .post('/api/v1/token/logout/')
          axios.defaults.headers.common['Authorization'] = '' // reset auth
          localStorage.removeItem('token') // remove token from different session
          this.$store.commit('removeToken')
          this.$router.push('/')
        }
    }
}
</script>
