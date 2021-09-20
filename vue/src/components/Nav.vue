<template>
    <nav class="navbar is-link" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item is-size-4">EduSys</router-link>
        </div>
        <div id="navbar-item" class="navbar-menu">
            <div class="navbar-start">
                <router-link to="/" class="navbar-item">Home</router-link>
                <router-link to="/about" class="navbar-item">About</router-link>
                <router-link to="/courses" class="navbar-item">Courses</router-link>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                <div class="buttons">
                    <template v-if="$store.state.isAuthenticated">
                        <router-link to="/dashboard/account" class="button is-warning">Account</router-link>
                    </template>
                    <template v-else>
                        <a class="button is-success" href="/signup"><strong>Sign up</strong></a>
                        <a class="button is-light" href="/login"><strong>Log in</strong></a>
                    </template>
                </div>
                </div>
            </div>
        </div>
    </nav>
</template>