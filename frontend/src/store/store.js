import { createStore } from 'vuex';
import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL + "api/users/";

function initialState() {
  return {
    isLoggedIn: false,
    userDetails: null  
  };
}

export default createStore({
  state: initialState(),
  mutations: {
    SET_LOGGED_IN(state, status) {
        state.isLoggedIn = status;
        localStorage.setItem('isLoggedIn', status);
    },
    SET_USER_DETAILS(state, userDetails) {
        state.userDetails = userDetails;
        localStorage.setItem('userDetails', JSON.stringify(userDetails));
    },
    LOGOUT(state) {
      Object.assign(state, initialState());
      localStorage.removeItem('isLoggedIn');
      localStorage.removeItem('userDetails');
  },
    INITIALIZE_STORE(state) {
        if (localStorage.getItem('isLoggedIn')) {
            state.isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
        }
        if (localStorage.getItem('userDetails')) {
            state.userDetails = JSON.parse(localStorage.getItem('userDetails'));
        }
    }
  },
  actions: {
    async checkLoginStatus({ commit }) {
        try {
            const response = await axios.get(API_URL + 'check_auth', { withCredentials: true });
            commit('SET_LOGGED_IN', response.data.success);
            if (response.data.success) {
                // Fetch user details if logged in
                const userDetailsResponse = await axios.get(API_URL + 'get_user_details', { withCredentials: true });
                if (userDetailsResponse.data) {
                    commit('SET_USER_DETAILS', userDetailsResponse.data.user);
                }
            }
        } catch (error) {
            commit('SET_LOGGED_IN', false);
            commit('SET_USER_DETAILS', null); // Clear user details if not logged in
        }
    }
}
});
