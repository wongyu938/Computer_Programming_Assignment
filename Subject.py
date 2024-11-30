import csv
subjects = []
def Extract_Subject():  #과목 이름들을 리스트에 넣는 함수
    f = open('20231231.csv')
    reader = csv.reader(f)
    for row in reader:
        if row[1] not in subjects and row[1] != '유형':
            subjects.append(row[1])
    f.close()

def Print_Subject(): #과목을 출력하는 함수
    Extract_Subject()
    for i in range(len(subjects)):
        print(f"{i+1}.{subjects[i]}",end=" ")
    Enter_Subject = input("어떤 과목을 선택하시겠습니까?")
    while True:
        if Enter_Subject not in subjects:
            Enter_Subject = input("알맞은 과목 명을 입력하세요.")
        else:
            break
        
    return Enter_Subject

def Extract_data_man(subject):
    f = open('20231231.csv')
    reader = csv.reader(f)
    man_data = {}
    for row in reader:
        if row[1]==subject:
            man_data[int(row[2].strip())]=int(row[3].strip())
    return man_data

def Extract_data_woman(subject):
    f = open('20231231.csv')
    reader = csv.reader(f)
    woman_data = {}
    for row in reader:
        if row[1]==subject:
            woman_data[int(row[2].strip())]=int(row[4].strip())
    return woman_data
    

