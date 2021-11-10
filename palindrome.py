
#AUTHOR:FELIPE MOLANO



#this function receives a word or prhase and determines if it is a palindrome
def isPalin(word):

    print("u have entered the word: ", word)
    word = word.replace(" ","")
    word = word.lower()
    print("your fixed word is : ", word)
    print("it has  ", len(word), "characters ")
    lista0 = word[0:]
    lista00= word[::-1]
    if lista0 == lista00:
        print(" ------- the word is a palindrome !")
    else:
        print(" ------- the word is not a palindrome !")
        
    
    



#test
isPalin("dabale Arroz a la zoRra el abad")
isPalin("somos")