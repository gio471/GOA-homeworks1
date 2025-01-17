#https://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python:
def lowercase_count(strng):
    counter = 0
    for i in strng:
        if i.islower():
            counter += 1
            
    return counter

#https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python:
def capitals(word):
    random = []  #შევქმენი ცარიელი სია
    for i in range(len(word)):  #for ციკლის მეშვეობით word-ის სიგრძიე რამდენიც იქნება იმდენჯერ განმეორდება ციკლი
        if word[i].isupper():   #თუ word-ის ინდექსი არის upper-ი მაშინ ჩაემატება ის ინდექსი სიაში
            random.append(i)    
    return random
