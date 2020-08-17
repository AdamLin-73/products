print('輸入完成請按q')
products = []

while  True:
	name = input('請輸入買家名稱: ')
	if name == 'q':
		break
	account = input('請輸入買家帳號: ')
	store = input('請輸入超商: ')
	goods = input('請輸入商品: ')
	p = int(input('請輸入商品成交價格: '))
	c = int(input('請輸入成本: '))
	s = int(input('請輸入運費: '))
	f = int(input('請輸入手續費: '))
	profit =int(p - c -s -f)
	credit_card = input('請輸入信用卡: ')
	p = str(p)
	c = str(c)
	s = str(s)
	f = str(f)
	profit = str (profit)
	products.append([name, account, store, goods, p, c, s, f, credit_card, profit])
print(products)

for p in products:
	print(p[0], '買家帳號是', p[1], '取貨超商是', p[2], '購買商品', p[3], '的價格是', p[4], '成本是', p[5], '運費', p[6], '手續費', p[7], 'profit', p[9], 'credit_card', p[8])

with open('products_sell.txt', 'w') as f:
	for p in products:
	#	f.write(p[0] + '買家帳號是' + p[1] + '取貨超商是' + p[2] + '購買商品' + p[3] + '的價格是' + p[4] + '成本是' + p[5] + '運費' + p[6] + '手續費' + p[7] + 'profit'+ p[9] + 'credit_card' + p[8] +'\n')
		f.write(p[0] + ' 買家帳號是: ' + p[1] + ' 取貨超商是: ' + p[2] + ' 購買商品: ' + p[3] + ' 的價格是 ' + p[4] + ' 成本是 ' + p[5] + ' 運費: ' + p[6] + ' 手續費 : ' + p[7] + ' profit: '+ p[9] + ' credit_card: ' + p[8] +'\n')