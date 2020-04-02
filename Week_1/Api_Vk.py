import requests
import datetime


now = datetime.datetime.now()


def calc_age(uid):
    user = requests.get(f"https://api.vk.com/method/users.get?user_ids={uid}&fields=id&access_token=64b0b1c664b0"
                        "b1c664b0b1c6d264c005af664b064b0b1c63a3468c68c4eda1487685d66&v=5.122")
    id = user.json()['response'][0]['id']
    friends = requests.get(f"https://api.vk.com/method/friends.get?user_id={id}&fields=bdate&access_token=64b0b1c664"
                           "b0b1c664b0b1c6d264c005af664b064b0b1c63a3468c68c4eda1487685d66&v=5.122")
    list_of_friends = friends.json()['response']['items']
    bdays = {}
    for i in list_of_friends:
        if 'bdate' in i:
            bday = i['bdate']
            if len(bday) > 5:
                bday = list(bday.split('.'))
                year = int(now.year) - int(bday[2])
                if year not in bdays:
                    bdays[year] = 1
                else:
                    bdays[year] += 1
    return sorted(bdays.items(), key=lambda v: (v[1], -v[0]), reverse=True)


if __name__ == '__main__':
    res = calc_age('166936349')
    print(res)
