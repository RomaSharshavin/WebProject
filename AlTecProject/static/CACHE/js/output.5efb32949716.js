const contentData=[{text:`ООО "Ал-Тек" является официальным представителем финской компании Tammermatic
                                и поставляет, устанавливает и обслуживает автоматические мойки для легкового,
                                грузового, пассажирского и железнодорожного транспорта. Поддержать моечное
                                оборудование в отличном состоянии поможет наша сервисная служба.`,img:'/static/images/about1.webp'},{text:`Мы начали свой путь в 2010 году с поставок высокотехнологичного оборудования крупнейшим
                        организациям России, расположенным в разных городах страны. Со временем география нашей
                        деятельности расширилась, и теперь мы успешно сотрудничаем с клиентами в Беларуси и Казахстане.`,img:'/static/images/about2.webp'}];let currentIndex=0;function updateContent(){const aboutTextContainer=document.querySelector('.about-text p');const aboutImageContainer=document.querySelector('.about-image img');aboutTextContainer.innerHTML=contentData[currentIndex].text;aboutImageContainer.src=contentData[currentIndex].img;currentIndex=(currentIndex+1)%contentData.length;}
updateContent();setInterval(updateContent,10000);const scrollContent=document.getElementById('scroll-content');const companies=[{img:'/static/images/logo/rzd_dr_st_pos_rgb.webp'},{img:'/static/images/logo/vodo.webp'},{img:'/static/images/logo/mosinj.webp'},{img:'/static/images/logo/peter_metro.webp'},{img:'/static/images/logo/moscow_metro.webp'},{img:'/static/images/logo/aksel.webp'},{img:'/static/images/logo/Logo_statoil.webp'},{img:'/static/images/logo/sever.webp'},{img:'/static/images/logo/neste.webp'},{img:'/static/images/logo/ilim.webp'}];function addCompanies(){companies.forEach(company=>{const item=document.createElement('div');item.className='scroll-item fade-in';item.innerHTML=`<img src="${company.img}" alt="company logo">`;scrollContent.appendChild(item);});}
addCompanies();function duplicateItems(){const items=Array.from(scrollContent.children);items.forEach(item=>{const clone=item.cloneNode(true);scrollContent.appendChild(clone);});}
duplicateItems();const totalWidth=scrollContent.scrollWidth;const scrollDuration=totalWidth/120;document.styleSheets[0].insertRule(`
                    @keyframes scroll {
                        0% {
                            transform: translateX(0);
                        }
                        100% {
                            transform: translateX(-${totalWidth / 2}px);
                        }
                    }
                `,0);scrollContent.style.animation=`scroll ${scrollDuration}s linear infinite`;;