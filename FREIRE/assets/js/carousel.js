document.addEventListener("DOMContentLoaded", function () {
    const serviceList = document.getElementById("serviceList");
    const carousel = document.querySelector(".carousel");
    const carouselDots = document.querySelector(".carousel-dots");
    const listItems = Array.from(serviceList.querySelectorAll("li"));

    const images = listItems.map(li => {
        const img = document.createElement("img");
        img.src = li.dataset.image;
        carousel.appendChild(img);

        const dot = document.createElement("span");
        dot.classList.add("carousel-dot");
        dot.addEventListener("click", () => {
            navigateCarousel(listItems.indexOf(li));
        });
        carouselDots.appendChild(dot);

        return img;
    });

    let currentIndex = 0;

    function navigateCarousel(index) {
        currentIndex = index;
        const offset = -index * 100;
        carousel.style.transform = `translateX(${offset}%)`;
        updateActiveDot();
        updateActiveListItem(); 
    }

    function updateActiveDot() {
        const dots = Array.from(carouselDots.querySelectorAll(".carousel-dot"));
        dots.forEach((dot, index) => {
            if (index === currentIndex) {
                dot.classList.add("ativo");
            } else {
                dot.classList.remove("ativo");
            }
        });
    }

    function updateActiveListItem() {
        listItems.forEach((item, index) => {
            if (index === currentIndex) {
                item.classList.add("ativo");
            } else {
                item.classList.remove("ativo");
            }
        });
    }

    updateActiveDot();
    updateActiveListItem();

    listItems.forEach((li, index) => {
        li.addEventListener("mouseenter", () => {
            navigateCarousel(index);
        });
    });

    setInterval(() => {
        currentIndex = (currentIndex + 1) % images.length;
        navigateCarousel(currentIndex);
    }, 5000);
});
