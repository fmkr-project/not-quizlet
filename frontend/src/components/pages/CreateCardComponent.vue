<template>
    <div class="create-card-container">
      <h2>Create New Card</h2>
      <form @submit.prevent="submitCard">
        <div class="form-group">
          <label for="front">Front</label>
          <textarea id="front" v-model="newCard.front" required></textarea>
        </div>
        <div class="form-group">
          <label for="back">Back</label>
          <textarea id="back" v-model="newCard.back" required></textarea>
        </div>
        <button type="submit" class="btn-submit">Create Card</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newCard: {
          front: '',
          back: '',
        },
      };
    },
    methods: {
      async submitCard() {
        try {
          // Replace with your actual service call to create a card
          const response = await this.createCard(this.newCard);
          if (response.success) {
            this.$router.push('/path-to-view-your-cards'); // Redirect after creation
            // Optionally reset the form or give user feedback
          } else {
            console.error('Failed to create card:', response.message);
            // Optionally handle errors, such as displaying a notification
          }
        } catch (error) {
          console.error('Error creating card:', error);
          // Optionally handle exceptions, such as network errors
        }
      },
      async createCard(cardData) {
        // This function should make an API call to your backend.
        // Placeholder for sending `cardData` to your backend.
        console.log('Card data to submit:', cardData);
        // Mock response
        return { success: true, message: 'Card created' };
      },
    },
  };
  </script>
  
  <style scoped>
  .create-card-container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    background: white;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
  }
  
  .form-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    min-height: 100px;
  }
  
  .btn-submit {
    background-color: #5cb85c;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
  }
  
  .btn-submit:hover {
    background-color: #4cae4c;
  }
  </style>
  