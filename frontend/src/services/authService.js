import axios from 'axios';
/* eslint-disable */
const apiUrl = process.env.VUE_APP_API_URL;
const apiPort = process.env.VUE_APP_API_PORT;
const apiUsers = process.env.VUE_APP_API_USERS_ROUTE;
const API_URL = apiUrl.concat(apiPort).concat(apiUsers);

class AuthService {
    async register(user) {
        try {
            const response = await axios.post(API_URL + 'register', {
                username: user.username,
                email: user.email,
                password: user.password
            });
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
            });
            if (rememberMe) {
                const oneYearFromNow = new Date();
                oneYearFromNow.setFullYear(oneYearFromNow.getFullYear() + 1);
                document.cookie = `token=${response.data.token}; expires=${oneYearFromNow.toUTCString()}; path=/; Secure; HttpOnly`;
            } else {
                document.cookie = `token=${response.data.token}; path=/; Secure; HttpOnly`;
            }

            return { success: true, token: response.data.token };
        } catch (error) {
            let message = 'Login failed';
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
}

export default AuthService;