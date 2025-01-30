let currentIndex=0;const images=document.querySelectorAll('.clickable-image');const modal=document.getElementById('modal');const modalImg=document.getElementById('modal-img');let zoomFactor=0.5;function openModal(clickedImage){currentIndex=Array.from(images).indexOf(clickedImage);modal.style.display='block';setModalImage(clickedImage.src);}
function closeModal(){modal.style.display='none';}
function setModalImage(src){modalImg.src=src;modalImg.style.transform=`scale(${zoomFactor})`;}
function prevImage(){currentIndex=(currentIndex-1+images.length)%images.length;setModalImage(images[currentIndex].src);}
function nextImage(){currentIndex=(currentIndex+1)%images.length;setModalImage(images[currentIndex].src);}
document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeModal();e.preventDefault();}else if(e.key==='ArrowLeft'){prevImage();e.preventDefault();}else if(e.key==='ArrowRight'){nextImage();e.preventDefault();}});;