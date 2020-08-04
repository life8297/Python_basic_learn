x = 5
while x < 10: # 當x < 10 時進入loop
	print('x < 10')
	print('我還困在框框裡')
	print('x = ', x)
	x = x + 1
print('已逃出迴圈')

x = 5
while True: # 強制進入loop
	print('x < 10')
	print('我還困在框框裡')
	print('x = ', x)
	break # 無限迴圈需用break停止
print('已逃出迴圈')