<template>
  <div class="about">

    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">About EduSys</h1>
      </div>
    </div>
    
    <section class="section">
      This is the about page
    </section>

  </div>
</template>
<script>
export default {
  name: 'About',
  mounted() {
    document.title = 'About | EduSys'
  }
}
</script>