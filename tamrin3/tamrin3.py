import random
words=['boo','tree','python','bag', 'umbrella', 'clock', 'engineer', 'toothpate', 'shirmoz']
word=random.choice(words)
chance=10
right_word=[]

word_cuont=[]
for c in word:
    if c not in word_cuont:
         word_cuont.append(c)
        
print('_ '*len(word))
while chance > 0:
    usercharacter=input('guess:').lower()
    if usercharacter in word:
        right_word.append(usercharacter)
        for i in range(len(word)):
            if word[i] in right_word:
                print(word[i],end=' ')
            else:
                print('_',end=' ')
    if  word_cuont==right_word:
        print('\n you win')
        break
    else:
        chance-=1
















