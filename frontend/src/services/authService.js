import axios from 'axios';
/* eslint-disable */

const API_URL = "http://127.0.0.1:5010/api/users/"

class AuthService {
    async register(user) {
        try {
            const response = await axios.post(API_URL + 'register', {
                username: user.username,
                email: user.email,
                password: user.password
            }, {withCredentials: true} );
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
                password: user.password
            }, {withCredentials: true});
            if (rememberMe) {
                const oneYearFromNow = new Date();
                oneYearFromNow.setFullYear(oneYearFromNow.getFullYear() + 1);
                document.cookie = `token=${response.data.token}; expires=${oneYearFromNow.toUTCString()}; path=/; HttpOnly`;
            } else {
                document.cookie = `token=${response.data.token}; path=/; HttpOnly`;
            }

            return { success: true, token: response.data.token };
        } catch (error) {
            let message = 'The login has failed, make sure your email is registered.';
            if (error.response) {
                switch (error.response.status) {
                    case 400:
                        message = 'Please fill in all the fields.';
                        break;
                    case 401:
                        message = error.response.data.error || 'Invalid credentials or email not verified.';
                        break;
                    case 403:
                        message = 'Account is locked due to suspicious activity.';
                        break;
                    case 429:
                        message = error.response.data.error || 'Too many failed attempts. Try again later.';
                        break;
                    default:
                        message = 'An error occurred during login.';
                        break;
                }
            }
            return { success: false, message };
        }
    }
    async send_reset_password(user){
        try{
            const response = await axios.post(API_URL + 'send_reset_password', {
                email: user.email,
                password: user.password
            }, {withCredentials: true});
            return {success: true};
        }
        catch (error){
            let message = 'There was an error resetting your password.';
            if (error.response) {
                switch (error.response.status) {
                    case 404:
                        message = 'This mail is not registered.';
                        break;
                }
            }
            return { success: false, message };
        }
        


    }
}

export default AuthService;