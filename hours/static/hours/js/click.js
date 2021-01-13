
let btnShow = document.querySelector('button')


btnShow.addEventListener('click',()=>{
    let today = new Date()

    let hour = today.getHours();
    let mi = today.getMinutes();

    let current_date = `${hour}:${mi}`;
    btnShow.innerText = current_date;
})