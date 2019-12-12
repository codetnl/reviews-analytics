data = []
count = 0 #計數器
with open ('reviews.txt', 'r') as f:
	for line in f:  # f寫進line
		data.append(line) # line寫進data清單
		count += 1 #count + 1 = 1
		if count % 1000 == 0:  #如果與1000除餘數是0
			print(len(data))
print('檔案讀取玩了，總共有',len(data),'筆資料') 	#印出資料data裡有幾筆

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均長度是', sum_len/len(data))
