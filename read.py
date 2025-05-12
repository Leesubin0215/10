import tkinter

root = tkinter.Tk()
 
file = open("test.txt","r",encoding='UTF-8') #파일명을 지정해서 파일을 연다

strFile = file.readline()
root.geometry(strFile[:-1])

strFile = file.readline()
root.title(strFile[:-1])

#for strList in fileList : #리스트 안에 있는 값을 가져온다
   # print(strList, end="") #리스트 값을 출력한다

#str=file.readline()
#if(str ==""):
 #  print("끝?")
    
file.close() #파일을 열엇으면 파일을 닫아야함

'''
while True:
    str=file.readline()
    print(str, end='')
    if (str==""): # 값이 없는 것을 확인함
        break
'''

'''
fileList = file.readlines()
index = 1
for strList in fileList : 
    print(str(index)+" : "+strList, end="")
    index = index + 1
'''