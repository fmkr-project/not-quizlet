/* eslint-disable */
import axios from 'axios';
import store from '@/store/store'; // Import Vuex store

const API_URL = process.env.VUE_APP_API_URL+"users/";

class AuthService {
  constructor() {
    // Store instance is available throughout the class
  }

  async register(user) {
    try {
      const response = await axios.post(API_URL + 'register', {
        username: user.username,
        email: user.email,
        password: user.password
      }, { withCredentials: true });

      return { success: true, message: response.data.message };
    } catch (error) {
      let message = 'Registration failed';
      if (error.response) {
        switch (error.response.status) {
          case 400:
            message = 'Please fill in all the fields.';
            break;
          case 409:
            message = 'Username or Email already registered.';
            break;
          case 500:
          default:
            message = 'An error occurred during registration.';
            break;
        }
      }
      return { success: false, message };
    }
  }

  async login(user, rememberMe) {
    try {
      const response = await axios.post(API_URL + 'login', {
        email: user.email,
        password: user.password,
        rememberMe: rememberMe
      }, { withCredentials: true });
  
      if (response.data.success) {
        const userDetailsResponse = await this.getUserDetails(); // Use await here
        if (userDetailsResponse.success) {
          store.commit('SET_LOGGED_IN', true);
          store.commit('SET_USER_DETAILS', userDetailsResponse.userDetails);
          return { success: true, message: response.data.message };
        } else {
          return { success: false, message: userDetailsResponse.message };
        }
      } else {
        return { success: false, message: response.data.error || 'Login failed' };
      }
    } catch (error) {
      let message = 'The login has failed.';
      if (error.response) {
        switch (error.response.status) {
          case 400:
            message = 'Please fill in all the fields.';
            break;
          case 401:
            message = 'Invalid credentials or email not verified.';
            break;
          case 403:
            message = 'Account is locked due to suspicious activity.';
            break;
          case 429:
            message = 'Too many failed attempts. Try again later.';
            break;
          default:
            message = 'An error occurred during login.';
            break;
        }
      }
      return { success: false, message };
    }
  }

  async send_reset_password(user) {
    try {
      const response = await axios.post(API_URL + 'send_reset_password', {
        email: user.email,
        password: user.password
      }, { withCredentials: true });
      return { success: true };
    } catch (error) {
      let message = 'There was an error resetting your password.';
      if (error.response) {
        switch (error.response.status) {
          case 404:
            message = 'This mail is not registered.';
            break;
          default:
            message = 'An error occurred while attempting to reset the password.';
            break;
        }
      }
      return { success: false, message };
    }
  }

  async logout() {
    try {
      await axios.post(API_URL + 'logout', {}, { withCredentials: true });
      store.commit('LOGOUT');
      return { success: true };
    } catch (error) {
      return { success: false, message: 'Logout failed' };
    }
  }

  async checkLoginStatus() {
    try {
        const response = await axios.get(API_URL + 'check_auth', { withCredentials: true });
        const isLoggedIn = response.data.success;
        store.commit('SET_LOGGED_IN', isLoggedIn);
        return { success: isLoggedIn };
    } catch (error) {
        store.commit('SET_LOGGED_IN', false);
        return { success: false, message: 'Failed to check authentication' };
    }
  }
  async getUserDetails() {
    try {
        const response = await axios.get(API_URL + 'get_user_details', { withCredentials: true });
        return { success: true, userDetails: response.data.user };
    } catch (error) {
        return { success: false, message: error.response?.data?.error || 'Failed to fetch user details' };
    }
  }

  async modifyProfile(userData, newProfilePic) {
    try {
      let formData = new FormData();
      formData.append('username', userData.username);
      formData.append('password', userData.password);

      // Append file if provided
      if (newProfilePic) {
        formData.append('file', newProfilePic);
      }
      for (var pair of formData.entries()) {
        console.log(pair[0]+ ', ' + pair[1]); 
      }
      const response = await axios.post(API_URL + "modify_profile", formData, {
        withCredentials: true,
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      return { success: true, message: response.data.message };
    } catch (error) {
      console.log(error)
      // Detailed error handling based on the response status code
      let message = 'Error updating profile';
      if (error.response) {
        switch (error.response.status) {
          case 400:
            message = 'Invalid request. Please check your input.';
            break;
          case 401:
            message = 'Unauthorized. You might need to log in again.';
            break;
          case 403:
            message = 'Forbidden. You cannot modify this profile.';
            break;
          case 409:
            message = 'Username already taken. Please choose another one.';
            break;
          case 500:
            message = 'Internal Server Error. Please try again later.';
            break;
          default:
            message = error.response.data.error || 'An unexpected error occurred.';
            break;
        }
      }
      return { success: false, message };
    }
  }
}

export default AuthService;
