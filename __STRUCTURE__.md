not-quizlet
|-- backend
|   |-- app
|   |   |-- __init__.py
|   |   |-- config
|   |   |   |-- __init__.py
|   |   |   |-- development.py
|   |   |   |-- production.py
|   |   |   |-- testing.py
|   |   |-- models
|   |   |   |-- __init__.py
|   |   |   |-- user.py
|   |   |   |-- deck.py
|   |   |   |-- card.py
|   |   |-- services
|   |   |   |-- __init__.py
|   |   |   |-- user_service.py
|   |   |   |-- deck_service.py
|   |   |   |-- card_service.py
|   |   |-- api
|   |   |   |-- __init__.py
|   |   |   |-- v1
|   |   |   |   |-- __init__.py
|   |   |   |   |-- user_routes.py
|   |   |   |   |-- deck_routes.py
|   |   |   |   |-- card_routes.py
|   |   |-- utils
|   |   |   |-- __init__.py
|   |   |   |-- helpers.py
|   |   |-- errors
|   |   |   |-- __init__.py
|   |   |   |-- handlers.py
|   |   |-- tests
|   |       |-- __init__.py
|   |       |-- test_user.py
|   |       |-- test_deck.py
|   |       |-- test_card.py
|   |-- env
|   |   |-- .env
|   |   |-- __init__.py
|   |-- db
|   |   |-- __init__.py
|   |   |-- db.py
|   |-- migrations
|   |   |-- ...
|   |-- main.py
|   |-- requirements.txt
|
|-- database
|   |-- schema.sql
|   |-- data.db
|
|-- frontend
|   |-- node_modules
|   |   |-- ...
|   |-- public
|   |   |-- index.html
|   |   |-- favicon.ico
|   |-- src
|   |   |-- assets
|   |   |   |-- images
|   |   |   |-- styles
|   |   |-- components
|   |   |   |-- common
|   |   |   |   |-- Header.vue
|   |   |   |   |-- Footer.vue
|   |   |   |-- Deck
|   |   |   |   |-- DeckList.vue
|   |   |   |   |-- DeckView.vue
|   |   |   |   |-- DeckEdit.vue
|   |   |   |-- Card
|   |   |   |   |-- CardCreate.vue
|   |   |   |   |-- CardEdit.vue
|   |   |   |-- User
|   |   |   |   |-- UserProfile.vue
|   |   |   |   |-- UserSettings.vue
|   |   |-- views
|   |   |   |-- Home.vue
|   |   |   |-- Dashboard.vue
|   |   |   |-- Login.vue
|   |   |   |-- Register.vue
|   |   |-- store
|   |   |   |-- modules
|   |   |   |   |-- user.js
|   |   |   |   |-- deck.js
|   |   |   |   |-- card.js
|   |   |   |-- index.js
|   |   |-- router
|   |   |   |-- index.js
|   |   |-- App.vue
|   |   |-- main.js
|   |-- tests
|   |   |-- unit
|   |   |   |-- ...
|   |   |-- e2e
|   |   |   |-- ...
|   |-- .env.development
|   |-- .env.production
|   |-- package.json
|   |-- package-lock.json
|
|-- .gitignore
|-- README.md
|-- docker-compose.yml
|-- Dockerfile
