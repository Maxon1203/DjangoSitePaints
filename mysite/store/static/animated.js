// Получаем элемент для анимации
const background = document.getElementById('animated-background');

// Создаем частицы и добавляем их в DOM
for (let i = 0; i < 700; i++) {
    let star = document.createElement('div');
    star.className = 'star';
    star.style.left = `${Math.random() * window.innerWidth}px`;
    star.style.top = `${Math.random() * window.innerHeight}px`;
    background.appendChild(star);
}

// Анимация каждой звезды
function animateStars() {
    document.querySelectorAll('.star').forEach(star => {
        star.style.transition = 'all 1s linear';
        star.style.transform = `translate(${Math.random() * 20 - 5}px, ${Math.random() * 10 - 5}px)`;
    });

    // Повторяем анимацию каждые 0.5 секунды
    setTimeout(animateStars, 500);
}

// Начинаем анимацию
animateStars();
