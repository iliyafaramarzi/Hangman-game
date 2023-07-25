import random
file = open('words.txt' , 'r')
#-------------------------------------------------------------#save words in a txt file 
words = []
for word in file.readlines():
    words.append(word.strip().lower())
#------------------------------------------------------------------#make a random number
random_number = random.randrange(0 , len(words))
#---------------------------------------------------------------------#print '_ ' for (words lenght) time
dynamic_word = ''
guess_word = words[random_number]
#for i in range(0 , len(guess_word)):
#    dynamic_word += '_ '
#-----------------------------------------------------------------------#hangman character 7 level
while True:

    hangman = ["""
    ------
    |     |
    |
    |
    |
    |
    |
    |
    ----------
    """
        ,
    """
    ------
    |     |
    |     0
    |
    |
    |
    |
    |
    ----------
    """
    ,
        
    """
    ------
    |     |
    |     0
    |    -+-
    |
    |
    |
    |
    ----------
    """
    ,
    """
    ------
    |     |
    |     0
    |   /-+-/
    |
    |
    |
    |
    ----------
    """
    ,
    """
    ------
    |     |
    |     0
    |   /-+-/
    |     |
    |     |
    |
    |
    ----------
    """
        ,
    """
    ------
    |     |
    |     0
    |   /-+-/
    |     |
    |     |
    |    | |
    |    | |
    -------""" ]
    break
#-----------------------------------------------------------#show some words 
word_list = []
for i in range(0 , len(guess_word)):
    word_list.append(guess_word[i])
random_number = 0
for i in range(0 , (len(guess_word) - len(guess_word) // 3)):
    random_number = random.randrange(0 , len(guess_word))
    word_list[random_number] = '_'

#------------------------------------------------------# orginal word list
orgina_word_list = []
for i in range(0 , len(guess_word)):
    orgina_word_list.append(guess_word[i])

#-----------------------------------------------------#strat game
dyna_num = 0
trys = 5
fales = 0

print('welcome to the Hangman game.Guess the word and win.I hope you enjoy...')

while '_' in word_list or trys != 0:
    if not '_' in word_list:
        break
    else:
        str_word_list = ''
        for i in word_list:
            str_word_list += ' ' + i + ' '
        
        print(hangman[fales])
        print('you can try %i more time.' % trys)
        print('the word is: %s' % str_word_list)

        enter_word = input('please enter a word:')
        if trys != 0:
            if len(enter_word) > 1 or len(enter_word) < 1:
                print('lenght error please enter one word.')
                continue

            else:

                if not '_' in word_list:
                    print('ohhhhh you wiiin')
                    break

                elif enter_word in orgina_word_list:
                    dyna_num = orgina_word_list.index(enter_word)
                    if orgina_word_list[dyna_num] != '_':
                        for i in range(0 , len(guess_word)):
                            if enter_word == guess_word[i] and word_list[i] != '_':
                                continue
                            elif enter_word == guess_word[i] and word_list[i] == '_':
                                word_list[i] = orgina_word_list[i]
                                continue

                    else:
                        word_list[dyna_num] = orgina_word_list[dyna_num]
                        continue


                else:
                    fales += 1
                    trys -= 1 
                    continue
        else:
            break

if trys == 0:
    print('ohhhhh you lose :(')
else:
    print('-------------------------------')
    print('you winnnnn :) and the word is %s' % guess_word)
