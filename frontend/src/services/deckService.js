/* eslint-disable */
import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL + "decks/";

class DeckService {
  // Fetches decks created by the admin
  async fetchAdminDecks() {
    try {
      const response = await axios.get(API_URL + 'public_decks', { withCredentials: true });
      return { success: true, decks: response.data.decks };
    } catch (error) {
      let message = 'Failed to fetch decks';
      if (error.response) {
        // You can expand on error handling based on the status codes
        message = error.response.data.error || message;
      }
      return { success: false, message };
    }
  }
  async fetchUserDecks() {
    try {
      const response = await axios.get(API_URL + 'get_user_decks', { withCredentials: true });
      return { success: true, decks: response.data.decks };
    } catch (error) {
      let message = 'Failed to fetch decks';
      if (error.response) {
        // You can expand on error handling based on the status codes
        message = error.response.data.error || message;
      }
      return { success: false, message };
    }
  }
  // Add other methods as needed for creating, modifying, or deleting decks
  async createDeck(deckData) {
    try {
      const response = await axios.post(API_URL + 'create', deckData, { withCredentials: true });
      return { success: true, message: 'Deck created successfully', deckId: response.data.id };
    } catch (error) {
      let message = 'Failed to create deck';
      if (error.response) {
        message = error.response.data.error || message;
      }
      return { success: false, message };
    }
  }

  async modifyDeck(deckId, deckData) {
    try {
      const response = await axios.put(API_URL + `modify/${deckId}`, deckData, { withCredentials: true });
      return { success: true, message: 'Deck modified successfully' };
    } catch (error) {
      let message = 'Failed to modify deck';
      if (error.response) {
        message = error.response.data.error || message;
      }
      return { success: false, message };
    }
  }

  // Method to get flashcards by deck ID
  async getFlashcardsByDeckId(deckId) {
    try {
      const response = await axios.get(API_URL + `${deckId}/flashcards`, { withCredentials: true });
      // Assuming the API returns an array of flashcards in the response's data
      return { success: true, flashcards: response.data.flashcards };
    } catch (error) {
      console.error('Error fetching flashcards:', error);
      // Handle the error appropriately
      return { success: false, message: 'Failed to fetch flashcards' };
    }
  }


  // ... any other deck-related methods
}

export default new DeckService();
