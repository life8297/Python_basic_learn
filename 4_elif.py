age = input('請輸入年齡: ') # input回傳為'字串'，字串無法與整數做比較
age = int(age) # 將age('字串')轉換為age(整數)
if age < 13: # True: 進入此小框；False: 跳過此小框
	print('就讀國小: ?')
elif age >= 13 and age < 18:  # elif: else if, 另外如果
	print('就讀國中: ?')
elif age >= 18 and age < 22:
	print('就讀大學: ?')
else:
	print('在哪間公司就業: ?')
# 上面4路中會進入1路