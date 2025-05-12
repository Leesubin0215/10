
outfile = open("outTest.txt", "w", endcoding="UTF-8")

while True:
    outStr = input("내용 입력==>")
    #'끝'이라고 입력하면 종료
    if ourStr == '끝':
        break
    outfile.writelines(outStr+"\n")

#outfile.writelines("안녕하세요.\n")
#outfile.writelines("반갑습니다.\n")

outfile.close()