
document.addEventListener("DOMContentLoaded", () => {
    const carousel = document.querySelector(".movie-carousel");

    if (!carousel) return;

    const slides = [...carousel.querySelectorAll(".movie-carousel__slide")];
    const dotsContainer = carousel.querySelector(".movie-carousel__dots");
    const prevButton = carousel.querySelector(".movie-carousel__arrow--prev");
    const nextButton = carousel.querySelector(".movie-carousel__arrow--next");

    if (!slides.length) return;

    let activeIndex = 0;
    let timer;

    slides.forEach((slide, index) => {
        const dot = document.createElement("button");

        dot.type = "button";
        dot.className = "movie-carousel__dot";
        dot.setAttribute("aria-label", `Фильм ${index + 1}`);

        dot.addEventListener("click", () => {
            showSlide(index);
            restartTimer();
        });

        dotsContainer.appendChild(dot);
    });

    const dots = [...dotsContainer.querySelectorAll(".movie-carousel__dot")];

    function showSlide(index) {
        activeIndex = (index + slides.length) % slides.length;

        slides.forEach((slide, i) => {
            slide.classList.remove("is-active", "is-prev", "is-next");

            if (i === activeIndex) {
                slide.classList.add("is-active");
            } else if (
                i === (activeIndex - 1 + slides.length) % slides.length
            ) {
                slide.classList.add("is-prev");
            } else if (
                i === (activeIndex + 1) % slides.length
            ) {
                slide.classList.add("is-next");
            }
        });

        dots.forEach((dot, i) => {
            dot.classList.toggle("is-active", i === activeIndex);
        });
    }

    function restartTimer() {
        clearInterval(timer);
        timer = setInterval(() => {
            showSlide(activeIndex + 1);
        }, 10000);
    }

    prevButton.addEventListener("click", () => {
        showSlide(activeIndex - 1);
        restartTimer();
    });

    nextButton.addEventListener("click", () => {
        showSlide(activeIndex + 1);
        restartTimer();
    });

    showSlide(0);
    restartTimer();
});
