########################## Hafiz Abdulmanan ############################

########################## Github Api Scraping Task (Programming langueges version)####################

from github import Github
import json

g = Github("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")


data = {
    'user name':str,
    'full name':str,
    'email':str
}
all_data = list()

count=0
for users in g.search_users(query="repos:>=50 location:pakistan"):
    #print(users.name , " " , users.email, " ")
    data['user name'] = users.login
    data['full name'] = users.name
    data['email'] = users.email
    print(data)
    all_data.append(data.copy())
    count+=1

json_string = json.dumps(all_data,indent = 4)
with open('json_fist_github_data.json', 'w') as out:
    out.write(json_string)


print("Total result :", count)
