products = []

while  True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
#	p = [] #三行寫法
#	p.append(name)
#	p.append(price)
#	products.append(p)
	
#	p = [name, price] ＃快速寫法
#	products.append(p)
	products.append([name, price])
print(products)
