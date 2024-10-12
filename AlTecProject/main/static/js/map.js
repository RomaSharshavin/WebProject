ymaps.ready(init);
function init() {
    var myMap = new ymaps.Map("map", {
        center: [59.9386, 30.3141], // Координаты центра карты (Санкт-Петербург)
        zoom: 9, // Уровень увеличения
        controls: ['zoomControl'] // Элементы управления
    });

    // Добавление метки для Санкт-Петербурга
    var myPlacemarkSPB = new ymaps.Placemark([59.939374, 30.433026], {
        balloonContent: 'ул. Магнитогорская, д. 51, лит. Е, офис 313"'
    });

    myMap.geoObjects.add(myPlacemarkSPB);

    // Исправлено: использовано events вместо even
    myPlacemarkSPB.events.add("click", function () {
        myMap.setCenter([59.939374, 30.433026], 15, {
            duration: 2000 // Указываем продолжительность анимации в миллисекундах
        });
    });

}