import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

nouns = ["kitty", "dime-bag", "plumper", "lamp shade", "rabbit"]
adjectives = ["curt", "toasty", "waxed", "horny", "hungry", "embossed"]
#ask about flavours
# loop through questions asking one at a time --> input response in new dictionary 

def is_valid(response):
  if (response == 't' or response == 'true' or response == 'y'): 
    return True
  elif (response == 'false' or response == 'f' or response == 'n'):
    return False
  else:
    return None

def customer_tastes(questionsToAsk):
  answers = {}
  for question in questionsToAsk:
    answer = None
    while is_valid(answer) == None:
      answer = input(questionsToAsk[question] + ' ')
      if is_valid(answer) == None:
        print('it\'s a ye or ne question')
      else:
        answers[question] = is_valid(answer)
  return answers

def drink_constructor(cust_prefs):
  print(cust_prefs)
  drink = ""
  counter = 0
  for cus_pref in cust_prefs:
    counter += 1
    if cust_prefs[cus_pref] == True:
      drink += (random.choice(ingredients[cus_pref]))
    if counter == len(cust_prefs):
      drink += "."
    else:
      drink += ", "
  drink_name = random.choice(adjectives) + " " + random.choice(nouns)
  print("your " + drink_name.title() + " is made up of a: " + drink)

if __name__ == '__main__':
  keep_m_coming = True
  while keep_m_coming:
    responses = customer_tastes(questions)
    drink_constructor(responses)
    inputValue = input("would you like another drink?")
    if inputValue == "yes" or inputValue == "y":
      keep_m_coming = True
    else:
      print("goodbye then!")
      keep_m_coming = False