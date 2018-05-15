# _*_ coding: utf-8 _*_


from itertools import combinations

def guessName(ws,num):
	return_v=[]
	for i in range(num):
		return_v.append('a'+str(i))

	for x in list(combinations(words, num)):
		return_v = x
		print '-'.join(return_v)

# words = ['爱','桥','凉','笔','大','爱']

words = ['天','对','说','我','空','睛']

guessName(words,2)


