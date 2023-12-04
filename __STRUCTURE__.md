|-- frontend/                      # Assuming this is a Vue CLI generated structure
    |-- node_modules/
    |-- public/
    |-- src/
        |-- assets/
        |-- components/            # Reusable Vue components
            |-- auth/
                |-- LoginForm.vue
                |-- RegisterForm.vue
            |-- game/
                |-- GameLobby.vue
                |-- Flashcard.vue
                |-- Scoreboard.vue
                |-- GameTimer.vue
            |-- decks/
                |-- DeckList.vue
                |-- DeckView.vue
                |-- CardEditor.vue
        |-- views/                 # Vue components representing entire views/pages
            |-- Home.vue
            |-- Login.vue
            |-- Register.vue
            |-- Dashboard.vue
            |-- Game.vue
            |-- DeckManager.vue
        |-- router/
            |-- index.js           # Vue Router configuration
        |-- store/                 # Vuex store modules
            |-- index.js           # Vuex store main configuration
            |-- authModule.js
            |-- gameModule.js
            |-- deckModule.js
        |-- services/              # Services for API calls and WebSocket interactions
            |-- authService.js
            |-- gameService.js
            |-- deckService.js
        |-- App.vue
        |-- main.js
    |-- package.json
    |-- ...