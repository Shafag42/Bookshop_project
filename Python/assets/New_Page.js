let number = parseInt(prompt("Kitabın səhifə sayı:"));

while (isNaN(number) || number<=0 ) {
  alert("Hesablamada problem baş verdi");
  number = parseInt(prompt("Number"));

}
console.log("number- ",number)

let day=(prompt("Neçə günə bitirməlisiniz?"))
while (isNaN(day) || day==0 || day<=0) {
  alert("Hesablamada problem baş verdi");
  day=(prompt("How many days?"))
}
console.log("day- ",day)

result=Math.ceil(number/day)
alert ("Hər gün ən az " + result + " səhifə oxumalısınız!")
console.log("result- ",result)



   
  







