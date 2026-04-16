const allSideMenu = document.querySelectorAll('#barra_lateral .side-menu.top li a');

allSideMenu.forEach(item => {
    const li = item.parentElement;

    item.addEventListener('click', function () {
        allSideMenu.forEach(i => {
            i.parentElement.classList.remove('active');
        });

        li.classList.add('active');
    });
});



//BARRA LATERAL
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const barra_lateral = document.getElementById('barra_lateral');

menuBar.addEventListener('click', function () {
    barra_lateral.classList.toggle('hide');
})





const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button i');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
    if(window.innerWidth < 576) {
        e.preventDefault();

        const isOpen = searchForm.classList.toggle('show');

        if(isOpen) {
            searchButtonIcon.classList.replace('bx-search','bx-x');
        } else {
            searchButtonIcon.classList.replace('bx-x','bx-search');
        }
    }
});

window.addEventListener('resize', function () {
    if(window.innerWidth < 768) {
        barra_lateral.classList.add('hide');
    } else {
        barra_lateral.classList.remove('hide');
    }
});

if(menuBar) {
    menuBar.addEventListener('click', function () {
        barra_lateral.classList.toggle('hide');
    });
}
