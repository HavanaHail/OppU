let addyearcounter = 0;

function SchoolPopup() {
  var popup = document.getElementById("schoolPopup");
  popup.classList.toggle("show");

}
function StudentPopup() {
  var popup = document.getElementById("studentPopup");
  popup.classList.toggle("show");

}
function ExtracurricularPopup() {
  var popup = document.getElementById("extracurricularPopup");
  popup.classList.toggle("show");

}
function NewLifePopup() {
  var popup = document.getElementById("newLifePopup");
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
