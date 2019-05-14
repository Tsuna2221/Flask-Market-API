import random, string, requests

txt = open('names.txt', 'r')
post_url = "http://127.0.0.1:5000/customer/insert"
names_list = []

for name in txt:
    names_list.append(name.strip())

def storeCustomers():
    print("Insert Length..."); length = input()

    for i in range(0, int(length)):
        rand_name = names_list[random.randint(0, len(names_list))].strip()
        rand_number = ''.join(random.SystemRandom().choice(string.digits) for _ in range(3))

        email = rand_name + rand_number + "@gmail.com"

        obj = {
            "first_name": names_list[random.randint(0, len(names_list))],
            "last_name": names_list[random.randint(0, len(names_list))],
            "email": email,
            "password": "yuio9012",
            "confirm_password": "yuio9012"
        }

        res = requests.post(post_url, json=obj)
        print(res.text)

storeCustomers()

txt.close()