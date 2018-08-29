## The task 
Write a function countUniqueNames(billFirstName,billLastName,shipFirstName,shipLastName,billNameOnCard) that counts the number of unique names in a transaction.

billFirstName - the first name in the billing address form (could include middle names)
billLastName - the last name in the billing address form
shipFirstName - the first name in the shipping address form (could include middle names)
shipLastName - the last name in the shipping address form
billNameOnCard - the full name as it appears on the credit card.

You should be able to handle middle names, nicknames and editing typos:

countUniqueNames(“Deborah”,”Egli”,”Deborah”,”Egli”,”Deborah Egli”) returns 1

countUniqueNames(“Deborah”,”Egli”,”Debbie”,”Egli”,”Debbie Egli”) returns 1

countUniqueNames(“Deborah”,”Egni”,”Deborah”,”Egli”,”Deborah Egli”) returns 1

countUniqueNames(“Deborah S”,”Egli”,”Deborah”,”Egli”,”Egli Deborah”) returns 1

countUniqueNames(“Michele”,”Egli”,”Deborah”,”Egli”,”Michele Egli”) returns 2

The solution should contain unit tests that cover at least the above use cases.
