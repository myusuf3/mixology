import request 
from bs4 import BeautifulSoup



def find_measures(bsoup, id):
  measures = bsoup.find_all('div', class_="recipeMeasure")
  return [ parse_measures(m, id) for m in measures ]

def find_directions(bsoup, id):
  directions = bsoup.find_all('div', class="recipeDirection")
  return [ parse_measures(m, id) for m in measures ]



def parse_measures(measure_info,id ):
  contents = measure_info.contents
  return ( id, contents[0], contents[1].text )

def parse_directions(direction_info, id):
  contents = direction_info.contents
  if contents[0] in ("Build", "Serve in a ", "Muddle/shake"):
    return None
  elif contents[0] == "Fill with":
    return "Ice"
  elif contents[0] == "Top with":
    return contents[1].text
  elif contents[0] == "Shake in ":
    return "Shake in iced cocktail shaker & strain"
  elif contents[0] == "Stir in ":
    return "Stir in mixing glass with ice & strain" 
  elif contents[0] == "Add ":
    return contents[1].text
  elif contents[0] == "Muddle/Shake"


def get_drinks():

