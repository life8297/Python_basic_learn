while True:
	mode = input('請輸入遊戲模式:')
	if mode == 'q':
		print('已關閉模式')
		break
	elif mode == '1':
		print('已啟動模式1')
	elif mode == '2':
		print('已啟動模式2')
	else:
		print('請輸入 q/1/2')