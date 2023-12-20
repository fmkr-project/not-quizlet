<template>
  <div class="register-container" id="your-element-selector">
    <div class="register-form">
      <section class="register-content">

        <div class="row">
          <div class="col" style="text-align: center;">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="1em"
              height="1em"
              fill="currentColor"
              viewBox="0 0 16 16"
              class="bi bi-person-fill text-primary"
              style="text-align: center; width: 70px; height: 70px;"
            >
              <path
                d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3Zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"
              ></path>
            </svg>
          </div>
        </div>
        <p class="text-center mb-4">Create your PIMA account.</p>
        <form @submit.prevent="submitRegistration">
          <div class="row">
            <div class="col-lg-12">
              <div class="form-group mb-3">
                <label class="form-label" for="username">Username</label>
                <input
                  type="text"
                  class="form-control"
                  id="username"
                  v-model="username"
                  aria-describedby="username"
                  placeholder=" "
                />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group mb-3">
                <label class="form-label" for="email">Email</label>
                <input
                  type="email"
                  class="form-control"
                  id="email"
                  v-model="email"
                  aria-describedby="email"
                  placeholder=" "
                />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group mb-3">
                <label class="form-label" for="password">Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="password"
                  v-model="password"
                  aria-describedby="password"
                  placeholder=""
                />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group mb-4">
                <label class="form-label" for="confirmPassword">Confirm Password</label>
                <input
                  type="password"
                  class="form-control"
                  id="confirmPassword"
                  v-model="confirmPassword"
                  aria-describedby="confirmPassword"
                  placeholder=""
                />
              </div>
            </div>
          </div>
          <div class="d-flex justify-content-center">
            <button class="btn btn-primary" type="submit">Sign Up</button>
          </div>
          <p class="text-center text-danger mt-3">{{ errorMessage }}</p>
          <p class="text-center mt-3">
            Already have an account? <router-link to="/login">Login here</router-link>.
          </p>
        </form>
      </section>
    </div>
  </div>
</template>

<script>
/* global VANTA */
import AuthService from "@/services/authService"; // Ensure correct path

export default {
  name: "RegisterComponent",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "", // Added confirmPassword field
      hasError: false,
      errorMessage: "",
    };
  },
  methods: {
    async submitRegistration() {
      try {
        if (this.password !== this.confirmPassword) {
          this.hasError = true;
          this.errorMessage = "Passwords do not match.";
          return;
        }

        const authService = new AuthService();
        const response = await authService.register({
          username: this.username,
          email: this.email,
          password: this.password,
        });

        if (response.success) {
          console.log(response);
          this.$router.push("/login"); // Redirect to login page after successful registration
        } else {
          this.hasError = true;
          this.errorMessage = response.message; // Use message from AuthService
        }
      } catch (error) {
        this.hasError = true;
        this.errorMessage =
          error.message || "An error occurred during registration.";
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
.register-container {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    min-height: 70vh; /* Minimum height to maintain vertical centering */
}

.register-form {
    width: 500px; /* Set the width of the register form */
    padding: 20px; /* Padding inside the form */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow for depth */
    border-radius: 40px; /* Rounded corners for the form */
    background-color: white; /* Background color of the form */
    display: flex; /* Using flex to control the inner layout */
    flex-direction: column; /* Stack form elements vertically */
    align-items: center; /* Center form elements horizontally */
    margin: auto; /* Auto margins for vertical centering within the container */
}

/* Adjust the margins of the first and last children inside the form if necessary */
.register-form > *:first-child {
    margin-top: 0; /* Removes extra space at the top of the first element */
}

.register-form > *:last-child {
    margin-bottom: 0; /* Removes extra space at the bottom of the last element */
}

/* Ensure the button and input fields do not exceed the form's width */
.register-form .form-control,
.register-form button {
    width: calc(100% - 40px); /* Adjusting for padding, assuming 20px on each side */
    max-width: 100%; /* Prevents the element from exceeding the form's width */
}

/* ... other styles ... */
</style>


