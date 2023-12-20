<template>
  <div class="login-container" id="your-element-selector">
    <div class="login-form" >
        <section class="login-content">

            <div class="row">
                <div class="col" style="text-align: center;"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" class="bi bi-person-fill text-primary" style="text-align: center;width: 70px;height: 70px;">
                        <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3Zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"></path>
                    </svg></div>
            </div>
            <p class="text-center mb-4">Login to your PIMA account.</p>
            <form @submit.prevent="submitLogin">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="form-group mb-3"><label class="form-label form-label" for="email">Email</label><input type="email" class="form-control" id="email" v-model="email" aria-describedby="email" placeholder=" "></div>
                    </div>
                    <div class="col-lg-12">
                        <div class="form-group mb-4"><label class="form-label form-label" for="password">Password</label><input type="password" class="form-control" id="password" v-model="password" aria-describedby="password" placeholder=""></div>
                    </div>
                    <div class="col-lg-12 d-flex justify-content-between align-items-center mb-4">
                      <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="customCheck1" v-model="rememberMe">
                        <label class="form-label form-check-label" for="customCheck1">Remember Me</label>
                      </div>

                    </div>
                </div>
                <div class="d-flex justify-content-center"><button class="btn btn-primary" type="submit">Sign In</button></div>
                <p class="text-center text-danger mt-3">{{ errorMessage }}</p>
                <p class="text-center mt-3">Don’t have an account? <a href="/register" class="text-underline">Click here to sign up.</a></p>
            </form>
            <div class="reset-password-link d-flex justify-content-center">
              <ResetPasswordComponent/>
            </div>
        </section>
    </div>
  </div>
</template>
<script>
/* global VANTA */
import ResetPasswordComponent from '@/components/auth/ResetPasswordComponent';
import AuthService from '@/services/authService'; // Ensure correct path
export default {
  name : 'LoginComponent',
  components : {
    ResetPasswordComponent
  },
  data() {
    return {
      email: '',
      password: '',
      rememberMe: false,
      hasError: false,
      errorMessage: '',
    };
  },
  methods: {
    async submitLogin() {
      try {
        const authservice = new AuthService();
        const response = await authservice.login({
          email: this.email,
          password: this.password,
        }, this.rememberMe);

        if (response.success) {
          console.log(response)
          this.$store.commit('SET_LOGGED_IN', true);
          this.$router.push('/home'); // Adjust this if needed
        } else {
          this.hasError = true;
          this.errorMessage = response.message; // Use message from AuthService
        }
      } catch (error) {
        this.hasError = true;
        this.errorMessage = error.message || 'An error occurred during login.';
      }
    },
  },
  mounted() {
    this.vantaEffect = VANTA.WAVES({
  el: "#your-element-selector",
  mouseControls: true,
  touchControls: true,
  gyroControls: false,
  minHeight: 200.00,
  minWidth: 200.00,
  scale: 1.00,
  scaleMobile: 1.00,
})
  },
  beforeUnmount() { // or beforeDestroy() in Vue 2
    if (this.vantaEffect) {
      this.vantaEffect.destroy();
    }
  }
};
</script>
<style scoped>
.container {
  max-width: 400px;
  margin: auto;
  padding: 0 15px;
}
/* Add this new style for the reset password link */
.reset-password-link a {
  text-decoration: underline; /* Underline the link */
  cursor: pointer; /* Change cursor to pointer when hovering over the link */
}

/* Adjust this style to only apply to the Remember Me label */
.form-check-label {
  cursor: pointer; /* Change cursor to pointer when hovering over the label */
  margin-bottom: 0; /* Keep the label aligned with the checkbox */
}

/* The outer container */
.login-container {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    min-height: 70vh; /* Full height of the viewport */
}

/* The login form */
.login-form {
    width: 500px; /* Fixed width */
    height: 600px; /* Fixed height */
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Optional: adds shadow for better appearance */
    border-radius: 10px; /* Optional: rounds the corners */
    background-color: white; /* Optional: background color */
    border-radius: 40px;
}

</style>