'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):                         # define count_th function

    count = 0                               # set initial count to zero
    str1 = word                             # incoming word
    str2 = "th"                             # search string

    if len(str1) < 2:                       # if the length of the incoming word is less than 2 characters long
        return 0                            # return 0 (implying that nothing was found)

    n1 = len(str1)                          # get length of incoming word
    n2 = len(str2)                          # get length of search string

    if (n1 == 0 or n1 < n2):                # check to make sure incoming word is valid
        return 0;                           # if not, return 0

    if (str1[0 : n2] == str2):              # if the incoming word begins with a 'th'
        return count_th(str1[n2 - 1:]) + 1; # good, re-run the function to check for more occurances of the 'th' combination

    return count_th(str1[n2 - 1:]);         # position to start search moved to the right by 1

# print(count_th('oth_th8th'))                # print the number of 'th' occurances
