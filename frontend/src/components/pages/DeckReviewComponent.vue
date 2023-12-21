<template>
  <div class="review-container">
    <button @click="backToPublic" class="back-to-public">Back to Public Decks</button>
    <div class="container">
      <div class="row" data-aos="zoom-in" v-if="flashcards">
        <div class="col-md-4" v-for="(card, index) in flashcards" :key="card.id">
          <div class="flashcard" @click="toggleFlip(index)">
            <div class="flashcard-content" :class="{ flipped: card.flipped }">
              <div class="flashcard-front" :style="{ backgroundColor: card.color }">
                <h4 class="card-label">Question</h4>
                <h3 :style="{ fontSize: calculateFontSize(card.front_side) }">{{ card.front_side }}</h3>
                <button class="btn btn-light btn-large" @click.stop="toggleFlip(index)">FLIP</button>
              </div>
              <div class="flashcard-back" :style="{ backgroundColor: card.color }">
                <h4 class="card-label">Answer</h4>
                <h3 :style="{ fontSize: calculateFontSize(card.back_side) }">{{ card.back_side }}</h3>
                <button class="btn btn-light btn-large" @click.stop="toggleFlip(index)">FLIP</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <p>Loading flashcards...</p>
      </div>
    </div>
  </div>
</template>

<script>
import DeckService from '@/services/deckService';
import assignColors from '@/assets/js/color-picker.js';
export default {
  name: 'DeckReviewComponent',
  data() {
    return {
      flashcards: [],
      currentIndex: 0,
      flipped: false,
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
          this.flashcards = assignColors(result.flashcards);
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
@import "@/assets/css/deck-review.css";
@import "@/assets/css/flashcards.css";
</style>
  