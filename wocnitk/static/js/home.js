var hamburger = document.getElementById("hamburger");
var line1 = document.getElementsByClassName("line-1")[0];
var line2 = document.getElementsByClassName("line-2")[0];
var line3 = document.getElementsByClassName("line-3")[0];

hamburger.addEventListener("click", function () {
  line1.classList.toggle("open");
  line2.classList.toggle("open");
  line3.classList.toggle("open");
  document.querySelector("nav").classList.toggle("open");
});
