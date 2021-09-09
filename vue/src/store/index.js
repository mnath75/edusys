import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      username: '',
      id: ''
    },
    token: '',
    isAuthenticated: false
  },
  mutations: {
    // get info about the user from the browser to set the app
    initializeStore(state){
      if(localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.id = localStorage.getItem('id')
        state.user.username = localStorage.getItem('username')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.id = ''
        state.user.username = ''
      }
    },
    // set token at login
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    },
    // remove token at logout
    removeToken(state){
      state.token = ''
      state.isAuthenticated = false
    },
    // see Login.vue + settings DRF
    setUser(state, user){
      state.user = user
    }
  },
  actions: {
  },
  modules: {
  }
})
