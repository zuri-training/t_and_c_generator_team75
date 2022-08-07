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



/**feedback js */












