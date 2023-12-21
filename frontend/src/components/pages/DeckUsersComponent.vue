<template>
    <body>
    <section class="decks-section">
        <div class="container py-5">
        <h1 style="text-align: center; margin-bottom: 46px;">Your Decks</h1>
        <div class="deck-grid">
            <div
            class="deck-card"
            v-for="deck in userDecks"
            :key="deck.id"
            @click="navigateToDeckReview(deck.id)"
            >
            <div class="deck-card-body">
                <h5 class="deck-title">{{ deck.name }}</h5>
                <p class="deck-description">{{ deck.description }}</p>
            </div>
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
        selectedDeckId: null
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
    }
};
</script>

<style scoped>
@import "@/assets/css/flashcards.css";
@import "@/assets/css/styles.css";
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