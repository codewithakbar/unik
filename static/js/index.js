var swipeer = new Swiper(".meSwiper", {
  slidesPerView: 3,
  centeredSlides: true,
  spaceBetween: 30,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});

window.addEventListener("resize", function() {
  if (window.innerWidth <= 768) {
    swipeer.params.slidesPerView = 1;
  } else {
    swipeer.params.slidesPerView = 3;
  }
  swipeer.update();
});