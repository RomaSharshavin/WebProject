ymaps.ready(init);
function init() {
    var myMap = new ymaps.Map("map", {
        center: [59.939374, 30.433026], // Координаты центра карты (Санкт-Петербург)
        zoom: 13, // Уровень увеличения
        controls: ['zoomControl'] // Элементы управления
    });

    // Добавление метки
    var myPlacemark = new ymaps.Placemark([59.939374, 30.433026], {
        balloonContent: 'ООО "Ал-Тек"'
    });

    myMap.geoObjects.add(myPlacemark);
}