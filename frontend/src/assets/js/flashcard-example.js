document.addEventListener('DOMContentLoaded', function () {
    var flashcards = document.querySelectorAll('.flashcard-example');

    flashcards.forEach(function (card) {
        card.addEventListener('click', function () {
            card.classList.toggle('flipped');
        });
    });
});