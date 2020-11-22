# def is_leap(year):
#     if year > 1919:

#         if (year % 4) == 0:
#             if (year % 100) == 0:
#                 if (year % 400) == 0:
#                     return bool(True)
#                 else:
#                     return bool(False)
#             else:
#                 return bool(True)
#         else:
#             return bool(False)
#     else:
#         if (year % 4) == 0:
#             return bool(True)
#         else:
#             return bool(False)
#
#
#
# def dayOfProgrammer(year):
#      if is_leap(year)  == True:
#          return("12.09.{0}".format(year))
#      else:
#          if year == 1918:
#              return '26.09.1918'
#          else:
#             return("13.09.{0}".format(year))
#
#
# print(dayOfProgrammer(2016))
# print(dayOfProgrammer(2017))
# print(dayOfProgrammer(1918))


# def max_array(a):
#     a.sort()
#     b = []
#     j = 0
#     for i in range(len(a)):
#         num = a[i]
#         #j = 0
#         for number in a[j:]:
#             #while number - num <= 1:
#                 #b[i][j] = a[j]
#                 print (number)
#         j += 1
#     return b
#
# max_array([1,22,3,4])
#
# def pickingNumbers(a):
#     len_array = []
#     a.sort()
#     for num in a:
#         len_array.append((array_maker(num, a)))
#     return max(len_array)
#
#
# def array_maker(num, array):
#     new_array = [num]
#     for number in array:
#         if number-num == 1 or number == num:
#             new_array.append(number)
#     #print (new_array)
#     return len(new_array)-1
#
#
# print(pickingNumbers([1,1,2,2,4,4,5,5,5]))
# print(pickingNumbers([4,6,5,3,3,1]))
# print(pickingNumbers([1,2,2,3,1,2]))
#
#

# def climbingLeaderboard(ranked, player):
#     a = []
#     for scores in player:
#         ranked.append(scores)
#         a.append(convert(ranking(ranked), scores))
#     return a
# def convert(list, scores):
#     it = iter(list)
#     rest_dict = dict(zip(it, it))
#     return rest_dict.get(scores)
#
# def ranking(ranked):
#     ranked.sort(reverse=True)
#     i = 0
#     rank = 1
#     ranked_player_score = []
#     for score in ranked:
#         if i == 0:
#             prev_score = ranked[i]
#         else:
#             prev_score = ranked[i-1]
#         if prev_score == score:
#             ranked_player_score.append(score)
#             ranked_player_score.append(rank)
#         else:
#             rank += 1
#             ranked_player_score.append(score)
#             ranked_player_score.append(rank)
#         i += 1
#     return ranked_player_score


# 1. FIND SMALLER_WORD
# 2. SORT


def wordtolist(word):
    a=[]
    for character in word:
        a.append(character)
    #print(a)
    return a

def bigger_word(word, index):
    charindex = word[-1 * index]
    stored_word = wordtolist(word)
    a = list(stored_word)
    i = index
    max_word = word
    while i < len(word):
         char_swap = word[-1*(i+1)]
         a[-1*index] = char_swap
         a[-1 * (i + 1)] = charindex
         #print(''.join(map(str, a)))
         if ''.join(map(str, a)) > ''.join(map(str, stored_word)):
            max_word = ''.join(map(str, a))
            break
         a = list(stored_word)
         i += 1
         print(i)
    #return {'big_word' : max_word,'position' : i}
    return(max_word)


def find_next_big_word(word) -> object:
    i = 1
    while i < len(word):
        biggest_word = bigger_word(word,i)
        if biggest_word != word:
            break
    return(biggest_word)


#print(find_next_big_word('bb'))
#print(find_next_big_word('ab'))
#print(find_next_big_word('bb'))
#print(find_next_big_word('ranopriyo'))
print(find_next_big_word('dhck'))
#print(find_next_big_word('dkhc'))
