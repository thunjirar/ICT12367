const count = document.querySelector(".count")
const input = document.querySelector(".input")
input.addaEventListener("keyup",()=>{
        count.innerHTML=input.value.length
})