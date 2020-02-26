// Function for finding the book price total

function sumPrices()
{
   var allPrices;
   var priceTotal = 0;
   var index;

   if(document.getElementById("btn_buy").checked)
   {
      console.log("Buy button currently checked");
      allPrices = document.getElementsByClassName("newBuy");
   }
   else if (document.getElementById("btn_rent").checked)
   {
      console.log("Rent button currently checked");
      allPrices = document.getElementsByClassName("newRent");
   }

   for(index=0; index < allPrices.length; index++)
   {
      var text = allPrices[index].innerText;
      var matches = text.match(/(\d+)/);

      if(matches)
      {
         var num = parseInt(matches[0]);
         priceTotal = priceTotal + num;
      }
   }
   document.getElementById("totalPrice").innerHTML = priceTotal;
   return;
}

if(window.addEventListener)
{
   window.addEventListener("load", sumPrices, false);
}
else if (window.attachEvent)
{
   window.attachEvent("onload", sumPrices);
}