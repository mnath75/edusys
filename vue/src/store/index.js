import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {
      token: '',
      isAuthenticated: false
    }
  },
  mutations: {
    // get info about the user from the browser to set the app
    initializeStore(state){
      if(localStorage.getItem('token')) {
        state.user.token = localStorage.getItem('token')
        state.user.isAuthenticated = true
      } else {
        state.user.token = ''
        state.user.isAuthenticated = false
      }
    },
    // set token at login
    setToken(state, token){
      state.user.token = token
      state.user.isAuthenticated = true
    },
    // remove token at logout
    setToken(state){
      state.user.token = ''
      state.user.isAuthenticated = false
    }
  },
  actions: {
  },
  modules: {
  }
})
