/* eslint-disable */
class Flashcard {
    constructor(frontContent, backContent, colorClass) {
      this.frontContent = frontContent;
      this.backContent = backContent;
      this.colorClass = colorClass;
      this.element = null;
      this.createFlashcard();
    }
  
    createFlashcard() {
      this.element = document.createElement('div');
      this.element.classList.add('flashcard', this.colorClass);
  
      const contentContainer = document.createElement('div');
      contentContainer.classList.add('flashcard-content');
  
      const frontSide = document.createElement('div');
      frontSide.classList.add('front');
      frontSide.innerHTML = this.frontContent;
  
      const backSide = document.createElement('div');
      backSide.classList.add('back');
      backSide.innerHTML = this.backContent;
  
      contentContainer.appendChild(frontSide);
      contentContainer.appendChild(backSide);
  
      this.element.appendChild(contentContainer);
      this.setupEventListeners();
    }
  
    setupEventListeners() {
      this.element.addEventListener('click', () => {
        this.element.classList.toggle('flipped');
      });
    }
  
    appendTo(container) {
      container.appendChild(this.element);
    }
}
export default Flashcard;