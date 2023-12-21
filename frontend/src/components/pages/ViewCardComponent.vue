<template>
    <div class="view-container">
        <div class="create-card-button-container">
            <button @click="createNewCard" class="create-card-button">Create New Card</button>
        </div>
      <div class="container">
        <div class="row" data-aos="zoom-in" v-if="userCards">
          <div class="col-md-4" v-for="(card, index) in userCards" :key="card.id">
            <div class="flashcard" @click="toggleFlip(index)">
              <div class="flashcard-content" :class="{ flipped: card.flipped }">
                <div class="flashcard-front">
                  <h4 class="card-label">Question</h4>
                  <h3 :style="{ fontSize: calculateFontSize(card.front_side) }">{{ card.front_side }}</h3>
                  <button class="btn btn-light btn-large" @click.stop="toggleFlip(index)">FLIP</button>
                </div>
                <div class="flashcard-back">
                  <h4 class="card-label">Answer</h4>
                  <h3 :style="{ fontSize: calculateFontSize(card.back_side) }">{{ card.back_side }}</h3>
                  <button class="btn btn-light btn-large" @click.stop="toggleFlip(index)">FLIP</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else>
          <p>Loading cards...</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import cardService from '@/services/cardService'; // Hypothetical service for user-related operations
  
  export default {
    name: 'ViewCardComponent',
    data() {
      return {
        userCards: [],
        currentIndex: 0,
        flipped: false,
      };
    },
    created() {
      this.fetchUserCards();
    },
    methods: {
      async fetchUserCards() {
        try {
          const result = await cardService.fetchUserCards(); // Hypothetical method to fetch all user cards
          if (result.success) {
            this.userCards = result.cards;
          } else {
            console.error('Failed to fetch cards:', result.message);
          }
        } catch (error) {
          console.error('Error fetching cards:', error);
        }
      },
      toggleFlip(index) {
        this.userCards[index].flipped = !this.userCards[index].flipped;
      },
      createNewCard() {
        this.$router.push('/mycard/create');
      },
      calculateFontSize(text) {
      const baseSize = 18; // Base font size in pixels
      const maxSize = 30;  // Maximum font size
      const maxLength = 180; // Ideal max number of characters for base size

      if (!text) return `${baseSize}px`; // Early return for empty text

      let calculatedSize = baseSize * (maxLength / Math.max(text.length, maxLength));
      calculatedSize = Math.min(calculatedSize, maxSize);
      return `${calculatedSize}px`;
    },
    previousFlashcard() {
      // Implementation for navigating to the previous flashcard
      if (this.currentIndex > 0) this.currentIndex--;
    },
    nextFlashcard() {
      // Implementation for navigating to the next flashcard
      if (this.currentIndex < this.flashcards.length - 1) this.currentIndex++;
    }
    },
  };
  </script>
  
  <style scoped>
  @import "@/assets/css/flashcards.css";

  .create-card-button-container {
  text-align: center;
  margin-top: 20px;
}

.create-card-button {
  padding: 10px 20px;
  background-color: #4CAF50; /* Example button color */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.create-card-button:hover {
  background-color: #45a049;
}
  </style>
  