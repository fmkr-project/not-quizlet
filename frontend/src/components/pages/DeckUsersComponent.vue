<template>
  <body>
  <section class="decks-section">
    <div class="deck-controls" style="text-align: center;" >
              <button @click="showAddDeckPopup = true">Add Deck</button>
              <button :class="{active: removeActive}" @click="toggleRemove">Remove Deck</button>
              <button @click="showModifyDeckPopup = true" :disabled="!selectedDeckId">Modify Deck</button>
          </div>
      <div class="container py-5">
      <h1 style="text-align: center; margin-bottom: 46px;">Your Decks</h1>
      <div class="deck-grid">
              <div
              class="deck-card"
              v-for="deck in userDecks"
              :key="deck.id"
              @click="selectDeck(deck.id)"
              :class="{ 'selected': deck.id === selectedDeckId && removeActive }"
              >
              <div class="deck-card-body">
                  <h5 class="deck-title">{{ deck.name }}</h5>
                  <p class="deck-description">{{ deck.description }}</p>
              </div>
              </div>
          </div>
          <div v-if="showAddDeckPopup" class="popup-overlay" @click.self="showAddDeckPopup = false">
              <div class="popup">
                <form @submit.prevent="submitNewDeck">
            <div class="form-group">
              <label for="deck-name">Deck Name</label>
              <input type="text" class="form-control" id="deck-name" placeholder="Enter deck name" v-model="newDeck.name" required>
            </div>

            <div class="form-group">
              <label for="deck-description">Description</label>
              <textarea class="form-control" id="deck-description" rows="3" placeholder="Enter a brief description" v-model="newDeck.description"></textarea>
            </div>

            <div class="form-group form-check">
              <input type="checkbox" class="form-check-input" id="deck-public" v-model="newDeck.isPublic">
              <label class="form-check-label" for="deck-public">Public</label>
            </div>

            <div class="row w-100">
                  <div class="col-12 d-flex justify-content-center">
                      <button type="submit" class="btn btn-primary">Create a deck.</button>
                      <button type="button" class="btn btn-secondary" @click.self="showAddDeckPopup = false">Cancel</button>
                  </div>
              </div>
          </form>
              </div>
          </div>
          <div v-if="showModifyDeckPopup" class="popup-overlay" @click.self="showModifyDeckPopup = false">
              <div class="popup">
                  <h3>Modify Deck</h3>
                  <form @submit.prevent="submitDeckChanges">
          <input type="text" placeholder="Deck Name" v-model="selectedDeck.name" required>
          <textarea placeholder="Description" v-model="selectedDeck.description"></textarea>
          <label><input type="checkbox" v-model="selectedDeck.isPublic"> Public</label>
          <button type="submit">Update Deck</button>
      </form>

              </div>
          </div>
          <div v-if="showRemoveDeckConfirmation" class="popup-overlay" @click.self="showRemoveDeckConfirmation = false">
              <div class="popup">
                  <h3>Are you sure you want to delete this deck?</h3>
                  <button @click="removeDeck">Yes, Delete it</button>
                  <button @click="showRemoveDeckConfirmation = false">Cancel</button>
              </div>
          </div>
      </div>
  </section>
</body>    
</template>

<script>
import DeckService from '@/services/deckService';

export default {
  name: 'DeckUsersComponent',
  data() {
      return {
        userDecks: [],
        selectedDeckId: null,
        removeActive: false,
        modifyActive: false,
        showAddDeckPopup: false,
        showModifyDeckPopup: false,
        showRemoveDeckConfirmation: false,
        newDeck: {
              name: '',
              description: '',
              isPublic: true
          },
      };
  },
  created() {
      this.fetchUserDecks();
  },
  methods: {
      async fetchUserDecks() {
          const response = await DeckService.fetchUserDecks();
          if (response.success) {
              this.userDecks = response.decks.created;
          } else {
              console.error(response.message);
              // Handle error as needed
          }
      },
      navigateToDeckReview(deckId) {
          this.$router.push({ name: 'DeckReview', params: { id: deckId } });
      },
      selectDeck(deckId) {
          if(this.removeActive) {
              this.selectedDeckId = deckId;
              this.showRemoveDeckConfirmation = true;
          } else if (this.modifyActive){
            this.selectedDeckId = deckId;
            this.showModifyDeckPopup = true;
              
          }
          else{
            this.navigateToDeckReview(deckId);
          }
      },
      toggleRemove() {
          this.removeActive = !this.removeActive;
          // Deselect any selected deck when toggling off
          if (!this.removeActive) this.selectedDeckId = null;
      },
      async removeDeck() {
          // Call service to remove the selected deck
          if (this.selectedDeckId) {
              const response = await DeckService.removeDeck(this.selectedDeckId);
              if (response.success) {
                  // Remove deck from local array and reset state
                  this.userDecks = this.userDecks.filter(deck => deck.id !== this.selectedDeckId);
                  this.selectedDeckId = null;
                  this.showRemoveDeckConfirmation = false;
              } else {
                  console.error(response.message);
                  // Handle error as needed
              }
          }
      }
  }
};
</script>

<style scoped>
@import "@/assets/css/flashcards.css";
@import "@/assets/css/styles.css";
@import "@/assets/css/confirmation_popup.css";
.deck-grid {
display: grid;
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
gap: 20px;
}

.deck-card {
background: #f5f5f5;
border-radius: 8px;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
transition: transform 0.2s ease-in-out;
}

.deck-card:hover {
transform: translateY(-5px);
}

.deck-card-body {
padding: 15px;
text-align: center;
}

.deck-title {
font-size: 1.2em;
font-weight: bold;
}

.deck-description {
font-size: 0.9em;
}
</style>