<template>
    <nav class="navbar navbar-expand-md sticky-top navbar-shrink py-3 navbar-light" data-aos="fade-down" id="mainNav" style="background-color: #FCF7FD">
      <div class="container">
        <a class="navbar-brand d-flex align-items-center" href="/">
          <span class="bs-icon-sm bs-icon-circle bs-icon-primary shadow d-flex justify-content-center align-items-center me-2 bs-icon" style="width: 100px;height: 100px;">
            <img width="48" height="41" src="https://elasticbeanstalk-eu-west-3-625039870308.s3.eu-west-3.amazonaws.com/img/logo-nobg.png" style="text-align: center;height: 73px;width: 73px;margin: 0px;padding: 0px;margin-top: -6px;margin-right: -1px;">
          </span>
        </a>
        <button data-bs-toggle="collapse" class="navbar-toggler" data-bs-target="#navcol-1">
          <span class="visually-hidden">Toggle navigation</span>
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navcol-1">
          <div class="col-xxl-1">
            <h1 class="fw-bold" style="font-size: 31px;">Polyvalent Interactive <br>Mastery App </h1>
          </div>
          <ul class="navbar-nav mx-auto">
      <li class="nav-item">
        <router-link to="/home" class="nav-link active">Home</router-link>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/deckhub">Deck Hub</a>
      </li>

      <!-- Conditional links that appear only when the user is logged in -->
      <li class="nav-item" v-if="isLoggedIn">
        <router-link to="/my-decks" class="nav-link">My Decks</router-link>
      </li>
      <li class="nav-item" v-if="isLoggedIn">
        <router-link to="/mycard/view" class="nav-link">My Cards</router-link>
      </li>
      <li class="nav-item" v-if="isLoggedIn">
        <router-link to="/my-profile" class="nav-link">My Profile</router-link>
      </li>
    </ul>
          <div v-if="isLoggedIn">
            <ul class="navbar-nav">
    <li class="nav-item">
      <div class="nav-item dropdown d-lg-flex">
    <a class="active d-lg-flex align-items-lg-center" aria-expanded="false" data-bs-toggle="dropdown" href="#">
      <span class="d-lg-flex" style="font-size: 20px;">
        <strong>
          <!-- Bind username here -->
          <span style="color: rgb(0, 0, 0); margin-right: 16px">{{ userDetails?.username || 'User' }}</span>
        </strong>
      </span>
      <!-- Bind profile picture here -->
      <img
        v-if="userDetails?.pfp_image_location"
        :src="userDetails.pfp_image_location"
        class="border rounded-circle"
        style="width: 80px; height: 80px; background: var(--bs-blue);"
      />
      <!-- Fallback image if no profile picture -->
      <img
        v-else
        src="logo-nobg.png"
        class="border rounded-circle"
        style="width: 80px; height: 80px; background: var(--bs-blue);"
      />
    </a>
          <div class="dropdown-menu">
              <a class="dropdown-item" href="#" style="width: 121.808px;">
                <router-link to="/profile">
                <svg class="bi bi-person-fill" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16" style="font-size: 17px;width: 25.9922px;height: 25.9922px;">
                  <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3Zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"></path>
                </svg>Profile </router-link></a>
              <a class="dropdown-item" href="#" @click.prevent="logout">
                <svg class="icon icon-tabler icon-tabler-logout" xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="width: 25.997px;height: 25.997px;">
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M14 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2"></path>
                  <path d="M7 12h14l-3 -3m0 6l3 -3"></path>
                </svg>Log out </a>
            </div>
          </div>
    </li>
</ul>
          </div>
          <div v-else>
            <a href="/register" style="padding: 0px;margin: 10px;text-decoration: underline;margin-right: 16px;">Register</a>
            <router-link to="/login" class="btn btn-primary shadow" role="button">Sign in</router-link>
          </div>
        </div>
      </div>
    </nav>
</template>
<script>
import AuthService from '@/services/authService'; // Import AuthService
export default {
  name: 'HeaderComponent',
  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
    },
    userDetails() {
      return this.$store.state.userDetails;
    }
  },
  methods: {
    async logout() {
      const authservice = new AuthService();
      await authservice.logout();
      this.$router.push('/home');
    }
  }
};
</script>
<style></style>