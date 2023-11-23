Vue.createApp({
  data() {
    return {
      step: 1,
      showCreateCard: false,
      showAddCard: false,
      newDeck: {
        name: '',
        cards: []
      },
      newCard: {
        name: '',
        description: ''
      },
      allCards: [
        // Populate this array with existing cards from your backend
      ]
    };
  },
  methods: {
    nextStep() {
      this.step = 2; // Proceed to card addition options
    },
    addNewCardToDeck() {
      // Add the new card to the deck's cards array and proceed to options
      this.newDeck.cards.push({ ...this.newCard });
      this.newCard = { name: '', description: '' }; // Reset the new card form
      this.showCreateCard = false;
      this.step = 2; // Show options again
    },
    addExistingCardToDeck(card) {
      // Add an existing card to the deck's cards array and proceed to options
      this.newDeck.cards.push(card);
      this.showAddCard = false;
      this.step = 2; // Show options again
    },
    createDeck() {
      // Placeholder function for creating a deck
      // Here you would make an API call to your backend to save the new deck
      console.log('Creating deck with cards:', this.newDeck);
      // Reset the deck form (if needed)
      this.newDeck = { name: '', cards: [] };
      this.step = 1; // Go back to the first step
    }
  }
}).mount('#app');