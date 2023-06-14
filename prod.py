prod = []
while True:
	n = input('product name:')
	if n == 'q':
		break
	pri = input('price:')
	pri = int(pri)
	#p = [n ,pri] # p = [n, pri] = p.append(n) p.append(pri)
	prod.append([n ,pri]) # ([m, pri]) = (p) = [n, pri] 
print(prod)

for i in prod:
	print(i[0], 'price is', i[1])


with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('product, price\n')
	for i in prod:
		f.write(i[0] + ',' + str(i[1]) + '\n')