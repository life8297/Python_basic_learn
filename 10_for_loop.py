# for loop: 把清單中的東西一個一個拿出來
# 清單中有多少資料就for迴圈幾次
cars = ['Tesla', 'Ford', 'Audi', 'Benz']
for car in cars: # car為短暫稱呼當下內容之變數
	print(car)

# 字串當清單
name = 'Game of throne' #將字串中每個字母個別取出
print(len(name))
for n in name:
	print(n)

print('m' in name) # 檢內容是否存在
print('me' in name) 
print('y' in name)