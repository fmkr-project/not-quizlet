<script>
import AuthService from '@/services/authService'; // Ensure correct path

export default {
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
        const response = await AuthService.login({
          email: this.email,
          password: this.password,
        }, this.rememberMe);

        if (response.success) {
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
};
</script>

<template>
  <section class="login-content">
    <b-row class="m-0 align-items-center bg-white h-100">
      <b-col md="6">
        <b-row class="justify-content-center">
          <b-col md="10">
            <b-card class="card-transparent shadow-none d-flex justify-content-center mb-0 auth-card iq-auth-form">
              <h2 class="mb-2 text-center">Sign In</h2>
              <p class="text-center">Login to stay connected.</p>
              <form @submit.prevent="toHomeDashboard">
                <div class="row">
                  <div class="col-lg-12">
                    <div class="form-group">
                      <label for="email" class="form-label">Email</label>
                      <input type="email" class="form-control" id="email" v-model="email" aria-describedby="email" placeholder=" " />
                    </div>
                  </div>
                  <div class="col-lg-12">
                    <div class="form-group">
                      <label for="password" class="form-label">Password</label>
                      <input type="password" class="form-control" id="password" v-model="password" aria-describedby="password" placeholder=" " />
                    </div>
                  </div>
                  <div class="col-lg-12 d-flex justify-content-between">
                    <div class="form-check mb-3">
                      <input type="checkbox" class="form-check-input" id="customCheck1" v-model="rememberMe" />
                      <label class="form-check-label" for="customCheck1">Remember Me</label>
                    </div>
                    <a href="/auth/reset-password">Forgot Password?</a>
                  </div>
                </div>
                <div class="d-flex justify-content-center">
                  <button type="submit" class="btn btn-primary">Sign In</button>
                </div>
                <p v-if="hasError" class="text-danger text-center">Invalid credentials. Please try again.</p>
                <p class="mt-3 text-center">Don’t have an account? <a href="/auth/register" class="text-underline">Click here to sign up.</a></p>
              </form>
            </b-card>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </section>
</template>
  