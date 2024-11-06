function init() {
    var myMap = new ymaps.Map("map", {
        center: [59.9386, 30.3141], // Координаты центра
        zoom: 9, // зум
        controls: ['zoomControl']
    });

    // Метка СПБ
    var myPlacemarkSPB = new ymaps.Placemark([59.939374, 30.433026], {
        balloonContent: '<div class="balloon-content">' +
        '<p>Дополнительная информация здесь.</p>' +
        '</div>'
    });

    myMap.geoObjects.add(myPlacemarkSPB);

    // Плавное перемещение к метке
    myPlacemarkSPB.events.add("click", function () {
        myMap.setCenter([59.939374, 30.433026], 15, {
            duration: 2000 // продолжительность анимации в мс
        });
    });
}
