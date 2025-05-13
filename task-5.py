import random
deckOfCards=[2,3,4,5,6,7,8,9,'T','J','Q','K','A']
suit=['h','s','c','d']
def deck():
  deck_list=[]
  for i in deckOfCards:
    for j in suit:
      deck_list.append(j+str(i))
  return deck_list
cards=deck()
magic_card=random.choice(cards)
print("Guess the card in the format: suit+rank (e.g., 'h2', 'sT', etc.)")
for i in range(3):
  guess=input(f"Attempt{i+1}/3 Guess the card: ").lower()
  if guess==magic_card.lower():
    print("You got it right! ")
    break
  else:
    print("Try again")
    if guess[0] == magic_card[0]:
      print("The suit is correct!")
    elif guess[1] == magic_card[1]:
      print("The rank is correct!")
    else:
      print(f"Hint: The suit is",magic_card[0])
else:
  print("Oops! You're out of luck! The correct card was: ",magic_card)