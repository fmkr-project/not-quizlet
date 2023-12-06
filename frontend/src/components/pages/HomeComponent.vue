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
            <div class="col"><div class="flashcard-example red" id="flashcard-example-1">
<div class="flashcard-example-content">
    <div class="flashcard-example-front red">
        <h3>Who invented the first computer in the world?</h3>
        <button class="btn btn-light btn-large">FLIP</button>
    </div>
    <div class="flashcard-example-back red">
        <h3>Konrad Zuse in 1936 by the name Z1</h3>
        <button class="btn btn-light btn-large">FLIP</button>
    </div>
</div>
</div>
</div>
            <div class="col"><div class="flashcard-example yellow" id="flashcard-example-2">
<div class="flashcard-example-content">
    <div class="flashcard-example-front yellow">
        <h3>Who invented all the parts that are now used for a modern computer?</h3>
        <button class="btn btn-light btn-large">FLIP</button>
    </div>
    <div class="flashcard-example-back yellow">
        <h3>Charles Babbage in 1833.</h3>
        <button class="btn btn-light btn-large">FLIP</button>
    </div>
</div>
</div>
</div>
            <div class="col"><div class="flashcard-example blue" id="flashcard-example-3">
<div class="flashcard-example-content">
    <div class="flashcard-example-front blue">
        <h3>Who invented the "Clarke Calculator"?</h3>
        <button class="btn btn-light btn-large">FLIP</button>
    </div>
    <div class="flashcard-example-back blue">
        <h3>Edith Clarke in 1925</h3>
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
import "@/assets/js/flashcard-example.js";
export default {
  name: 'HomeComponent',
};
</script>
<style scoped>
@import "@/assets/css/flashcard-examples.css";
@import "@/assets/css/styles.css";
</style>