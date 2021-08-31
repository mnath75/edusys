<template>
  <div class="signup">

    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Sign in EduSys</h1>
      </div>
    </div>
    
    <section class="section">
      <div class="container">
          <div class="columns">
              <div class="column is-4 is-offset-4">
                  <form>
                      <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" class="input">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input">
                        </div>
                    </div>

                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" class="input">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-warning">Sign up</button>
                        </div>
                    </div>

                    <router-link to="/login">Or click here to login </router-link>

                  </form>
              </div>
          </div>
      </div>
    </section>

  </div>
</template>