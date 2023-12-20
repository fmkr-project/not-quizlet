<template>
    <div class="profile-container">
      <form @submit.prevent="onSubmit">
        <div class="profile-header">
          <!-- Display current profile picture and username -->
          <div class="profile-picture">
            <img :src="userDetails.pfp_image_location" alt="Profile Picture" class="rounded-image">
          </div>
          <div class="profile-username">
            <h2>{{ userDetails.username }}</h2>
          </div>
        </div>
  
        <div class="form-group">
          <label for="profile-upload" class="upload-label">Change Profile Picture:</label>
          <input type="file" id="profile-upload" @change="onFileChange" class="file-input">
          <!-- Image preview -->
          <div v-if="selectedImage" class="image-preview">
            <img :src="selectedImage" alt="Selected Image Preview" class="rounded-image">
          </div>
        </div>
  
        <div class="form-group">
          <label for="username">New Username:</label>
          <input type="text" id="username" v-model="newUsername" class="form-input">
        </div>
  
        <div class="form-group">
          <label for="password">New Password:</label>
          <input type="password" id="password" v-model="newPassword" class="form-input">
        </div>
  
        <div class="form-group">
          <label for="verify-password">Verify New Password:</label>
          <input type="password" id="verify-password" v-model="verifyPassword" class="form-input">
        </div>
  
        <button type="submit" class="submit-button">Update Profile</button>
      </form>
    </div>
  </template>
  
  
<script>
export default {
    name: 'ProfileComponent',
    data() {
        return {
        selectedImage: null, // To hold the selected image preview
        newUsername: '', // To hold the new username
        newPassword: '', // To hold the new password
        verifyPassword: '',
        };
    },
    methods: {
        onFileChange(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onload = () => {
            this.selectedImage = reader.result;
            };
        }
        },
        onSubmit() {
        // Handle form submission including all updates
        // TODO: Implement API calls or Vuex actions to update the user details
        }
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
  margin: 20px auto;
  max-width: 500px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.profile-picture {
  margin-right: 20px;
}

.rounded-image {
  width: 100%;
  max-width: 200px;
  height: auto;
  border-radius: 50%;
  object-fit: cover;
}

.upload-label,
.form-group label {
  display: block;
  margin-top: 20px;
}

.file-input {
  margin-top: 10px;
}

.form-input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.submit-button {
  display: block;
  width: 100%;
  padding: 10px;
  margin-top: 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}

.image-preview {
  margin-top: 10px;
}
</style>

