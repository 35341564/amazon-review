data  = []
count = 0
with open('reviews.txt','r')as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢，總共有',len(data),"筆資料")
print(data[0])

wc = {} #word_count
for d in data:
    words = d.split(" ")
    for word in words:
        if word in wc:
            wc[word] += 1
        else: 
            wc[word] = 1

for word in wc:
    if wc[word] > 100:
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input('查啥字? : ')
    if word in wc:
        print(wc[word])
    else:
        print('no')





# print("留言平均長度為:",avg)

# new = []
# for d in data:
#     if len(d)<100:
#         new.append(d)
# print("一共有",len(new),"筆資料長度小於100")
# print(new[0])