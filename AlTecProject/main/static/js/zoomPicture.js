// Получаем элементы
const modal = document.getElementById('modal');
const modalBackground = document.getElementById('modal-background');
const modalImg = document.getElementById('modal-img');
const closeBtn = document.getElementById('close');

// Переменная для хранения текущего масштаба и состояния (увеличение или уменьшение)
let scale = 1;
let increasing = true;

// Открытие модального окна
document.querySelector('.clickable-image').onclick = function() {
    modalBackground.style.display = "block";
    modal.style.display = "flex";
    modalImg.src = this.src;
    scale = 1; // Сбрасываем масштаб при открытии
    modalImg.style.transform = "scale(1)";
    increasing = true; // Начинаем с увеличения
};

// Закрытие модального окна
closeBtn.onclick = function() {
    modalBackground.style.display = "none";
    modal.style.display = "none";
};

// Закрытие модального окна при клике вне изображения
modalBackground.onclick = function() {
    modalBackground.style.display = "none";
    modal.style.display = "none";
};

// Обработка кликов по изображению для увеличения и уменьшения
modalImg.onclick = function(e) {
    if (increasing) {
        // Увеличение по клику
        if (scale < 2) {
            scale += 1; // Увеличиваем масштаб
        } else {
            increasing = false; // Когда достигли максимума, переключаем на уменьшение
        }
    } else {
        // Уменьшение по клику
        if (scale > 1) {
            scale -= 1; // Уменьшаем масштаб
        } else {
            increasing = true; // Когда достигли минимума, переключаем на увеличение
        }
    }
    modalImg.style.transform = `scale(${scale})`; // Применяем новый масштаб
    e.stopPropagation(); // Предотвращаем закрытие модального окна
};