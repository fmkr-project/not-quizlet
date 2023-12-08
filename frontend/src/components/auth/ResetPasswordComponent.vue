<template>
  <div>
    <!-- Trigger button -->
    <button @click="showModal = true" class="btn-forgot-password">Forgot my password</button>

    <!-- Modal -->
    <transition name="modal">
      <div class="modal-mask" v-if="showModal">
        <div class="modal-wrapper">
          <div class="modal-container">
            
            <!-- Modal header -->
            <div class="modal-header">
              <h1>Reset your password</h1>
            </div>
            
            <!-- Form -->
            <form @submit.prevent="submitReset">
              <!-- Modal body -->
              <div class="modal-body">
                <p>If you have forgotten your password you can reset it here.</p>
                <div class="form-group">
                  <label for="reset-email">Email</label>
                  <input class="form-control" id="reset-email" placeholder="E-mail Address" v-model="resetEmail" type="email">
                </div>
                
                <div class="form-group">
                  <label for="new-password">New Password</label>
                  <input class="form-control" id="new-password" placeholder="Your New Password" v-model="resetNewPassword" type="password">
                </div>
                
                <div class="form-group">
                  <label for="verify-password">Verify New Password</label>
                  <input class="form-control" id="verify-password" placeholder="Verify New Password" v-model="resetVerifyPassword" type="password">
                </div>
              </div>

            <!-- Modal footer -->
            <div class="modal-footer">
                <!-- Grid row for error message -->
                <div class="row w-100">
                    <div class="col-12 col-md-8 mx-auto">
                        <div v-if="errorPopup" class="alert alert-danger text-center">{{ errorPopup }}</div>
                    </div>
                </div>

                <!-- Grid row for buttons -->
                <div class="row w-100">
                    <div class="col-12 d-flex justify-content-center">
                        <button type="submit" class="btn btn-primary">Send a password reset link.</button>
                        <button type="button" class="btn btn-secondary" @click="resetErrorPopUp">Cancel</button>
                    </div>
                </div>
            </div>
            </form>

            <!-- Error Message -->


          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showModal: false,
      resetEmail: '',
      resetNewPassword: '',
      resetVerifyPassword: '',
      errorPopup: ''
    };
  },
  methods: {
    resetErrorPopUp(){
        this.errorPopup = '';
        this.showModal = false;
        this.resetEmail = '';
        this.resetNewPassword = '';
        this.resetVerifyPassword = '';
    },
    submitReset() {
      // Validate the input fields
      if (!this.resetEmail || !this.resetNewPassword || !this.resetVerifyPassword) {
        this.errorPopup = 'All fields are required.';
        return;
      }
      if (this.resetNewPassword !== this.resetVerifyPassword) {
        this.errorPopup = 'Passwords do not match.';
        return;
      }
      // TODO: Implement the reset password logic
      this.errorPopup = ''; // Clear error message
      this.showModal = false; // Close the modal on successful submission
      // Reset form
      this.resetEmail = '';
      this.resetNewPassword = '';
      this.resetVerifyPassword = '';
    }
  }
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-wrapper {
  padding: 20px;
}

.modal-container {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
}

.modal-header h1 {
  margin-top: 0;
}

.modal-body {
  margin: 20px 0;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
}

.btn-forgot-password {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  text-decoration: underline;
}

.btn-primary {
  margin-right: 10px;
}

/* Add animation for the modal */
.modal-enter-active, .modal-leave-active {
  transition: opacity 0.5s;
}
.modal-enter, .modal-leave-to {
  opacity: 0;
}
</style>