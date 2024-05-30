planets = {"Mercury": "The smallest planet, nearest the sun",
           "Venus": "Venus takes 243 days to rotate",
           "Earth": "The only planet known to have native life",
           "Mars": "The red planet is the second smallest planet",
           "Jupiter": "The largest planet, Jupiter is a gas giant",
           "Saturn": "The second largest planet is a gas giant",
           "Uranus": "An ice giant with a ring system",
           "Neptune": "An ice giant and farthest from the sun",
           "Pluto": "The former ninth planet is now classified as a dwarf planet"
           }

while True:
  query = input("Which planet would you like information on? ")
  print(planets[query])