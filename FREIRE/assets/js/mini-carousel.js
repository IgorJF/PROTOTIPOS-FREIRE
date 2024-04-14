const carousel = document.querySelector('.mini-carousel');
const carouselItems = document.querySelectorAll('.carousel-item');
const dotContainer = document.querySelector('.carousel-dots-mini');
let currentIndex = 0;
let intervalId;

// Define o intervalo para a troca automática dos slides
const intervalDuration = 3000; // Intervalo em milissegundos

// Cria os dots para cada item do carousel
carouselItems.forEach((_, index) => {
    const dot = document.createElement('span');
    dot.classList.add('carousel-dot');
    dot.setAttribute('data-index', index);
    dotContainer.appendChild(dot);
});

const dots = document.querySelectorAll('.carousel-dot');

// Adiciona event listener para os dots
dots.forEach(dot => {
    dot.addEventListener('click', () => {
        const dotIndex = parseInt(dot.getAttribute('data-index'));
        goToSlide(dotIndex);
    });
});

// Ativa a troca automática dos slides
startCarousel();

function startCarousel() {
    intervalId = setInterval(() => {
        nextSlide();
    }, intervalDuration);
}

function stopCarousel() {
    clearInterval(intervalId);
}

function updateCarousel() {
    const itemWidth = carouselItems[0].offsetWidth;
    const scrollAmount = currentIndex * itemWidth;
    carousel.scrollTo({
        left: scrollAmount,
        behavior: 'smooth'
    });
    updateDots();
}

function updateDots() {
    dots.forEach(dot => {
        const dotIndex = parseInt(dot.getAttribute('data-index'));
        if (dotIndex === currentIndex) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % carouselItems.length;
    updateCarousel();
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + carouselItems.length) % carouselItems.length;
    updateCarousel();
}

function goToSlide(index) {
    currentIndex = index;
    updateCarousel();
}

carousel.addEventListener('mouseenter', stopCarousel);
carousel.addEventListener('mouseleave', startCarousel);
