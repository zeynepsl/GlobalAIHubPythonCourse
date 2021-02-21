#hangman game
import random

# seçmek için kullandığımız kitaplık
name = input("What is your name? ")
print("Good Luck ! ", name)

words = ['computer', 'engineering', 'data', 'science',
         'artificial', 'intelligence', 'global', 'hub',
         'software', 'hardware', 'python', 'programming']

# fonksiyon rasgele bir deger seciyor
word = random.choice(words)
print("Guess the characters")
guesses = ''

# burada herhangi bir sayıda dönüş kullanılabilir
turns = 10
while turns > 0:
    # bir kullanıcının kaç kez başarısız olduğunu sayar
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        # Başarısızlık 0 ise kullanıcı oyunu kazanır
        print("You Win")

        print("The word is: ", word)
        break
        
    # kullanıcı yanlış alfabeyi girdiyse
    # kullanıcıdan başka bir alfabe girmesini isteyecek
    guess = input("guess a character:")
    guesses += guess

    # kelimedeki karakterle girişi kontrol edelim
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")