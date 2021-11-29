<template>
    <div class="courses">

        <div class="hero is-info is-medium">
            <div class="hero-body has-text-centered">
                <h1 class="title">EduSys Courses</h1>
            </div>
        </div>
        
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column is-2">
                        <aside class="menu">
                            <p class="menu-label">Categories</p>
                            <ul class="menu-list">
                                <li>
                                    <a v-bind:class="{'is-active': !activeCategory}" 
                                        v-on:click="setActiveCategory('')">All courses</a>
                                </li>
                                <li v-for="category in categories" v-bind:key="category.ct_id" 
                                    v-bind:class="{'is-active': category.ct_id == activeCategory.ct_id}" 
                                    v-on:click="setActiveCategory(category)" >
                                    <a href="#">{{category.ct_title}}</a>
                                </li>
                            </ul>
                        </aside>
                    </div>
                    <div class="column is-10">
                        <p class="title">Courses</p>
                        <div class="columns is-multiline">
                            <div class="column is-4" v-for="course in courses" v-bind:key="course.cr_id">
                                <CourseCard v-bind:card="course" />
                            </div>
                        </div>
                        <div class="column is-12">
                            <nav class="pagination">
                                <a href="" class="pagination-previous">Previous</a>
                                <a href="" class="pagination-next">Next</a>
                                <ul class="pagination-list">
                                    <li><a class="pagination-link is-current">1</a></li>
                                    <li><a class="pagination-link">2</a></li>
                                    <li><a class="pagination-link">3</a></li>
                                    <li><a class="pagination-link">4</a></li>
                                </ul>
                            </nav>
                        </div>
                    </div>
                    
                </div>
            </div>
        </section>

    </div>
</template>

<script>
import axios from 'axios'
import CourseCard from '@/components/CourseCard'

export default {
    data() {
        return {
            categories: [],
            activeCategory: '',
            courses: []
        }
    },
    async mounted() {

        // when data retrieved, load page in DOM
        await axios
            .get('/api/v1/courses/categories/')
            .then(response => {
                this.categories = response.data
            })
        
        await this.getCourses()

    },
    components: {
        CourseCard
    }, // load components
    methods: {
        setActiveCategory(category) {
            console.log('setting category',category)
            this.activeCategory = category
            this.getCourses()
        },
        getCourses() {
            const params = {
                'category_id': this.activeCategory.ct_id
            }
            axios
                .get('/api/v1/courses/', {params})
                .then(response => {
                    console.log(response.data)
                    this.courses = response.data
                })
        }
    }
}
</script>
