let btn = document.querySelector(`.mobile-btn`);

const burgerFunc = (menuClassName, showClassName) => {
  let menu = document.querySelector(`.${menuClassName}`);

  if (menu.className.includes(showClassName)) {
    menu.className = menuClassName;
  } else {
    menu.className += ` ${showClassName}`;
  }
};

btn.addEventListener("click", () => {
  burgerFunc("nav", "header__menu-show ");
});
console.log(21);