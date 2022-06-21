# Github-Scraping
My try to scrap users data using Github API 

# Version 1:
It will scrap users data 
- Users from Pakistan
- has repos greater than 50
- name user name email 

Data will be in json file (total enteries 1200)


# Version 2:
It also scraping the users programming languages used in his repos. But I have narrowed down searching criteria (to has repos greater than 600)

Actualy programming languages cannot be accessed directly from user information using Github API. So I have made my logic to get the programming languages used by the user in his repos.
It will iterate all over the repos of the user and get the unique programming languages it is using. 
For example if there are 1000 repos of a user it will iterate all over the repos and give the programming languages is these repos. That require a lot of time so thats why I have narrowed down the searching criteria.

(Total enteries to json file 4)

# Version 3:
By selemium scraping of github users information from github main page
scrape results are present in CSV file 
Users from Pkaitan has repos greater than 400
Total reults : 13
