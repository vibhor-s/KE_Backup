var sidemenu_product_submenu_flag = 0;
'use strict';
var slideIndex = 0;
var timer = null;
showSlides();


function plusSlides(n) {
  clearTimeout(timer);
  showSlides(slideIndex += n);

}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  //alert('showslides('+ n +')\nslideIndex='+slideIndex);
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n==undefined){n = ++slideIndex}
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  
  timer = setTimeout(showSlides, 3000); // Change image every 3 seconds
}
























function openNav()
{
  document.getElementById("mySideNav").style.width = "75%";
}

function closeNav()
{
  document.getElementById("mySideNav").style.width = "0";
}



function close_product_submenu()
{
  if(sidemenu_product_submenu_flag===1)
  {
    document.getElementById("sidemenu_product_submenu").style.display = "none";
    document.getElementById("close_product_submenu_minus_button").style.display = "none"; 
    document.getElementById("close_product_submenu_plus_button").style.display = "inline-block"; 
    sidemenu_product_submenu_flag = 0;
  }
  else
  {
    document.getElementById("sidemenu_product_submenu").style.display = "block";
    document.getElementById("close_product_submenu_minus_button").style.display = "inline-block"; 
    document.getElementById("close_product_submenu_plus_button").style.display = "none"; 
    sidemenu_product_submenu_flag = 1;
  }
}




