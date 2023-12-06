<template>
  <section class="login-content">
    <div class="row m-0 align-items-center bg-white vh-100">
      <div class="col-md-6 d-md-block d-none bg-primary p-0 vh-100 overflow-hidden">
        <img src="@/assets/images/auth/02.png" class="img-fluid gradient-main animated-scaleX" alt="images" loading="lazy" />
      </div>
      <div class="col-md-6 p-0">
        <div class="card card-transparent auth-card shadow-none d-flex justify-content-center mb-0">
          <div class="card-body">
            <router-link :to="{ name: 'default.dashboard' }" class="navbar-brand d-flex align-items-center mb-3 text-primary">
              <brand-logo></brand-logo>
              <h4 class="logo-title ms-3 mb-0"><brand-name></brand-name></h4>
            </router-link>
            <h2 class="mb-2">Reset Password</h2>
            <p>Enter your email address and we'll send you an email with instructions to reset your password.</p>
            <form @submit.prevent="resetPassword">
              <div class="row">
                <div class="col-lg-12">
                  <div class="floating-label form-group">
                    <label for="email" class="form-label">Email</label>
                    <input type="email" class="form-control" id="email" v-model="email" aria-describedby="email" placeholder=" " />
                  </div>
                </div>
              </div>
              <button type="submit" class="btn btn-primary">Reset</button>
            </form>
            <p v-if="errorMessage" class="text-danger">{{ errorMessage }}</p>
            <p v-if="successMessage" class="text-success">{{ successMessage }}</p>
          </div>
        </div>
        <div class="sign-bg sign-bg-right">
          <!-- SVG Background -->
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const email = ref('');
const errorMessage = ref('');
const successMessage = ref('');

const resetPassword = async () => {
  errorMessage.value = '';
  successMessage.value = '';

  if (!email.value) {
    errorMessage.value = 'Please enter your email address.';
    return;
  }
  
  try {
    const response = await axios.post('http://127.0.0.1:5001/api/users/reset-password', {
      email: email.value
    });
    
    // Check if the backend response indicates that the email exists and the reset link was sent
    if (response.data.message) {
      successMessage.value = response.data.message;
      // Optionally navigate to another page or show a success message
    } else {
      // Handle any other response
      errorMessage.value = 'Unexpected response from the server.';
    }
  } catch (error) {
    if (error.response && error.response.status === 404) {
      // Handle 404 Not Found
      errorMessage.value = 'Email address not found.';
    } else {
      // Handle other errors
      errorMessage.value = 'An error occurred while trying to reset the password.';
    }
  }
};
</script>

<style lang="scss" scoped></style>
