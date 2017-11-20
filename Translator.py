# By Shane Cheek

"""The rules (I'm making this up as I go):

1. Get an input from the user
2. Words that start with a consonant - go to the first vowel and take everything before that vowel and place it at the end of the word. Example: That == atth
3. If the word starts with a vowel - go to the next vowel and take everything before that vowel and place it at the end of the word. Example: Anaconda == acondaan
4. Add "yay" or "ay" to the end of every word. Using the two above examples: atth == atthyay & acondaan == acondaanyay
5. You have to have a print to screen and a text to speech output
6. You cannot use modules to solve steps 1 - 4, but you can use on for step 5"""

# user input
sentence = input("Enter your phrase: ")

# creat an empty list for the reconfigured words
pigout = []

# split the sentence into a list of words
words = sentence.split()

#loop through each word. execute steps 3 & 4
vowels = tuple("aeiouAEIOU")

# If the word starts with a vowel, find the next vowel
for x in words:
    if len(x) == 1:
        pigout += x + "ay "
    elif x.startswith(vowels):
        for t in range(0,len(x)):
            if x[t] in vowels:
                pigout += ((x[t:]) + (x[-1:t]) + "ay ")
                break
    else:
        for t in range(1,len(x)):
            if x[t] in vowels:
                pigout += ((x[t:]) + (x[0:t]) + "ay ")
                break

# to remove punctuations
punctuations = "!()-[]{};:'\"\,<>./?@#$%^&*_~"
pigoutnopunct = []

for p in pigout:
    if p not in punctuations:
        pigoutnopunct += p

print(" ".join(pigoutnopunct))

