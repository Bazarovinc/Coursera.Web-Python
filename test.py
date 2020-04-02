import requests
import datetime

now = datetime.datetime.now()

def sort_age(list_of_bdays):
    for _ in range(len(list_of_bdays)):
        for i in range(1, len(list_of_bdays)):
            if list_of_bdays[i - 1][1] == list_of_bdays[i][1] and list_of_bdays[i - 1][0] > list_of_bdays[i][0]:
                list_of_bdays[i], list_of_bdays[i - 1] = list_of_bdays[i - 1], list_of_bdays[i]
            elif list_of_bdays[i - 1][1] < list_of_bdays[i][1]:
                list_of_bdays[i], list_of_bdays[i - 1] = list_of_bdays[i - 1], list_of_bdays[i]
    return list_of_bdays

r = requests.get("https://api.vk.com/method/friends.get?user_id=288752323&fields=bdate&access_token=64b0b1c664b0b1c664b0b1c6d264c005af664b064b0b1c63a3468c68c4eda1487685d66&v=5.122")
list_of_friends = r.json()['response']['items']
bdays = {}
for i in list_of_friends:
    if 'bdate' in i:
        bday = i['bdate']
        if len(bday) > 5:
            print(i)
            bday = list(bday.split('.'))
            year = int(now.year) - int(bday[2])
            if year not in bdays:
                bdays[year] = 1
            else:
                bdays[year] += 1

list_of_bdays = []
for k, v in bdays.items():
    l = [k, v]
    list_of_bdays.append(tuple(l))


print(sort_age(list_of_bdays))
print(bdays)

