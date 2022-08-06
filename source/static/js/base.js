const hamburger = document.getElementById("hamburger");
const line1 = document.querySelector(".line1");
const line2 = document.querySelector(".line2");
const header = document.querySelector("header");
const navbar = document.querySelector(".navbar");
const navigation = document.querySelector(".navigation");
hamburger.onclick = () => {
    mobileNav();
}

function mobileNav() {
    navbar.classList.toggle('hide');
    line1.classList.toggle('line1-rotate');
    line2.classList.toggle('line2-rotate');

}

const tab = document.getElementsByClassName('tab');
const tabcontent = document.getElementsByClassName('tab-content');
for( let i = 0; i < tab.length; i++ ) {
    tab[i].addEventListener('click', function(){

        
        this.classList.toggle('active');
        
        
        var tabcontent = this.nextElementSibling;
        if (tabcontent.style.maxHeight){
            tabcontent.style.maxHeight = null;
        }
        else {
            tabcontent.style.maxHeight = tabcontent.scrollHeight + "px";
        }


    });
}

/******** End Hamburger  *******/

function slide() {
    if (mediaQuery.matches) {
        const prev = document.querySelector('.arrow1');
        const next = document.querySelector('.arrow2');
        /*

        const slides = document.querySelectorAll('.feedback-boxes');


        slides.forEach((slide, index) => {
        slide.style.transform = `translateX(${index * 100}%)`;
        });

        let currentSlide = 0;

        let maxSlide = slides.length -1;*/
        const boxes = document.querySelectorAll('.feedback-box');

        const first = boxes[0];
        const second = boxes[1];
        const third = boxes[2];
        let array = [first, second, third];
        let currentSlide = 0;
        let maxSlide = 2;

        for(let i = 1; i < array.length; i++) {
            array[i].style.display = 'none';

        }
        next.addEventListener("click", function () {
            
            
            if(currentSlide === maxSlide) {
                currentSlide = 0;
            }
            else {
                currentSlide++;
            }
            for(let i = 0; i < array.length; i++) {
                array[i].style.display = 'none';
            
            }

            array[currentSlide].style.display = 'flex';


            

            /*array.forEach((array, index) => {
                array.style.transform = `translateX(${ 100 * (index - currentSlide )}%)`;
            });*/

            
        });

        prev.addEventListener("click", function () {
            console.log('click');
            if(currentSlide === 0 ) {
                currentSlide = maxSlide;
            }
            else {
                currentSlide--;
            }
            for(let i = 0; i < array.length; i++) {
                array[i].style.display = 'none';
            
            }
            array[currentSlide].style.display = 'flex';
            /*

            slides.forEach((slide, index) => {
                slide.style.transform = `translateX(${ 100 * (index - currentSlide )}%)`;
            });*/

            
        });

    }
}

const mediaQuery = window.matchMedia('(max-width: 960px)');

slide(mediaQuery);
mediaQuery.addEventListener(slide);








