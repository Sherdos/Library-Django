


// function openNav() {
//   document.getElementById("myNav").style.width = "25%";
// }

// /* Close when someone clicks on the "x" symbol inside the overlay */
// function closeNav() {
//   document.getElementById("myNav").style.width = '0%';
// }


var burgerMenu = document.querySelector('.burger-menu');
var burgerMenuIcon = document.querySelector('.burger-menu-icon');
var exe = document.querySelector('.exe');

burgerMenuIcon.addEventListener('click', function() {
    burgerMenu.classList.toggle('show');
    burgerMenuIcon.classList.toggle('bshow');
});

exe.addEventListener('click', function() {
    burgerMenu.classList.toggle('show');
    burgerMenuIcon.classList.toggle('bshow');
});
