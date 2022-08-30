let hand = document.getElementById("hand");
let heart = document.getElementById("heart");
let closeBtn = document.getElementById("closeBtn");
let icons = document.querySelector('.icons');
let alert1 = document.getElementById("alert");
let btnAdd = document.getElementById("btnAdd");
let element = document.getElementById("element");
let badge = document.getElementById("badge");
let prices = document.querySelectorAll(".prices");
let sum1 = document.querySelector('.sum');
let modal = document.querySelector('.modal-body');
let sum = 0;
let closes=document.querySelectorAll('.closebtn');
let elements=document.querySelectorAll('.listElement');
prices[0].innerHTML=12;
prices[1].innerHTML=16;
prices[2].innerHTML=21;

sum=37;

sum1.innerHTML=sum;
btnAdd.addEventListener('click', () => {

    const result = btnAdd.classList.toggle("active");

    if (result) {
        btnAdd.innerHTML = "Səbətdən çıxart";
        btnAdd.classList.remove('btn-primary');
        btnAdd.classList.add('btn-secondary');
        alert1.classList.add('alert-danger');
        alert1.classList.remove('alert-warning');
        numbers.innerHTML= parseInt(numbers.innerHTML) - 1
        element.classList.remove("d-none");
        element.classList.add("d-flex");
        prices[0].classList.add('active');
        prices[0].classList.remove('d-none');
        prices[0].innerHTML=12;
        badge.innerHTML =  parseInt(badge.innerHTML) + 1
        modal.innerHTML = "Məhsul səbətə əlavə edildi"
        if(badge.innerHTML !== 0) badge.classList.remove('d-none')
        if(sum1.innerHTML == 0) sum = 0
        sum1.innerHTML = sum + parseInt(prices[0].innerHTML);


    } else {
        btnAdd.innerHTML = "Səbətə əlavə et";
        btnAdd.classList.remove('btn-secondary');
        btnAdd.classList.add('btn-primary');
        alert1.classList.remove('alert-danger');
        alert1.classList.add('alert-warning');
        numbers.innerHTML= parseInt(numbers.innerHTML) + 1
        element.classList.remove("d-flex");
        element.classList.add("d-none");
        modal.innerHTML = "Məhsulu səbətdən çıxardınız"
        badge.innerHTML =  parseInt(badge.innerHTML) -1
        
        sum1.innerHTML = sum - parseInt(prices[0].innerHTML);
    }




});
const numbers = document.getElementById('numbers')
for(let i=0;i<prices.length;i++){
    closes[i].addEventListener('click',()=>{
        elements[i].classList.add('d-none');
        if(closes[i].parentElement.innerText=="İncognito"){
            numbers.innerHTML= parseInt(numbers.innerHTML) + 1
        
            btnAdd.innerHTML = "Səbətə əlavə et";
            btnAdd.classList.remove('btn-secondary');
            btnAdd.classList.add('btn-primary');
        }

        badge.innerHTML= parseInt(badge.innerHTML) -1
        if(badge.innerHTML == 0) badge.classList.add('d-none')
        sum1.innerHTML=(parseInt(sum1.innerHTML)-parseInt(prices[i].innerHTML));
    })
}


hand.style.cursor = "pointer";
heart.style.cursor = "pointer";
heart.addEventListener('click', () => {
    if (heart.className == 'fa fa-heart fs-2 text-secondary') {
        heart.classList.remove('text-secondary');
        heart.classList.add('text-danger');
        alert("Kitabı bəyəndiniz!")
    } else {
        heart.classList.remove('text-danger');
        heart.classList.add('text-secondary');
        alert("Bəyənməkdən imtina etdiniz!")
    }


});

hand.addEventListener('click', () => {
    hand.style.transform = 'rotate(180deg)';
    hand.style.transition = 'all .4s ease-out';
})

const classes = hand.classList;

hand.addEventListener('click', function () {
    const result = classes.toggle("active");

    if (result) {
        hand.style.transform = 'rotate(180deg)';
        hand.style.transition = 'all .4s ease-out';
    } else {
        hand.style.transform = 'rotate(360deg)';
        hand.style.transition = 'all .4s ease-out';
    }
})