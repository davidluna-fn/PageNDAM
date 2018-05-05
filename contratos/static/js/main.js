  
function showLightbox() {
  document.getElementById('fade').style.display='grid';
  document.getElementById('h-contacto').style.backgroundColor="#01A9DB";

}
function hideLightbox() {
  document.getElementById('fade').style.display='none';
  document.getElementById('h-contacto').style.backgroundColor="#353537";
}

function showLightboxLogin() {
  document.getElementById('fade-login').style.display='grid';
  document.getElementById('intranet-h').style.backgroundColor="#01A9DB";
}
function hideLightboxLogin() {
  document.getElementById('fade-login').style.display='none';
  document.getElementById('intranet-h').style.backgroundColor="#A4A4A4";
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
  var y = document.getElementsByClassName("mySlides-link");
  if (n > x.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
     y[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";
  y[slideIndex-1].style.display = "block";  
}



function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function headerActive(id){
 document.getElementById(id).style.backgroundColor = "#01A9DB";
 document.getElementById(id).style.marginBottom = "-20px;";
 document.getElementById(id).style.marginBottom = "";
}