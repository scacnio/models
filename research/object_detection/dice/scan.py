import csv
f = open('train_labels.csv',encoding='UTF-8')
csv_read = csv.reader(f)
mistakes = []
line = 1
labels = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
for data in csv_read:
    #data = line.strip().split(",")
    if data[3] not in labels:
        mistakes.append((data[0], data[3], line))
    line += 1

for item in mistakes:
    print(item)

if len(mistakes)==1:
    print("No mistakes")
else:
    print(line)