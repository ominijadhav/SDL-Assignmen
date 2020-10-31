# SDL-Assignmen

#omi.txt

#Mango Apple Gauva Papaya Mango Banana Pear Kiwi Strawbery Grapes Apple Apple Banana Mango Gauva pear 


#Source Code

file=input("\n Enter File name to open :-")
word=input("\n enter word to be searched :-")
k=0
with open(file,'r') as f:
    for line in f:
        words=line.split()
        for i in words:
            if(i==word):
                k=k+1
                
print("\n Occurance of word in a file :- ",k)                
print("\n Number of words in a file :- ",len(words))
           

#OUTPUT

Enter File name to open :-omi.txt

 enter word to be searched :-Apple

 Occurance of word in a file :-  3

 Number of words in a file :-  12


