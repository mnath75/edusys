<template>
  <div>
    <Nav/>

    <router-view/>

    <Footer/>
  </div>
</template>

<script>
import axios from 'axios'
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'

export default {
  name: 'App',
  components: {
    Nav,
    Footer
  },
  beforeCreate(){
    // before rendering the app, set the store (store/index.js)
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token ' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
