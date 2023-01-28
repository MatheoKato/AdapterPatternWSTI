# AdapterPatternWSTI
Task for passing the course Multi-layer systems

  We have two classes in our system. The first is GoldService that allows you to
reading the gold price from a given day (via the API provided by
NBP). The get_price method is used to retrieve the gold price and is the only one
public method in this class.
The second class is GoldPriceReader which reads price data from a file. She has a method
get_prices which loads data from a file and then returns a map where key is date and a
value is the price of gold.
As part of the task, you need to prepare an adapter that will allow you to use the class
GoldPriceReader the same way as GoldService .
Additional information
To get the gold price for the day, send an HTTP request to http://
api.nbp.pl/api/cenyzlota/{date} , where {date} is the date in the YYYY-MM-DD format.
More information can be found at http://api.nbp.pl/
Assumptions
1. Class and method names do not have to be exactly as described. They can be changed in purpose
match the standards of the language used.
2. The get_price method does not have to query the NBP API. Instead, for example,
display text in the console.
