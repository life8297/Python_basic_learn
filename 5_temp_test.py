# 溫度轉換練習
# 攝氏('C)轉換成華氏('F)
# 讓使用者輸入攝氏, 然後印出華氏
temp_c = input("攝氏溫度為:")
temp_c = float(temp_c) # 溫度可能為小數
temp_f = temp_c * 9 / 5 + 32 # 運算中先*/後+-
print('華氏溫度為: ', temp_f)