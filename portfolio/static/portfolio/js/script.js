(()=> {
    const formularies = document.querySelectorAll('.form-delete');

    for (const formulary of formularies) {
        formulary.addEventListener('submit', function(e) {
            e.preventDefault();
            const confirmed = confirm('Você tem certeza??')

            if (confirmed) {
                formulary.submit();
            }
        })
    }
})();

(()=> {
    const buttonCloseMenu = document.querySelector('.button-close-menu');
    const buttonShowMenu = document.querySelector('.button-show-menu');
    const menuContainer = document.querySelector('.menu-container');
    const buttonShowMenuVisibleClass = 'button-show-menu-visible';
    const menuHiddenClass = 'menu-hidden';

    console.log('Viviane do cuzão arrombado.... Sopa de porra!!!!');

    const closeMenu = () => {
        buttonShowMenu.classList.add(buttonShowMenuVisibleClass);
        menuContainer.classList.add(menuHiddenClass);
    };

    const showMenu = () => {
        buttonShowMenu.classList.remove(buttonShowMenuVisibleClass);
        menuContainer.classList.remove(menuHiddenClass);
    };

    if (buttonCloseMenu) {
        buttonCloseMenu.removeEventListener('click', closeMenu);
        buttonCloseMenu.addEventListener('click', closeMenu);
    }

    if (buttonShowMenu) {
        buttonShowMenu.removeEventListener('click', showMenu);
        buttonShowMenu.addEventListener('click', showMenu);
    }
})();

(()=> {
    const logoutLinks = document.querySelectorAll('.autores-logout-link');
    const formLogout = document.querySelector('.form-logout');

    for (const link of logoutLinks) {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            formLogout.submit();
        })
    }
})();

$(document).ready(function(){
    //ProgressBar
    let containerA = document.getElementById("circleA");
    let circleA = new ProgressBar.Circle(containerA, {
        color: '#fff',
        strokeWidth: 8,
        duration: 1400,
        from: { color: '#AAA'},
        to: { color: '#65DAF9'},
        step: function(state, circle){
            circle.path.setAttribute('stroke', state.color);
            let value = Math.round(circle.value() * 60);
            circle.setText(value + '%');
        }
    });
    let containerB = document.getElementById("circleB");
    let circleB = new ProgressBar.Circle(containerB, {
        color: '#fff',
        strokeWidth: 8,
        duration: 1600,
        from: { color: '#AAA'},
        to: { color: '#20B2AA'},
        step: function(state, circle){
            circle.path.setAttribute('stroke', state.color);
            let value = Math.round(circle.value() * 55);
            circle.setText(value + '%');
        }
    });
    let containerC = document.getElementById("circleC");
    let circleC = new ProgressBar.Circle(containerC, {
        color: '#fff',
        strokeWidth: 8,
        duration: 2000,
        from: { color: '#AAA'},
        to: { color: '#ADFF2F'},
        step: function(state, circle){
            circle.path.setAttribute('stroke', state.color);
            let value = Math.round(circle.value() * 70);
            circle.setText(value + '%');
        }
    });
    let containerD = document.getElementById("circleD");
    let circleD = new ProgressBar.Circle(containerD, {
        color: '#fff',
        strokeWidth: 8,
        duration: 2200,
        from: { color: '#AAA'},
        to: { color: '#CD853F'},
        step: function(state, circle){
            circle.path.setAttribute('stroke', state.color);
            let value = Math.round(circle.value() * 80);
            circle.setText(value + '%');
        }
    });
    let containerE = document.getElementById("circleE");
    let circleE = new ProgressBar.Circle(containerE, {
        color: '#fff',
        strokeWidth: 8,
        duration: 2200,
        from: { color: '#AAA'},
        to: { color: '#cf3293ff'},
        step: function(state, circle){
            circle.path.setAttribute('stroke', state.color);
            let value = Math.round(circle.value() * 95);
            circle.setText(value + '%');
        }
    });
    let containerF = document.getElementById("circleF");
    let circleF = new ProgressBar.Circle(containerF, {
        color: '#fff',
        strokeWidth: 8,
        duration: 1800,
        from: { color: '#AAA'},
        to: { color: '#261f63ff'},
        step: function(state, circle){
            circle.path.setAttribute('stroke', state.color);
            let value = Math.round(circle.value() * 95);
            circle.setText(value + '%');
        }
    });
    let containerG = document.getElementById("circleG");
    let circleG = new ProgressBar.Circle(containerG, {
        color: '#fff',
        strokeWidth: 8,
        duration: 1600,
        from: { color: '#AAA'},
        to: { color: '#5fad1eff'},
        step: function(state, circle){
            circle.path.setAttribute('stroke', state.color);
            let value = Math.round(circle.value() * 80);
            circle.setText(value + '%');
        }
    });

    //iniciando o loader quando o usuario chega no elemento
    let dataAreaOffset = $('#skills_area').offset();
    let stop = 0;

    $(window).scroll(function(e){
        let scroll = $(window).scrollTop();

        if (scroll > (dataAreaOffset.top - 500) && stop == 0) {
            circleA.animate(1.0);
            circleB.animate(1.0);
            circleC.animate(1.0);
            circleD.animate(1.0);
            circleE.animate(1.0);
            circleF.animate(1.0);
            circleG.animate(1.0);
            stop = 1;
        }
    });

    //Parallax
    setTimeout(function() {
        $('#skills_area').parallax({imageSrc: 'static/portfolio/image/cidadeparallax.png'});
    }, 250);
});