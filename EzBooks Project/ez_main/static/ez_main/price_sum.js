function calculate_pricing()
{
   var buyButton  = document.getElementsByClassName('buy');  // Array of all the buy buttons
   var rentButton = document.getElementsByClassName('rent'); // Array of all the rent buttons
   var newButton  = document.getElementsByClassName('new');  // Array of all the new buttons
   var usedButton = document.getElementsByClassName('used'); // Array of all the used buttons

   var index;
   var length = buyButton.length;
   var text;
   var matches;
   var priceTotal = 0;

   var newPrice;  // Array of only new prices
   var usedPrice; // Array of only used prices

   for(index = 0; index < length; index++)
   {
      if(buyButton[index].checked)
      {
         newPrice = document.getElementsByClassName('newBuy');
         usedPrice = document.getElementsByClassName('usedBuy');  
      }
      else if(rentButton[index].checked)
      {
         newPrice = document.getElementsByClassName('newRent');
         usedPrice = document.getElementsByClassName('usedRent'); 
      }

      // Get the correct price (new or used)
      if(newButton[index].checked)
      {
         text = newPrice[index].innerText;
      }
      else if(usedButton[index].checked)
      {
         text = usedPrice[index].innerText;
      }

      // Get the price as a number
      matches = text.match(/(\d+)/);

      if(matches)
      {
         var num = parseInt(matches[0]);
         priceTotal = priceTotal + num;
      }
   }

   var taxAmount       = (priceTotal * .06);
   var fixedTaxAmount  = taxAmount.toFixed(2);
   var grandTotal      = priceTotal + taxAmount;
   var fixedGrandTotal = grandTotal.toFixed(2);

   document.getElementById("total_price").innerHTML = "$" + priceTotal;
   document.getElementById("tax_amount").innerHTML  = "$" + fixedTaxAmount;
   document.getElementById("grand_total").innerHTML = "$" + fixedGrandTotal;
   return;

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