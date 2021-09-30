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
                            <li v-for="lesson in lessons" v-bind:key="lesson.ls_id">
                                <a @click="activeLesson = lesson" >{{lesson.ls_title}}</a>
                            </li>
                        </ul>
                    </div>
                    <div class="column is-10">
                        
                        <template v-if="activeLesson">
                            <h3>{{activeLesson.ls_title}}</h3>
                        </template>
                        <template v-else>
                            <h3>{{course.cr_title}}</h3>
                        </template>

                        <template v-if="activeLesson">
                            {{activeLesson.ls_short}}
                        </template>
                        <template v-else>
                            {{ course.cr_short }}
                        </template>
                        
                        <template v-if="$store.state.isAuthenticated">
                            <hr>
                            <template v-if="activeLesson">
                                {{activeLesson.ls_long}}
                            </template>
                            <template v-else>
                                {{ course.cr_long }}
                            </template>
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
            course: {},
            lessons: [],
            activeLesson: ""
        }
    },
    mounted() {
        const slug = this.$route.params.slug
        axios
            .get(`/api/v1/courses/${slug}`)
            .then(response => {
                this.course = response.data.course
                this.lessons = response.data.lessons
            })
    }
}
</script>