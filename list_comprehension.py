import random
under_10 = [ x for x in range(10)]
print('under_10:' + str(under_10))

odds = [ x for x in range(10) if x%2 == 1]
print('odds: ' + str(odds))


names = ['Cosmos', 'Pedro', 'Anu', 'Ray']
idx = [k for k, v in enumerate(names) if v == 'Anu']
print('index = ' + str(idx[0]))

letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)