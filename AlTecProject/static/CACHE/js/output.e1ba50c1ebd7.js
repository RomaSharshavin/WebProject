function init(){var myMap=new ymaps.Map("map",{center:[59.9386,30.3141],zoom:9,controls:['zoomControl']});var myPlacemarkSPB=new ymaps.Placemark([59.939374,30.433026],{balloonContent:'<div class="balloon-content">'+'<p>Дополнительная информация здесь.</p>'+'</div>'});myMap.geoObjects.add(myPlacemarkSPB);myPlacemarkSPB.events.add("click",function(){myMap.setCenter([59.939374,30.433026],15,{duration:2000});});};var script=document.createElement('script');script.src='https://api-maps.yandex.ru/2.1/?lang=ru_RU&apikey=61fc745e-0472-420e-9603-840cb0d46167';script.async=true;document.body.appendChild(script);script.onload=function(){if(typeof ymaps!=='undefined'){ymaps.ready(init);}else{console.error("ERROR MAP");}};function init(){var myMap=new ymaps.Map("map",{center:[59.9386,30.3141],zoom:9,controls:['zoomControl']});var myPlacemarkSPB=new ymaps.Placemark([59.939374,30.433026],{balloonContent:'<div class="balloon-content">'+'<p>Дополнительная информация здесь.</p>'+'</div>'});myMap.geoObjects.add(myPlacemarkSPB);myPlacemarkSPB.events.add("click",function(){myMap.setCenter([59.939374,30.433026],15,{duration:2000});});};