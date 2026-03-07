# dictionary  in python is collection key value pair  it is unorder and mutable
Room_boys  = {
    "mahesh_b" : "03-05-2007",
    "mahesh_s" : "01-01-2007",
    "mahesh_c" : "05-06-2007"
}
print(Room_boys)
meaning = {"bat": "use to hit",
           "boll" :"use to trow",
           "wicket":"take to wicket"
           }
# ascessing dictionary elements
print(meaning.get("bat"))
# important note keep in mind
print(meaning.get("boll"))
print(meaning.get("bat"))
print(meaning.get("wicket"))
print(meaning.get("mahesh_b"))
print(meaning.get("mahesh_s","not exist in the meanning"))
print(meaning.get("mahesh_c","not exist in the meanning"))
print(meaning.get("mahesh_c","not exist"))
# we want to add the another into the dictionary use adding also using this conndition
meaning["glouse"] = " is use to the wicket keeping because away from the pain " # imp remeber this one
print(meaning)
meaning["boll"] = "use to catch"
print(meaning)
meaning.pop("boll")
print(meaning)
print(meaning.keys())
print(meaning.values())
meaning.update({"glouse":"use to catch"})
print(len(meaning))
item1 = {
    "name" : "sugar",
    "price" : 50,
    "wieght" : "2"
}
item2 = {
    "name" : "tea powder",
    "price" : 599,
    "wieght" : "12"



}
item3 = {
    "name" : "rave",
    "price" : 5097,
    "wieght" : "22"}
items = [item1, item2, item3]
print(items)
print(f" total wierht: {item1["wieght"] + item2["wieght"] + item3["wieght"] }")


# this is all about the dictionary
#home work
karnataka_cities = {
    "yadagir" : "pannier",
    "mysures" : "jolada rotti",
    "bidar" : "chaha",
    "chittar durga" : "dosa",
    "raichur" : "kanda"
    }
print(karnataka_cities)
karnataka_cities["belagavi"] = "anna"
print(karnataka_cities)
karnataka_cities["mysures"] = "anna"
print(karnataka_cities)
print(karnataka_cities.get("mysures"))
print(karnataka_cities.get("belagavi"))
print(karnataka_cities.keys())
print(karnataka_cities.values())




