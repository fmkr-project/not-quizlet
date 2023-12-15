import { createStore } from 'vuex';
import axios from 'axios';
const API_URL = process.env.VUE_APP_API_URL + "api/users/"
export default createStore({
    state: {
      isLoggedIn: false,
    },
    mutations: {
      SET_LOGGED_IN(state, status) {
        state.isLoggedIn = status;
      },
    },
    actions: {
      async checkLoginStatus({ commit }) {
        try {
          const response = await axios.get(API_URL+'check_auth', { withCredentials: true });
          commit('SET_LOGGED_IN', response.data.isLoggedIn);
        } catch (error) {
          commit('SET_LOGGED_IN', false);
        }
      }
    }
  });
