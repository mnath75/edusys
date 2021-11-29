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
                                <a @click="setActiveLesson(lesson)" >{{lesson.ls_title}}</a>
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
                                <hr>

                                <article class="media box" v-for="comment in comments" v-bind:key="comment.cm_id">
                                    <div class="media-content">
                                        <div class="content">
                                            <p>
                                                <strong>{{ comment.cm_title }}</strong> <br>
                                                {{ comment.cm_content }} <br>
                                                <em>{{ comment.cm_created_at }}</em>
                                            </p>
                                        </div>
                                    </div>
                                </article>

                                <form v-on:submit.prevent="submitComment()">
                                    <div class="field">
                                        <label class="label">Title</label>
                                        <div class="control">
                                            <input type="text" class="input" v-model="comment.title">
                                        </div>
                                    </div>
                                    <div class="field">
                                        <label class="label">Content</label>
                                        <div class="control">
                                            <textarea type="text" class="textarea" v-model="comment.content"></textarea>
                                        </div>
                                    </div>
                                    <div class="notification is-danger" v-for="error in errors" v-bind:key="error">
                                        {{ error }}
                                    </div>
                                    <div class="field">
                                        <div class="control">
                                            <button class="button is-link">Submit</button>
                                        </div>
                                    </div>
                                </form>

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
            comments: [],
            activeLesson: "",
            comment: {
                title: '',
                content: ''
            },
            errors: []
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
    },
    methods: {
        setActiveLesson(lesson){
            this.activeLesson = lesson
            this.getComments()
        },
        getComments(){
            axios
                .get(`/api/v1/courses/${this.course.cr_slug}/${this.activeLesson.ls_slug}/comments`)
                .then(response => {
                    this.comments = response.data
                })
        },
        submitComment(){

            this.errors = [] // reset at each submission
            if(this.comment.title === ''){
                this.errors.push('Fill in the title!')
            }

            if(this.comment.content === ''){
                this.errors.push('Fill in the content!')
            }

            if(!this.errors.length){
                axios
                    .post(`/api/v1/courses/${this.course.cr_slug}/${this.activeLesson.ls_slug}`, this.comment)
                    .then(response => {
                        this.comment.title = '' // reset form
                        this.comment.content = ''

                        alert('Cool! Your comment is in')
                        this.getComments() // reload comment list
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }

        }
    }
}
</script>