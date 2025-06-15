# Write code below 💖
guess = 0
tries = 0
while guess != 6 and tries < 3:
  guess = int(input('Guess the number: '))
  tries = tries + 1
  if guess != 6 and tries < 3:
    print('Keep trying!') 
  elif guess !=6 and tries >=3:
    print('You tried too many times')
  else:
    print('You got it!') 
