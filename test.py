import requests

#Locatia API

BASE = "http://localhost:5000/"

data = [{"name": "Shining", "author": "Stephen King", "year": 1980},
        {"name": "1984", "author": "Jeorge Orwell", "year": 1949},
        {"name": "Metro 2033", "author": "Dmitriy Glukhovski", "year": 2005},
        {"name": "Dune", "author": "Frank Herbert", "year": 1968},
        {"name": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953},
        {"name": "Roadside Picnic", "author": "Strugatksy Brother", "year": 1972}]
## POST Request Test
for i in range(len(data)):
    response = requests.post(BASE + "book/" + str(i), data[i])
    print(response.json())
input()
## GET Request Test
for i in range(len(data)):
    response = requests.get(BASE + "book/" + str(i), data[i])
    print(response.json())
input()
##GET Request pe o carte anumita
response = requests.get(BASE + "book/1")
print(response.json())
input()
##PUT Request Test
response = requests.put(BASE + "book/7", {"name": "The Idiot", "author": "Fyodor Dostoyevsky", "year": 1868})
print(response.json())
##DELETE Request Test
response = requests.delete(BASE + "book/3")
print(response.json())
input()

