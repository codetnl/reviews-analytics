data = []
count = 0 #計數器
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count + 1 = 1
		if count % 1000 == 0:  #如果與1000除餘數是0
			print(len(data))
print(len(data))	#印出資料data裡有幾筆

print(data[0])     #印出第一筆資料