
let currentIndex = 0;

function changeText(direction) {
    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = texts.length - 1;
    } else if (currentIndex >= texts.length) {
        currentIndex = 0;
    }
    document.getElementById('text-content').innerHTML = texts[currentIndex]; // Обновляем текст
    const imageElement = document.getElementById('partner-image');
    imageElement.src = images[currentIndex].src; // Обновляем изображение
    imageElement.style.width = images[currentIndex].width; // Задаем ширину
    imageElement.style.height = images[currentIndex].height; // Задаем высоту
}
