prod = []

#讀取檔案
with open('product.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'product, price' in line:
			continue # 進行檔案讀取後跳過if 條件下一迴的意思
		name, price = line.strip().split(',') #用.split(',')做分割, 用strip()去除換行符號
		prod.append([name, price])
print(prod)




while True:
	n = input('product name:')
	if n == 'q':
		break
	pri = input('price:')
	pri = int(pri)
	#p = [n ,pri] # p = [n, pri] = p.append(n) p.append(pri)
	prod.append([n ,pri]) # ([m, pri]) = (p) = [n, pri] 
print(prod)

# 印出所有購買記錄
for i in prod:
	print(i[0], 'price is', i[1])

#寫入檔案
with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('product, price\n')
	for i in prod:
		f.write(i[0] + ',' + str(i[1]) + '\n')