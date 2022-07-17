//const { links } = require("express/lib/response");

const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');


    burger.addEventListener('click',() => { 
        //toggle nav bar as sidebar
        nav.classList.toggle('nav-links-active');

        //animate links into sidebar
        navLinks.forEach((link,index) => {
            if (link.style.animation) {
            link.style.animation = '';
            }
            else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7+0.3}s`;
            }
        });
        //animate burger to turn into x when clicked
        burger.classList.toggle('turnburger');
    });

}
navSlide();
