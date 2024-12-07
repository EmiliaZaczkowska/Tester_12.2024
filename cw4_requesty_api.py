import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
# print(response)
if response.status_code == 200:
    print("jupii, strona jest ok")
    print("Dane uzytkownikow to: ", response.json())
else:
    print(f"ups cos poszlo nie tak, kod bledu to : {response.status_code}")