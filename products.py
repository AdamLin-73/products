import os #operating system 

products = []
if os.path.isfile('products.csv'): #check folder if have products.csv file inside. 
	print('yeah! 找到檔案了')
 	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #keep going
			name, price = line.strip().split(',') #速寫
			products.append([name, price])
	print(products)

else:
	print('找不到檔案......')
#讀取

#		s = line.strip().split(',')
#		name = s[0]
#		price = s[1]
#		print(s)
while  True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
#	p = [] #三行寫法
#	p.append(name)
#	p.append(price)
#	products.append(p)
	
#	p = [name, price] ＃快速寫法
#	products.append(p)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')