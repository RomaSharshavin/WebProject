function toggleCharacteristics(){var descriptionElem=document.querySelector('.service-description');var characteristicsElem=document.querySelector('.service-characteristics');if(characteristicsElem.style.display==="none"){characteristicsElem.style.display="block";descriptionElem.style.display="none";document.getElementById('toggle-characteristics').innerText="Скрыть характеристики";}else{characteristicsElem.style.display="none";descriptionElem.style.display="block";document.getElementById('toggle-characteristics').innerText="Посмотреть характеристики";}}
function orderCalculation(){const productName="Системы очистки воды";window.location.href="/write/?product="+encodeURIComponent(productName);};