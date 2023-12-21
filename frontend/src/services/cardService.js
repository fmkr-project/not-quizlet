/* eslint-disable */
import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL + "cards/"; // Assuming your API URL is in the .env file

class CardService {
  // Fetches cards created by a specific user
  async fetchUserCards() {
    try {
      const response = await axios.get(API_URL + `mycard/view`, { withCredentials: true });
      return { success: true, cards: response.data.cards };
    } catch (error) {
      let message = 'Failed to fetch cards';
      if (error.response) {
        // You can expand on error handling based on the status codes
        message = error.response.data.error || message;
      }
      return { success: false, message };
    }
  }



  // ... any other card-related methods
}

export default new CardService();
