function check_room() {
    var checkRoom  = document.getElementById("roomNum")
    if ((checkRoom) < 10) {
        alert("enter something");
     return;
    }
}
if(window.addEventListener)
{
   window.addEventListener("load", calculate_pricing, false);
}
else if (window.attachEvent)
{
   window.attachEvent("onload", calculate_pricing);
}

window.addEventListener("click", calculate_pricing, false);