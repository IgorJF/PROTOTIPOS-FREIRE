document.addEventListener("DOMContentLoaded", function () {
    const newCarousel = document.querySelector(".carousel-sobre");
    const images = newCarousel.querySelectorAll("img");
    const carouselDotsContainer = document.querySelector(".carousel-dots-sobre");

    let currentIndex = 0;

    function navigateCarousel(index) {
        currentIndex = index;
        const offset = -index * 100;
        newCarousel.style.transform = `translateX(${offset}%)`;
        updateActiveDot();
    }

    function updateActiveDot() {
        const dots = Array.from(carouselDotsContainer.querySelectorAll(".carousel-dot-sobre"));
        dots.forEach((dot, index) => {
            if (index === currentIndex) {
                dot.classList.add("active");
            } else {
                dot.classList.remove("active");
            }
        });
    }      

    function createCarouselDots() {
        images.forEach((_, index) => {
            const dot = document.createElement("span");
            dot.classList.add("carousel-dot-sobre");
            dot.addEventListener("click", () => {
                navigateCarousel(index);
            });
            carouselDotsContainer.appendChild(dot); // Adiciona o dot ao container correto
        });
    }    

    createCarouselDots();

    updateActiveDot();

    setInterval(() => {
        currentIndex = (currentIndex + 1) % images.length;
        navigateCarousel(currentIndex);
    }, 5000);
});