########################## Hafiz Abdulmanan ############################

########################## Github Api Scraping Task ####################

from github import Github
import json

g = Github("Acess_Token") # I am hiding my access token will present if you want demo


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
with open('json_1_github_data.json', 'w') as out:
    out.write(json_string)


print("Total users :", count)
