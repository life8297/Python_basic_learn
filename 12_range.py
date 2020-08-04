# range 範圍
# python內建功能: 清單產生器

range(5) # [0, 1, 2, 3, 4]
range(3) # [0, 1, 2]
# 起始值未設即為0
range(1, 5) # [1, 2, 3, 4]
range(5, 10) # [5, 6, 8, 9]
# 起始值包含, 終值不包含
range(1, 10, 2) # [1, 3, 5, 7, 9]
range(2, 50, 10) # [2, 12, 22, 32, 42]
range(10, 1, -2) # [10, 8, 6, 4, 2]
# range(起始值, 結尾值, 遞增值)
# 遞增值預設為1

import random
for i in range(5): # 把清單中的東西拿出來, range通常與for搭被使用
	print('hi') # for搭配range通常用來重複執行固定的次數, 此處即為列印hi 5次
for i in range(100): # 把清單中的東西拿出來, range通常與for搭被使用
	r = random.randint(1, 1000) # 產生5個隨機整數
	print('這是第', i + 1, '個隨機數: ', r)
