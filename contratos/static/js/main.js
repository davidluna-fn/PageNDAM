  
function showLightbox() {
  document.getElementById('fade').style.display='grid';

}
function hideLightbox() {
  document.getElementById('fade').style.display='none';
}

function showLightboxLogin() {
  document.getElementById('fade-login').style.display='grid';
}
function hideLightboxLogin() {
  document.getElementById('fade-login').style.display='none';
}
function resetform() {
document.getElementById("form-busqueda").reset();
}


var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}
