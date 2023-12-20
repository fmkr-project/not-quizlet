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
<section>
    <div class="container py-5" data-aos="fade-up">
        <h1 style="text-align: center;margin-bottom: 46px;">User-created Flashcards to learn together!</h1>
        <div class="row" data-aos="zoom-in" style="margin-bottom: 60px;text-align: center;">
            <div class="col" v-for="card in flashcards" :key="card.id">
  <div class="flashcard" @click="toggleFlip(card.id)">
    <div class="flashcard-content" :class="{ flipped: card.flipped }">
      <div class="flashcard-front" :style="{ backgroundColor: card.color }">
        <h4 class="card-label">Question</h4>
        <h3 :style="{fontSize: calculateFontSize(card.question)}">{{ card.question }}</h3>
        <button class="btn btn-light btn-large">FLIP</button>
      </div>
      <div class="flashcard-back" :style="{ backgroundColor: card.color}">
        <h4 class="card-label">Answer</h4>
        <h3 :style="{fontSize: calculateFontSize(card.answer)}">{{ card.answer }}</h3>
        <button class="btn btn-light btn-large">FLIP</button>
      </div>
    </div>
  </div>
</div>
    </div>        
        <div class="mx-auto" style="max-width: 900px;">
            <div class="row row-cols-1 row-cols-md-2 d-flex justify-content-center">
                <div class="col mb-4">
                    <div class="card bg-primary-subtle">
                        <div class="card-body text-center px-4 py-5 px-md-5" data-aos="fade-up">
                            <p class="fw-bold text-primary card-text mb-2">Interactive Learning Tools</p>
                            <h5 class="fw-bold card-title mb-3">Dive into a variety of engaging learning activities.<br><br>From flashcards to match-up games, our app makes study sessions both effective and enjoyable.<br><br>Tailored to different learning styles, the interactive tools help reinforce memory retention and understanding.</h5>
                        </div>
                    </div>
                </div>
                <div class="col mb-4">
                    <div class="card bg-secondary-subtle">
                        <div class="card-body text-center px-4 py-5 px-md-5" data-aos="fade-up">
                            <p class="fw-bold text-secondary card-text mb-2">Custom Study Sets</p>
                            <h5 class="fw-bold card-title mb-3">Create personalized study sets or explore those made by other learners.<br><br>Whether you're mastering a language or gearing up for a biology exam, our app's vast library of user-generated content has something for everyone!</h5>
                        </div>
                    </div>
                </div>
                <div class="col mb-4">
                    <div class="card bg-info-subtle">
                        <div class="card-body text-center px-4 py-5 px-md-5" data-aos="fade-up">
                            <p class="fw-bold text-info card-text mb-2">Track your progress</p>
                            <h5 class="fw-bold card-title mb-3">With our progression tracking features, you can set goals and monitor your improvement over time.<br><br>Visualize your learning journey with insightful analytics and stay motivated as you conquer each learning milestone.</h5>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
</body>
</template>
<script>
export default {
  name: 'HomeComponent',
  data() {
    return {
      flashcards: [
      { id: 1, question: 'What is the Heisenberg Uncertainty Principle?', answer: 'It states that the position and the velocity of an object cannot both be measured exactly, at the same time, even in theory.', color: '#FF6B6B', flipped: false },
      { id: 2, question: 'What is the significance of the Turing Test in Artificial Intelligence?', answer: 'The Turing Test measures a machine\'s ability to exhibit intelligent behavior equivalent to, or indistinguishable from, that of a human.', color: '#FFD93D', flipped: false },
      { id: 3, question: 'What is Keynesian Economics?', answer: 'An economic theory stating that active government intervention in the marketplace and monetary policy is the best method of ensuring economic growth and stability.', color: '#6BCB77', flipped: false },
      { id: 4, question: 'What is Schrödinger\'s Cat thought experiment?', answer: 'A paradox that illustrates the problem of the Copenhagen interpretation of quantum mechanics applied to everyday objects, in this case, a cat in a box.', color: '#4D96FF', flipped: false },
      { id: 5, question: 'What does Moore\'s Law state?', answer: 'The number of transistors on a microchip doubles about every two years, though the cost of computers is halved.', color: '#A663CC', flipped: false },
      { id: 6, question: 'What is the principle of Comparative Advantage in Economics?', answer: 'The ability of an individual or group to carry out a particular economic activity more efficiently than another activity.', color: '#FF926B', flipped: false }
        // ... other flashcards
      ],
    };
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
    }
  }
};
</script>
<style scoped>
@import "@/assets/css/flashcards.css";
@import "@/assets/css/styles.css";
</style>