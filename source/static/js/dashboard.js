const hamburger = document.querySelector('#hamburger');
const navbar = document.querySelector('.navs');
const lines =document.querySelectorAll('#hamburger div')


        hamburger.addEventListener('click', function(){
            lines.forEach(line => line.classList.toggle('colorchange'));
            hamburger.classList.toggle('isactive');
            navbar.classList.toggle('active');
        });

        const clicks = document.querySelectorAll('.clicks');
        
        
        for(let i = 0; i < clicks.length; i++) {
         
            
          
          clicks[i].addEventListener('click', function(e) {
            
            
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
        const form = document.querySelector(".popup-form");
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
  
       