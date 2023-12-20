<template>
    <body>
        <header class="bg-primary-gradient">
        <div class="container pt-4 pt-xl-5">
            <div class="row pt-5" style="margin-bottom: 17px;">
                <div class="col-md-8 col-xl-6 text-center text-md-start mx-auto">
                    <div class="text-center">
                        <p class="fw-bold text-success mb-2">The Polyvalent Interactive Mastery App</p>
                        <h1 class="fw-bold">Learn With Pima&nbsp;</h1>
                    </div>
                    <div class="row light-cream-background">
                        <div class="col" style="text-align: center;">
                            <h5 class="fw-bold text-primary mb-3" style="text-align: center;margin-top: 26px;font-style: italic;">Passion</h5>
                        </div>
                        <div class="col">
                            <h5 class="fw-bold text-warning mb-3" style="text-align: center;margin-top: 26px;font-style: italic;">Inspiration</h5>
                        </div>
                        <div class="col">
                            <h5 class="fw-bold text-info mb-3" style="text-align: center;margin-top: 26px;font-style: italic;">Motivation</h5>
                        </div>
                        <div class="col">
                            <h5 class="fw-bold text-secondary mb-3" style="text-align: center;margin-top: 26px;font-style: italic;">Ambition</h5>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <section class="decks-section">
        <div class="container py-5">
        <h1 style="text-align: center; margin-bottom: 46px;">Public Decks</h1>
        <div class="deck-grid">
            <div class="deck-card" v-for="deck in adminDecks" :key="deck.id">
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
    name: 'DeckHubComponent',
    data() {
        return {
            adminDecks: [],
        };
    },
    created() {
        this.fetchAdminDecks();
    },
    methods: {
        toggleFlip(cardId) {
            this.flashcards = this.flashcards.map(card => ({
                ...card,
            flipped: card.id === cardId ? !card.flipped : card.flipped
            }));
        },
        calculateFontSize(text) {
            const baseSize = 18; // Base font size in pixels
            const maxSize = 30;  // Maximum font size
            const maxLength = 180; // Ideal max number of characters for base size

            let calculatedSize = baseSize * (maxLength / (text.length < maxLength ? text.length : maxLength));
            calculatedSize = calculatedSize > maxSize ? maxSize : calculatedSize;
            return calculatedSize + 'px';
        },
        async fetchAdminDecks() {
            const response = await DeckService.fetchAdminDecks();
            if (response.success) {
                this.adminDecks = response.decks;
            } else {
                console.error(response.message);
                // Handle error as needed
            }
        },
    }
};
</script>

<style scoped>
@import "@/assets/css/flashcards.css";
@import "@/assets/css/styles.css";

.decks-section {
  /* Style for the decks section */
}

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