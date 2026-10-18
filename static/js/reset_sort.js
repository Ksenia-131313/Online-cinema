document.addEventListener('DOMContentLoaded', function () {
    const navigation = performance.getEntriesByType('navigation')[0];

    if (navigation?.type === 'reload') {
        const path = window.location.pathname;

        if (path === '/filter/' || path === '/search/') {
            window.location.replace('/');
            return;
        }

        const url = new URL(window.location.href);

        if (url.searchParams.has('order')) {
            url.searchParams.delete('order');
            window.location.replace(url.toString());
        }
    }
});