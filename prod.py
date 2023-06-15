import os #operating system
def read_file(filename):
	prod = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'product, price' in line:
				continue # 進行檔案讀取後跳過if 條件下一迴的意思
			name, price = line.strip().split(',') #用.split(',')做分割, 用strip()去除換行符號
			prod.append([name, price])
		print(prod)
	return prod

#使用者輸入商品價格
def user_input(prod):
	while True:
		n = input('product name:')
		if n == 'q':
			break
		pri = input('price:')
		pri = int(pri)
		#p = [n, pri] # p = [n, pri] = p.append(n) p.append(pri)
		prod.append([n ,pri]) # ([n, pri]) = (p) = [n, pri] 
	print(prod)
	return prod

def print_products(prod):
	# 印出所有購買記錄
	for i in prod:
		print(i[0], 'price is', i[1])

def write_file(filename, prod):
	#寫入檔案
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('product, price\n')
		for i in prod:
			f.write(i[0] + ',' + str(i[1]) + '\n')

def main():
	filename = 'product.csv'
	if os.path.isfile(filename): # os.path.isfile()檢查有無檔案 #讀取檔案
		prod = read_file(filename)
	else:
		print('there is no file')
	prod = user_input(prod)
	print_products(prod)
	write_file('product.csv', prod)

main()