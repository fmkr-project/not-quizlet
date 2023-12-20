<template>
  <div class="profile-container">
    <div class="profile-picture">
      <label for="profile-upload">Upload Profile Picture:</label>
      <input type="file" id="profile-upload" @change="onFileChange">
    </div>
    <div class="change-password">
      <button @click="onChangePasswordClick">Change Password</button>
    </div>
    <div class="change-username">
      <label for="username">New Username:</label>
      <input type="text" id="username">
      <button @click="onChangeUsernameClick">Change Username</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  methods: {
    onFileChange() {
      // Handle file upload
    },
    onChangePasswordClick() {
      // Handle password change
    },
    onChangeUsernameClick() {
      // Handle username change
    }
  }
}
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
