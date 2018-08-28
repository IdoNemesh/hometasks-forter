## The Task: 
Create a JavaScript code that identifies if the user is logged in to it’s Google Account on it’s browser.
Few instructions:

* The code will run from the page https://www.macsales.com and no other page.
* You must use TamperMonkey/GreaseMonkey to 'inject' the JS code.
* The result should be displayed using `console.log`.
* You must not load any additional external libraries into MacSales’ page.
* Your JS code must not use visual indicators (icons / input field values / etc).
* BONUS: Detect if the user has a GooglePlus account / any other info.
* BONUS 2: Send the result to a `PasteBin`-like server that we can visit later.

## My solution:
So first, I downloaded GreaseMonkey to my Firefox.
Then, after a google search, I found an image url that will load only if the user is connected to a google account.
