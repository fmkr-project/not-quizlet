const app = Vue.createApp({
    data() {
      return {
        showModal: false,
        flipCard: false,
        selectedCard: null,
        cards: [], // Will be populated with data from the Flask API
      };
    },
    methods: {
      // Method to fetch card data from Flask API
      fetchCardData() {
        fetch('/api/cards') // Adjust '/api/cards' to match your Flask API endpoint
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
          })
          .then(data => {
            this.cards = data.cards; // Adjust this if your JSON structure is different
          })
          .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
          });
      }
    },
    mounted() {
      this.fetchCardData(); // Fetch card data when the component is mounted
    }
  });
  
  app.mount('#app');
  