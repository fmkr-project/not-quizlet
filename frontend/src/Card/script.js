// const app = Vue.createApp({
//     data() {
//       return {
//         showModal: false,
//         flipCard: false,
//         selectedCard: null,
//         cards: [], // This will be populated with data from your Flask API
//       };
//     },
//     methods: {
//       viewCardDetails(card) {
//         this.selectedCard = card;
//         this.flipCard = false; // Start with the front side
//         this.showModal = true; // Show the modal
//       },
//       toggleFlipCard() {
//         this.flipCard = !this.flipCard; // Toggle the flipped state
//       },
//       fetchCards() {
//         fetch('/api/cards') // Endpoint to your Flask API
//           .then(response => response.json())
//           .then(data => {
//             this.cards = data; // Assuming your Flask API sends back an array of cards
//           })
//           .catch(error => {
//             console.error('Error fetching cards:', error);
//           });
//       }
//     },
//     mounted() {
//       this.fetchCards(); // Fetch the cards from the Flask API when the component mounts
//     }
//   }).mount('#app');
  
const app = Vue.createApp({
  data() {
    return {
      showModal: false,
      flipCard: false,
      selectedCard: null,
      cards: [
        { id: 1, name: 'Card 1', description: 'Description for Card 1' },
        { id: 2, name: 'Card 2', description: 'Description for Card 2' },
        // More cards...
      ],
    };
  },
  methods: {
    viewCardDetails(card) {
      this.selectedCard = card;
      this.flipCard = false; // Start with the front side
      this.showModal = true; // Show the modal
    },
    toggleFlipCard() {
      this.flipCard = !this.flipCard; // Toggle the flipped state
    }
  }
}).mount('#app');