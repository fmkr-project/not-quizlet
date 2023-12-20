<template>
    <div class="profile-container">
      <div class="profile-picture">
        <!-- Display current profile picture -->
        <img :src="userDetails.pfp_image_location" alt="Profile Picture">
        <label for="profile-upload">Change Profile Picture:</label>
        <input type="file" id="profile-upload" @change="onFileChange">
        <!-- Add an image preview here for the selected picture -->
        <img :src="selectedImage" alt="Selected Image Preview">
      </div>
      <div class="change-password">
        <button @click="onChangePasswordClick">Change Password</button>
      </div>
      <div class="change-username">
        <label for="username">New Username:</label>
        <input type="text" id="username" v-model="newUsername">
        <button @click="onChangeUsernameClick">Change Username</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ProfileComponent',
    data() {
      return {
        selectedImage: null, // To hold the selected image preview
        newUsername: '', // To hold the new username
      };
    },
    methods: {
      onFileChange(event) {
        // Handle file upload and update selectedImage with a preview
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.readAsDataURL(file);
          reader.onload = () => {
            this.selectedImage = reader.result;
          };
        }
      },
      onChangePasswordClick() {
        // Handle password change
      },
      onChangeUsernameClick() {
        // Handle username change
      },
    },
    computed: {
      userDetails() {
        return this.$store.state.userDetails;
      },
    },
  };
  </script>

<style scoped>
.profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.profile-picture input {
  margin-top: 10px;
}

.change-password, .change-username {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.change-username input {
  margin-bottom: 10px;
}
</style>
