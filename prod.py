prod = []
while True:
	n = input('product name:')
	if n == 'q':
		break
	pri = input('price:')
	p = [n ,pri] # p = [n, pri] = p.append(n) p.append(pri)
	prod.append([n ,pri]) # ([m, pri]) = (p) = [n, pri] 
print(prod)

for i in prod:
	print(i[0], 'price is', i[1])