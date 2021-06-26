import json

import os

sets_dir = "./Sets"

def main():
  # Grab json database file names
  dark_json = "Dark.json"
  light_json = "Light.json"
  sets_json  = "sets.json"

  with open(dark_json, "rt") as dark, open(light_json, "rt") as light, open(sets_json, "rt") as sets:
    # Read in data
    dark_cards  = json.loads(dark.read())["cards"]
    light_cards = json.loads(light.read())["cards"]
    sets_info   = json.loads(sets.read())

    if not os.path.exists(sets_dir):
      os.mkdir(sets_dir)
    
    for set in sets_info:
      dir = set["name"]
      path = os.path.join(sets_dir, dir)
      if not os.path.exists(path):
        os.mkdir(path)
      dark_path = os.path.join(path, "Dark")
      if not os.path.exists(dark_path):
        os.mkdir(dark_path)
      light_path = os.path.join(path, "Light")
      if not os.path.exists(light_path):
        os.mkdir(light_path)

    for card in dark_cards:
      save_card_json(sets_info, card, "Dark/")

    for card in light_cards:
      save_card_json(sets_info, card, "Light/")

def save_card_json(sets_info, card, dark_light):
    card_set = find_set(card, sets_info) + "/"
    path = os.path.join(sets_dir, card_set, dark_light)
    card_name = card["front"]["title"].replace("•","").replace(":"," -").replace("/","-")
    full_path = path + card_name + ".json"

    with open(full_path, "w") as file:
      file.write( "[" + json.dumps(card) + "]" )

def debug_print_path(parent, dir):
  print( parent + dir )

def find_set(card, sets_info):
  card_set = card["set"]
  if card_set.find("d") != -1:
    card_set.replace("d","")

  for set in sets_info:
    if set["id"] == card_set:
      return set["name"]

  print( card_set )
  return "Unsorted"

if __name__ == "__main__":
	main()