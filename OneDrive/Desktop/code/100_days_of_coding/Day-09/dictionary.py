capitals={
  "france":"Paris",
  "germeny":"Berlin",
}

travel_log={
  "france":{
    "cities_visited":["Paris", "Lille", "Oijon"],
    "total_visits":12
  },
  "Germeny":{
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
    "total_visits":15
  }
}

print(travel_log["Germeny"]["cities_visited"])
print(travel_log["france"])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

