<script>
    const breadcrumb = document.querySelector('.breadcrumb');
    const path = window.location.pathname.split('/').filter(Boolean); // Получаем путь URL

    let breadcrumbHTML = '<a href="/">Главная</a>'; // Начинаем с главной страницы

    path.reduce((acc, cur, index) => {
        const href = acc + '/' + cur; // Формируем ссылку
        breadcrumbHTML += ` &gt; <a href="${href}">${cur}</a>`;
        return href;
    }, '');

    breadcrumb.innerHTML = breadcrumbHTML;
</script>
