planets = {"Mercury": ["The smallest planet, nearest the sun", False, 0],
           "Venus": ["Venus takes 243 days to rotate", False, 0],
           "Earth": ["The only planet known to have native life", False, 1],
           "Mars": ["The red planet is the second smallest planet", False, 2],
           "Jupiter": ["The largest planet, Jupiter is a gas giant", True, 67],
           "Saturn": ["The second largest planet is a gas giant", True, 62],
           "Uranus": ["An ice giant with a ring system", True, 27],
           "Neptune": ["An ice giant and farthest from the sun", True, 14],
           "Pluto": ["The former ninth planet is now classified as a dwarf planet", False, 5]
           }

while True:
  query = input("Which planet would you like information on? ")
  if query in planets.keys():
    print(planets[query])
  else:
    print("No data available, sorry!")