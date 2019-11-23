lists = [3, 5, 7, 1, 10, 8, 9, 15];
tmp=0

'''
	SORTING PROCESS IS HERE
'''
for i in range(len(lists)):
	for y in range(0, len(lists) -1):
		if lists[y] > lists[y+1]:
			tmp = lists[y]
			lists[y] = lists[y+1]
			lists[y+1] = tmp


def prinList():
	for i in range(0,len(lists)):
		print("%d " % lists[i], end='')


prinList()
