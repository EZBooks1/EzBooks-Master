function calculate_pricing()
{
   var purchase_method; // Method for the purchase of the books (buy or rent)
   var allNew;          // Array of all the new prices
   var allUsed;         // Array of all the used prices
   var newButton  = document.getElementsByClassName('new');  // Array of all the new buttons
   var usedButton = document.getElementsByClassName('used'); // Array of all the used buttons
  
   // Get the purchase method as indicated by the button currently active
   if(document.getElementById("btn_buy").checked)
   {
      purchase_method = 'buy';
   }
   else if(document.getElementById("btn_rent").checked)
   {
      purchase_method = 'rent';
   }
   
   // Get the array of prices only for the needed purchase method (buy or rent)
   if(purchase_method == 'buy')
   {
      allNew = document.getElementsByClassName('newBuy');
      allUsed = document.getElementsByClassName('usedBuy');
   }
   else if(purchase_method == 'rent')
   {
      allNew = document.getElementsByClassName('newRent');
      allUsed = document.getElementsByClassName('usedRent');
   }

   var index;
   var length = allNew.length;
   var text;
   var matches;
   var priceTotal = 0;

   for(index = 0; index < length; index++)
   {
      // Get the correct price (new or used)
      if(newButton[index].checked)
      {
         text = allNew[index].innerText;
      }
      else if(usedButton[index].checked)
      {
         text = allUsed[index].innerText;
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