<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <img v-bind:src="card.get_image" alt="image">
            </figure>
        </div>
        <div class="card-content">
            <div class="media">
                <div class="media-content">
                    <p class="is-size-5">{{ card.cr_title }} </p>
                </div>
            </div>
            <div class="content">
                <p> {{ card.cr_short }} </p>
                <router-link :to="{'name': 'Course', params: {slug: card.cr_slug }}">More</router-link>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    props: ['card']
}
</script>
