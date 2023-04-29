import random
print("> python sentences.py")


def get_determiner(quantity):
  
    
  #Return a randomly chosen determiner.

  if quantity == 1:
        words = ["a", "one", "the"]
  else:
        words = ["some", "many", "the"]

  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

def get_noun(quantity):
    #Return a randomly chosen noun.
  
  if quantity == 1:
    noun = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
  else:
    noun = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
  
  return random.choice(noun)  


def get_verb(quantity): 
  
  tense = ["past", "present", "future"]
  random.choice(tense)

  #Return a randomly chosen verb. If tense is "past",

  if tense == "past":
        verb = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
  elif tense == "present" and quantity == 1:
      verb = [ "drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
  elif tense == "future": 
      verb = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]
  else:
      verb = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]

    # Randomly choose and return a determiner.
  verb = random.choice(verb)
  return verb

#PART 1 ############
#def make_sentence(determiner,noun,verb):
    #Build and return a sentence with three words: a determiner, a noun, and a verb. The grammatical quantity of the determiner and noun will match the number in the quantity parameter. The grammatical quantity and tense of the verb will match the number and tense in the quantity and tense parameters.

  #full_sentence = (f" {determiner.capitalize()} {noun} {verb} ")
  #print(full_sentence)
#############

#Write the main function to call your make_sentence function six times and print six sentences with these characteristics:

def get_preposition():
    
  #Return a randomly chosen preposition from this list of prepositions:
  preposition = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
  
  return random.choice(preposition)

  
  #Build and return a prepositional phrase composed of three words: a preposition, a determiner, and a noun by calling the get_preposition, get_determiner, and get_noun functions.


def prep_phrase(preposition,determiner,noun,verb):

  prep_phrase = (f" {determiner.capitalize()} {noun} {verb} {preposition} {determiner} {noun} ")
  print (prep_phrase)

  # Return: a prepositional phrase.
def main():
  for i in range(0,5):
    quantity = random.randint(1,6)
    prep_phrase(get_preposition(),get_determiner(quantity),get_noun(quantity),get_verb(quantity))
  
main()

 