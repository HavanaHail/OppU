let addyearcounter = 0;

function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");

}
function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");

}
function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");

}
function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");

}

function incrementAge() {
  addyearcounter = addyearcounter+1
  console.log(addyearcounter)
  if (addyearcounter % 2==0) {
    console.log ("add year counter")
    var popup = document.getElementById("popup1");
    popup.style.visibility="visible";
    popup.style.opacity="1";
  }
};

function closePopUp() {
  var popup = document.getElementById("popup1")
  popup.style.visibility="hidden";
  popup.style.opacity="0";

}
