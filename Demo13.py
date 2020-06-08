'''
相传古印度的一个宰相西萨-班达依尔发明了国际象棋。国王舍罕王玩得很开心，于是决定奖励这个宰相，问他有什么
要求。宰相没有向国王要求金银珠宝，而是提出了以下要求：请在棋盘的第1个格子里放上1颗麦粒，在第2个格子里放
上2颗麦粒，在第3个格子里放上4颗麦粒，依次类推，每个格子放的麦粒数都是前一个格子里放的麦粒数的2倍，直到
放完64个格子为止。国王一听，认为这是区区赏金，微不足道，于是满口答应。
请你编程序计算：
国王要向宰相奖励多少颗麦粒？
111麦粒约重50毫克。全部麦粒共重多少吨？
在标准11人足球场（尺寸是68米 X 105米，面积是7140平方米）上平铺全部麦粒，小麦的高度是多少米？假设一斤（500克）面的体积约为550550毫升。111升等于1立方分米，1立方米等于1000立方分米。
注意：
由于数量巨大，要使用浮点数来存储麦粒总数、吨数和高度。
'''
num =1
sum = 1
for i in range(1, 64):
    num*=2
    sum+=num
print(sum)

weight = sum*50/1e9
print("%.2ft" %weight)

height = sum *50/1000 / 500 /1e6/7140*550
print("%.2fm" %height)

