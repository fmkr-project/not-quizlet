<template>
  <section class="login-content">
    <div class="row m-0 align-items-center bg-white vh-100">
      <div class="col-md-6 d-md-block d-none bg-primary p-0 vh-100 overflow-hidden">
        <img src="@/assets/images/auth/05.png" class="img-fluid gradient-main animated-scaleX" alt="images" loading="lazy" />
      </div>
      <div class="col-md-6">
        <div class="row justify-content-center">
          <div class="col-md-10">
            <div class="card card-transparent auth-card shadow-none d-flex justify-content-center mb-0">
              <div class="card-body">
                <router-link :to="{ name: 'default.dashboard' }" class="navbar-brand d-flex align-items-center mb-3 text-primary">
                  <!-- The brand-logo and brand-name components should be defined in your project -->
                  <brand-logo></brand-logo>
                  <h4 class="logo-title ms-3 mb-0"><brand-name></brand-name></h4>
                </router-link>
                <h2 class="mb-2 text-center">Sign Up</h2>
                <p class="text-center">Create your <brand-name></brand-name> account.</p>
                <form @submit.prevent="handleRegistration">
                  <div class="row">
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label for="first-name" class="form-label">First Name</label>
                        <input type="text" class="form-control" id="first-name" v-model="firstName" placeholder=" " />
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label for="last-name" class="form-label">Last Name</label>
                        <input type="text" class="form-control" id="last-name" v-model="lastName" placeholder=" " />
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label for="email" class="form-label">Email</label>
                        <input type="email" class="form-control" id="email" v-model="email" placeholder=" " />
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label for="phone" class="form-label">Phone No.</label>
                        <input type="text" class="form-control" id="phone" v-model="phone" placeholder=" " />
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" class="form-control" id="password" v-model="password" placeholder=" " />
                      </div>
                    </div>
                    <div class="col-lg-6">
                      <div class="form-group">
                        <label for="confirm-password" class="form-label">Confirm Password</label>
                        <input type="password" class="form-control" id="confirm-password" v-model="confirmPassword" placeholder=" " />
                      </div>
                    </div>
                    <div class="col-lg-12 d-flex justify-content-center">
                      <div class="form-check mb-3">
                        <input type="checkbox" class="form-check-input" id="customCheck1" v-model="termsAgreed" />
                        <label class="form-check-label" for="customCheck1">I agree with the terms of use</label>
                      </div>
                    </div>
                  </div>
                  <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-primary">Sign Up</button>
                  </div>
                  <p class="mt-3 text-center">
                    Already have an Account? <router-link to="/auth/login" class="text-underline">Sign In</router-link>
                  </p>
                </form>
              </div>
            </div>
          </div>
        </div>
        <!-- The sign-bg-right component should be defined in your project -->
        <div class="sign-bg sign-bg-right">
          <!-- Background SVG omitted for brevity -->
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const firstName = ref('');
const lastName = ref('');
const email = ref('');
const phone = ref('');
const password = ref('');
const confirmPassword = ref('');
const termsAgreed = ref(false);
const $router = useRouter();

  const handleRegistration = async () => {
    if (password.value !== confirmPassword.value) {
      alert("Passwords do not match.");
      return;
    }
    
    if (!termsAgreed.value) {
      alert("You must agree to the terms of use.");
      return;
    }
    
    const username = `${firstName.value} ${lastName.value}`;

    const userData = {
      "username" : username,
      "email" : email.value,
      "password": password.value,
    };

    try {
      const response = await axios.post('http://127.0.0.1:5001/api/users/register', userData);
      console.log('Registration successful:', response.data.message);
      $router.push('/auth/login');
    } catch (error) {
      console.error('Registration error:', error);
      alert("Registration failed: " + error.message);
    }
  };
</script>

<style lang="scss" scoped></style>
