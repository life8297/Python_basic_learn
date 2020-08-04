# function 函式/功能: 用於收納程式碼, 是個功能

def wash(dry=False, water=8): # 定義function, 不執行
	print('洗衣機啟動')
	print('加水', water, '分滿')
	print('加洗衣精')
	if dry:
		print('烘衣')

wash(True, 10)
wash(water=10)

def add(x=1, y=2): # x=1, y=2為預設值, 參數撰寫時不用空格
	print(x + y)

add() # 3, 使用預設值
add(5, 20) # 25
add(5) # 7, y使用預設值
add(y=5) # 6, 指定參數

def new(x, y):
	return x + y

result = new(3, 4)
print(result)

def average(numbers):
	return sum(numbers) / len(numbers)
print(average([1, 2, 3]))