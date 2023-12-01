// JavaScript для создания эффекта параллакса
document.addEventListener('scroll', function(e) {
  var scrolled = window.pageYOffset;
  var parallaxElements = document.querySelectorAll('.parallax');

  parallaxElements.forEach(function(el) {
    var speed = el.dataset.parallaxSpeed;
    var offset = scrolled * speed;

    el.style.transform = 'translateY(' + offset + 'px)';
  });
});
