# if架構
rain = input('今天有沒有下雨?(有/無): ')
if rain == '有': # True: 進入小框；False: 不進入小框
	print('記得帶傘, 帶零食回家, 追劇時間!')
	movie = input('想看哪部?: ')
	print(movie, '我知道, 超好看的!!')
if rain == '無':
	print('記得外出運動...')
