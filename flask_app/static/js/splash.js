let intro = document.querySelector('.intro');
let headline = document.querySelector('.headline');
let headlinePart = document.querySelectorAll('.headline_part');

window.addEventListener('DOMContentLoaded', ()=>{
    
    setTimeout(()=>{

        headlinePart.forEach((span, idx)=>{
            setTimeout(()=> {
                span.classList.add('active');
            }, (idx + 1) * 400)
        })

        setTimeout(()=>{
            headlinePart.forEach((span, idx)=>{
                setTimeout(()=> {
                    span.classList.remove('active');
                    span.classList.add('fade');
                }, (idx + 1) * 50)
            })    
        }, 3000)
    
        setTimeout(()=>{
            intro.style.top = '-100vh';
        }, 3700)
        
        setTimeout(()=>{
            window.location.replace("./coffeegonewild/home");
        }, 4300)
        
    }) 
})