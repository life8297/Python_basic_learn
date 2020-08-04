# 讀取檔案
# 開啟food.txt並做讀取('r'ead)，並當作為變數f
# 讀取為'r'ead; 寫入為'w'rite
data = []
with open('food.txt', 'r') as f: 
	for line in f: # 讀取f中的資料, 會以每行資料呈現, 與line無關(可變更變數命名)
		data.append(line) 
print(data) # 記事本中換行會記錄/n

# 去除/n
n_data = []
with open('food.txt', 'r') as file: 
	for line in file: # 讀取f中的資料, 會以每行資料呈現, 與line無關(可變更變數命名)
		n_data.append(line.strip()) # strip針對字串去除空格、換行(/n)符號
print(n_data)

# with的解釋
# 檔案讀取時需open, 用完則需close, 但如檔案未close, 則會使此檔案時被占用
# with功能在於: 離開with區塊時, 會自動close被open的檔案