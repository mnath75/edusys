<template>
    <div class="courses">

        <div class="hero is-info is-medium">
            <div class="hero-body has-text-centered">
                <h1 class="title">{{ course.cr_title }}</h1>
            </div>
        </div>
        
        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <h2>Table of contents</h2>
                        <ul>
                            <li><a href="#" >Intro</a></li>
                            <li><a href="#">Part 1</a></li>
                            <li><a href="#">Part 2</a></li>
                            <li><a href="#">Summary</a></li>
                        </ul>
                    </div>
                    <div class="column is-10">
                        <h3>Intro</h3>
                        {{ course.cr_short }}
                        
                        <template v-if="$store.state.isAuthenticated">
                            <hr>
                            {{ course.cr_long }}
                        </template>
                        <template v-else class="has-text-centered">
                            <hr>
                            <h2>Restricted access</h2>
                            <p>You need to have an account to follow the course!</p>
                        </template>
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
            course: []
        }
    },
    mounted() {
        const slug = this.$route.params.slug
        axios
            .get(`/api/v1/courses/${slug}`)
            .then(response => {
                this.course = response.data
            })
    }
}
</script>