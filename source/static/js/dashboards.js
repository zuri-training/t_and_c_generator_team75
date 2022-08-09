const hamburger = document.querySelector('#hamburger');
const navbar = document.querySelector('.navs');
const lines =document.querySelectorAll('#hamburger div')


        hamburger.addEventListener('click', function(){
            lines.forEach(line => line.classList.toggle('colorchange'));
            hamburger.classList.toggle('isactive');
            navbar.classList.toggle('active');
        });

        const clicks = document.querySelectorAll('.clicks');
        const policyBtn = document.querySelector(".policy-button"); 
        const policyPopup = document.querySelector(".popup-container");
        const close = document.querySelector(".close");
        
        close.addEventListener('click', function() {
          policyPopup.style.display = "none";
          header.style.backgroundColor = '#fff';
        });
        
        policyBtn.addEventListener("click", function(event) {
          event.preventDefault();
          policyPopup.style.display = "block";
          header.style.backgroundColor = 'rgba(21, 17, 17, 0.61)';
        });
        
        for(let i = 0; i < clicks.length; i++) {
         
            
          
          clicks[i].addEventListener('click', function(e) {
            
            e.preventDefault();
            for(let i =0;  i < clicks.length; i++) {
              clicks[i].style.color = "#F9F9F9";
              clicks[i].style.backgroundColor = "#251B2C";
            }
          
            
             e.target.style.color = "#A535F1";
            e.target.style.backgroundColor = "#F9F9F9";
           
          });
          
        }
        /***form *****/
        const messageicon = document.querySelector(".messageicon");
        const form = document.querySelector(".form");
        const eks = document.querySelector(".eks");
        const header = document.querySelector('header');
     
        eks.addEventListener('click', function () {
          form.style.display = 'none';
        });
        messageicon.addEventListener('click', function () {
          form.style.display = "block";
          
        });
        
        /** user dropdown **/
        const user = document.querySelector('.user');
        const closed = document.querySelector('.user-info')
        user.addEventListener('click', function(){
          closed.classList.toggle("open");

          

        });
  
       