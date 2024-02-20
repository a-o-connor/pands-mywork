#dict = {
#"key":"item"
# }

#want to store details about a car

car = {
    "make":"ford",
    "model":"mondeo",
    "year":2006,
    "owner":{
        "name":"Andrew",
        "number":1123
    }
}

#print(car["owner"]["name"]) 

#print(car["make"])

# print(car["owner"].get("names"))
# print(car["owner"].get("name"))


for key in car:
    print(key, "has a value of", car[key])
