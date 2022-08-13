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
        const submit = document.querySelector(".submit");
        const response = document.querySelector(".close2");
        const acform = document.querySelector(".form");
        const eks2 = document.querySelector(".eks2");
        const sendAgain = document.querySelector(".again");

        sendAgain.addEventListener('click', function () {
          acform.style.display = 'block';
          response.style.display = "none";
        });


        submit.addEventListener('click', function(e){
          e.preventDefault()
          acform.style.display = "none";
          response.style.display ="block";
          
        });

        eks2.addEventListener('click', function () {
          form.style.display = 'none';
        });

     
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
  
       