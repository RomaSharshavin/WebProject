const texts = {% autoescape off %}{{ texts|safe }}{% endautoescape %};
let currentIndex = 0;

function changeText(direction) {
    currentIndex += direction; // Изменяем индекс
    if (currentIndex < 0) {
        currentIndex = texts.length - 1; // Циклический переход влево
    } else if (currentIndex >= texts.length) {
        currentIndex = 0; // Циклический переход вправо
    }
    document.getElementById('text-content').innerHTML = `<p>${texts[currentIndex]}</p>`; // Обновляем текст
}