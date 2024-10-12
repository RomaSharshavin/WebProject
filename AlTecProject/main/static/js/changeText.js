const texts = JSON.parse(document.getElementById('texts-data').textContent);
let currentIndex = 0;

function changeText(direction) {
    currentIndex += direction; // Изменяем индекс
    if (currentIndex < 0) {
        currentIndex = texts.length - 1; // Циклический переход влево
    } else if (currentIndex >= texts.length) {
        currentIndex = 0; // Циклический переход вправо
    }
    document.getElementById('text-content').innerHTML = texts[currentIndex]; // Обновляем текст
}
