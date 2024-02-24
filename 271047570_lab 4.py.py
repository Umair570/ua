#                                                       "lab number 4"

#TASK 1

first_name=input("please enter a name")
last_name=input("please enter a name")
full_name=first_name +" "+ last_name

print(full_name)

#TASK 2

NAME=input("please enter a name")
length=len(NAME)
print(length)

if length%2==1 and length>3:
    print("accepted")
else:
    print("rejected")


#TASK 3
STRING=input("please enter a sentence")
vowel_a=(STRING.count("a"))
vowel_e=(STRING.count("e"))
vowel_i=(STRING.count("i"))
vowel_o=(STRING.count("o"))
vowel_u=(STRING.count("u"))
print("number of a:",vowel_a)
print("number of e:",vowel_e)
print("number of i:",vowel_i)
print("number of o:",vowel_o)
print("number of u:",vowel_u)

#TASK 4

STRING=input("please enter a sentence")

upper_case=(STRING.upper())
lower_case=(STRING.lower())
print(upper_case)
print(lower_case)


#TASK 5

sentence=input("please enter a sentence")
split_sentence=(sentence.split())
print(split_sentence)


#TASK 6
sentence=input("please enter sentence:").lower()
if sentence.count("sad")>0 or sentence.count("kill")>0 or sentence.count("die")>0:
    print("rejected")
else:
    print("accepted")
