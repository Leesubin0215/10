#test.txt 파일을 불러와서
#outTest.txt 파일에 저장된다.

inFile = open ("test.txt", "r", encoding= "UTF-8")
outfile = open("outTest.txt", "w", encoding="UTF-8")

#---------------------------------------
#파일 ㅇ읽기
#strFile=inFile.readline()
#print(strFile, end="")

#파일 쓰기
#outfile.writelines(strFile)
#-------------------------------------------

#파일 읽어서 쓰기
while True:
    strFile =inFile.readline()
    if(strFile == ""):
        break
    outfile.writelines(strFile)

inFile.close()
outfile.close()