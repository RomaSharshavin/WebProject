let currentIndex = 0;

function initialize() {
    const textElement = document.getElementById('text-content');
    const imageElement = document.getElementById('partner-image');
    const imageContainer = document.querySelector('.image-container');

    // Устанавливаем начальные значения
    textElement.innerHTML = texts[currentIndex]; // Начальный текст
    imageElement.src = images[currentIndex].src; // Начальное изображение
    imageElement.style.width = images[currentIndex].width; // Задаем ширину
    imageElement.style.height = images[currentIndex].height; // Задаем высоту

    // Убираем прозрачность, чтобы показать их сразу
    textElement.style.opacity = 1;
    imageContainer.style.opacity = 1;
}

function changeText(direction) {
    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = texts.length - 1;
    } else if (currentIndex >= texts.length) {
        currentIndex = 0;
    }

    const textElement = document.getElementById('text-content');
    const imageElement = document.getElementById('partner-image');
    const imageContainer = document.querySelector('.image-container');

    // Плавное изменение текста
    textElement.style.opacity = 0; // Убираем текст
    setTimeout(() => {
        textElement.innerHTML = texts[currentIndex]; // Обновляем текст
        textElement.style.opacity = 1; // Возвращаем текст
    }, 500); // Долговечность перехода

    // Плавное изменение изображения
    imageContainer.style.opacity = 0; // Убираем изображение
    setTimeout(() => {
        imageElement.src = images[currentIndex].src; // Обновляем изображение
        imageElement.style.width = images[currentIndex].width; // Задаем ширину
        imageElement.style.height = images[currentIndex].height; // Задаем высоту
        imageContainer.style.opacity = 1; // Возвращаем изображение
    }, 500); // Долговечность перехода
}

// Инициализируем при загрузке страницы
window.onload = initialize;
