# Stock_Trading_News_Alert

A Python program that send to your preferred phone number the last three articles from the company you want plus the percentage of the stock price change (drop or up)

First you can change at the top the company name to your preferred company
![Screenshot_104](https://user-images.githubusercontent.com/104036788/189950945-bf2f356a-2654-49e3-9227-ede2c74775a8.jpg)



Second you go to:
https://www.alphavantage.co/
and get your free API KEY so you can use it in the main.py

![Screenshot_105](https://user-images.githubusercontent.com/104036788/189949911-0d41e272-2d36-4822-9041-c9a3ddeadb46.jpg)

as you can see above, you should also go to :
https://newsapi.org/
and get your free API KEY 

and finally here:
https://www.twilio.com/
and create a free account so you can grab your free Twilio_SID and Twilio Auth Token to send SMS to your preferred number.


 * Get yesterday's closing stock price.
 * Get the day before yesterday's closing stock price
 * Use the News API to get articles related to the COMPANY_NAME
 * Create a new list of the first 3 article's headline and description
