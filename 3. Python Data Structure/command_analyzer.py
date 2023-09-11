import csv

def getKey(item):       # 정렬을 위한 함수 
    return item[1]      # 신경 쓸 필요 없음

command_data = []       #파일 읽어오기
with open("command_data.csv", "r", encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',' , quotechar='"' )
    for row in spamreader:
        command_data.append(row)


command_conuter = {}                # dict 생성, 아이디를 key값,
for data in command_data:
    if data[1] in command_conuter.keys():
        command_conuter[data[1]] += 1
    else:
        command_conuter[data[1]] = 1
# print(command_conuter)

dictlist = []
for key, value in command_conuter.items():
    temp = [key, value]
    dictlist.append(temp)
# print(dictlist)
sorted_dict = sorted(dictlist, key = getKey, reverse = True)
print(sorted_dict[:100])
