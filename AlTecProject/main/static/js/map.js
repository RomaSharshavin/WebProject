ymaps.ready(init);
function init() {
    var myMap = new ymaps.Map("map", {
        center: [57.58239091081727, 34.56004699233066], // Координаты центра карты (Санкт-Петербург)
        zoom: 5, // Уровень увеличения
        controls: ['zoomControl'] // Элементы управления
    });

    // Добавление метки для Санкт-Петербурга
    var myPlacemarkSPB = new ymaps.Placemark([59.939374, 30.433026], {
        balloonContent: 'ООО "Ал-Тек"'
    });

    myMap.geoObjects.add(myPlacemarkSPB);

    // Удалите следующие строки, чтобы не добавлять метку в Москве
    // var myPlacemarkMosk = new ymaps.Placemark([55.468244, 37.574444], {
    //     balloonContent: 'Офис в Московской обл.'
    // });
    // myMap.geoObjects.add(myPlacemarkMosk);
}