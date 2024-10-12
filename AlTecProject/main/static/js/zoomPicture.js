let currentIndex = 0;
const images = document.querySelectorAll('.clickable-image');
const modal = document.getElementById('modal');
const modalImg = document.getElementById('modal-img');
let zoomFactor = 0.5; // Переменная для настройки увеличения зума

// Функция для открытия модального окна
function openModal(clickedImage) {
    currentIndex = Array.from(images).indexOf(clickedImage);
    modal.style.display = 'block';
    setModalImage(clickedImage.src); // Установка изображения в модальном окне
}

// Функция для закрытия модального окна
function closeModal() {
    modal.style.display = 'none';
}

// Функция для установки изображения в модальном окне с учетом зума
function setModalImage(src) {
    modalImg.src = src;
    modalImg.style.transform = `scale(${zoomFactor})`;
}

// Функция для показа предыдущего изображения
function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    setModalImage(images[currentIndex].src); // Обновление изображения с учетом зума
}

// Функция для показа следующего изображения
function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    setModalImage(images[currentIndex].src); // Обновление изображения с учетом зума
}

// Обработчик событий нажатия клавиш
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
        e.preventDefault();
    } else if (e.key === 'ArrowLeft') {
        prevImage();
        e.preventDefault();
    } else if (e.key === 'ArrowRight') {
        nextImage();
        e.preventDefault();
    }
});
