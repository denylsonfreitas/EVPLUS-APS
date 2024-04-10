let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", ()=>{
    sidebar.classList.toggle("open");
    menuBtnChange();
});

searchBtn.addEventListener("click", (event)=>{ 
    event.preventDefault(); // Evita que o link seja seguido
    sidebar.classList.toggle("open");
    menuBtnChange();
});

function menuBtnChange() {
if(sidebar.classList.contains("open")){
    closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
}else {
    closeBtn.classList.replace("bx-menu-alt-right","bx-menu");
}
}

document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        var alertContainer = document.getElementById('alert-container');
        alertContainer.innerHTML = '';
    }, 7000);
});