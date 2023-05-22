import random
WORDS=("python","jumble", "easy", "cornhub", "party", "float", "lightning mcqueen")
word=random.choice(WORDS)
correct=word
jumble=""
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
print("the jumble is",jumble)
guess=input("\nYour guess: ")
count=1
guess=guess.lower()
while (guess!=correct) and (guess != ""):
    print("Sorry bruh your not him.")
    guess=input("\nYour guess: ")
    count+=1
    guess=guess.lower()
if guess== correct:
    print ("goodjob thats fye")
