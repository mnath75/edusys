<template>
  <div>
    <Nav/>

    <router-view/>

    <Footer/>
  </div>
</template>

<script>
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'

export default {
  name: 'App',
  components: {
    Nav,
    Footer
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
