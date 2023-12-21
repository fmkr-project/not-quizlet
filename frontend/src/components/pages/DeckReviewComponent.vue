<template>
  <div class="review-container">
    <button @click="backToPublic" class="back-to-public">Back to Public Decks</button>
    <div v-if="flashcards && flashcards.length">
      <div class="flashcard" :class="{ 'is-active': currentIndex === index }" v-for="(card, index) in flashcards" :key="card.id">
        <div class="flashcard-content" :class="{ flipped: card.flipped }">
          <div class="flashcard-front" :style="{ backgroundColor: card.color }">
            <h3 :style="{ fontSize: calculateFontSize(card.front_side) }">{{ card.front_side }}</h3>
            <button class="btn btn-light btn-large" @click="toggleFlip(index)">FLIP</button>
          </div>
          <div class="flashcard-back" :style="{ backgroundColor: card.color }">
            <h3 :style="{ fontSize: calculateFontSize(card.back_side) }">{{ card.back_side }}</h3>
            <button class="btn btn-light btn-large" @click="toggleFlip(index)">FLIP</button>
          </div>
        </div>
      </div>
      <div class="navigation-buttons">
        <button @click="previousFlashcard" :disabled="currentIndex === 0">Previous</button>
        <button @click="nextFlashcard" :disabled="currentIndex === flashcards.length - 1">Next</button>
      </div>
    </div>
    <div v-else>
      <p>Loading flashcards...</p>
    </div>
  </div>
</template>

<script>
import DeckService from '@/services/deckService';

export default {
  name: 'DeckReviewComponent',
  data() {
    return {
      flashcards: [],
      currentIndex: 0,
      isFlipped: false,
    };
  },
  created() {
    this.fetchFlashcards();
  },
  methods: {
    async fetchFlashcards() {
      const deckId = this.$route.params.id;
      try {
        const result = await DeckService.getFlashcardsByDeckId(deckId);
        if (result.success) {
          this.flashcards = result.flashcards;
        } else {
          console.error('Failed to fetch flashcards:', result.message);
        }
      } catch (error) {
        console.error('Error fetching flashcards:', error);
      }
    },
    toggleFlip(index) {
      this.flashcards[index].flipped = !this.flashcards[index].flipped;
    },
    previousFlashcard() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
        this.isFlipped = false;
      }
    },
    nextFlashcard() {
      if (this.currentIndex < this.flashcards.length - 1) {
        this.currentIndex++;
        this.isFlipped = false;
      }
    },
    backToPublic() {
      this.$router.push('/deckhub');
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
  },
};
</script>
  
<style scoped>
.flashcard-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.flashcard {
  width: 300px;
  height: 400px;
  margin: 20px;
  perspective: 1000px;
  border-radius: 5px;
  cursor: pointer;
}

.flashcard-content {
  width: 100%;
  height: 100%;
  position: relative;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flashcard-front, .flashcard-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  border-radius: 5px;
  color: white; /* Default text color for all cards */
}

.flashcard-back {
  transform: rotateY(180deg);
  /* Add specific styling for the back side here if needed */
}

.btn-large {
  border: none;
  background-color: transparent;
  color: white;
  padding: 10px 20px;
  text-transform: uppercase;
  font-weight: bold;
  transition: background-color 0.3s ease;
  cursor: pointer;
  margin-top: 1rem;
}

.btn-large:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.flashcard-content.flipped {
  transform: rotateY(180deg);
}

.card-label {
  font-weight: bold;
  margin-bottom: 1rem; /* Spacing between label and question/answer */
  color: #fff; /* Adjust color as needed */
}

.flashcard h3 {
  margin-bottom: 1.5rem; /* Increased spacing to accommodate label */
  text-align: center;
  word-wrap: break-word;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: relative;
}

.navigation-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Additional styles for responsive layout */
@media (max-width: 768px) {
  .flashcard-container {
    flex-direction: column;
  }

  .flashcard {
    width: 90%;
    height: auto;
    margin: 10px auto;
  }
}

/* Style for the back to public button */
.back-to-public {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  background-color: #f5f5f5;
  color: #333;
  text-align: center;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.back-to-public:hover {
  background-color: #e1e1e1;
}

/* Ensure the text on the card is readable */
.flashcard-front, .flashcard-back {
  color: black; /* Changed from white for readability */
  background: #23ED60; /* Light cream background */
  border: 1px solid #ddd; /* Add border to flashcards */
}

/* Corrected class name for 'light-cream-background' */
.light-cream-background {
  background-color: #fbf8e7;
}


</style>
  