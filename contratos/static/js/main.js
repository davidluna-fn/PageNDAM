var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
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
}

function showLightbox() {
  document.getElementById('over').style.display='block';
   document.getElementById('fade').style.display='block';
}
function hideLightbox() {
  document.getElementById('over').style.display='none';
  document.getElementById('fade').style.display='none';
}

function showLightboxLogin() {
  document.getElementById('overLogin').style.display='block';
  document.getElementById('fade').style.display='block';
}
function hideLightboxLogin() {
  document.getElementById('overLogin').style.display='none';
  document.getElementById('fade').style.display='none';
}

function resetform() {
    document.getElementById("form-busqueda").reset();
}

