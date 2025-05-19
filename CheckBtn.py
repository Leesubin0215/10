import tkinter
import random
import tkinter.messagebox

root=tkinter.Tk()

result = [
    "전생에 고양이었을 가능성은 매우 낮습니다.",
    "보통 사람입니다.",
    "특별히 이상한 곳은 없습니다.",
    "꽤 고양이 다운 구석이 있습니다",
    "고양이와 비슷한 성격 같습니다.",
    "고양이와 근접한 성격입니다.",
    "전생에 고양이었을지도 모릅니다.",
    "겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다."
]

#버튼 클릭시
def chkBtnClick():
    numCheck =0
    if cvalue1.get() == True : numCheck +=1
    if cvalue2.get() == True : numCheck +=1
    if cvalue3.get() == True : numCheck +=1
    if cvalue4.get() == True : numCheck +=1
    if cvalue5.get() == True : numCheck +=1
    if cvalue6.get() == True : numCheck +=1
    if cvalue7.get() == True : numCheck +=1
    print(numCheck)

#체크버튼 클릭시
def chkBtnClick():
    numCheck =0
    if cvalue1.get() == True : numCheck +=1
    if cvalue2.get() == True : numCheck +=1
    if cvalue3.get() == True : numCheck +=1
    if cvalue4.get() == True : numCheck +=1
    if cvalue5.get() == True : numCheck +=1
    if cvalue6.get() == True : numCheck +=1
    if cvalue7.get() == True : numCheck +=1
    print(numCheck)
    textFilled.delete("1.0", tkinter.END)
    textFilled.insert("1.0", "체크된 수는 "+str(numCheck)+"\n")

       # if cvalue.get()== True:
      #  print("체크 되었습니다.")
       # tkinter.messagebox.askyesno("제목","오징어 게임에 참가하시겠습니까?")
        #if answer == True:
   #         print("동의")
       # else:
      #      print("거절")
   # else:
       # print("체크가 해제 되었습니다.")

#좌표출력기
def mouseMove(event):
    x= event.x
    y= event.y
    labelMouse["text"]=str(x)+","+str(y)

root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕", 10))
labelMouse.pack()

#화면창 만들기
root.title("캔버스 만들기")
canvas=tkinter.Canvas(root, width=800, height=600, bg="beige")

#캔버스 내 이미지 생성
bgimg=tkinter.PhotoImage(file="mina.png")#같은 파일 안에 있어야 불러오기 쉬움
canvas.create_image(400,300,image=bgimg)

#저장하는 값이 먼저 나와야함
cvalue1 = tkinter.BooleanVar()
cvalue2 = tkinter.BooleanVar()
cvalue3 = tkinter.BooleanVar()
cvalue4 = tkinter.BooleanVar()
cvalue5 = tkinter.BooleanVar()
cvalue6 = tkinter.BooleanVar()
cvalue7 = tkinter.BooleanVar()

cvalue1.set(True)
cvalue2.set(True)
cvalue3.set(True)
cvalue4.set(True)
cvalue5.set(True)
cvalue6.set(True)
cvalue7.set(True)

cbtn1 = tkinter.Checkbutton(text="높은 곳이 좋다",variable=cvalue1,command=chkBtnClick) #variable=cvalue로 이어줌
cbtn2 = tkinter.Checkbutton(text="공을 보면 굴리고 싶어진다",variable=cvalue2,command=chkBtnClick)
cbtn3= tkinter.Checkbutton(text="깜짝 놀라면 털이 곤두선다",variable=cvalue3,command=chkBtnClick)
cbtn4 = tkinter.Checkbutton(text="쥐구멍이 마음에 든다",variable=cvalue4,command=chkBtnClick)
cbtn5 = tkinter.Checkbutton(text="개에게 적대감을 느낀다",variable=cvalue5,command=chkBtnClick)
cbtn6 = tkinter.Checkbutton(text="생선 뼈를 빨라먹고 싶다",variable=cvalue6,command=chkBtnClick)
cbtn7 = tkinter.Checkbutton(text="밤, 기운이 난다",variable=cvalue7,command=chkBtnClick)

cbtn1.place(x=402, y=165 +ygap*0)
cbtn2.place(x=402, y=165 +ygap*1)
cbtn3.place(x=402, y=165 +ygap*2)
cbtn4.place(x=402, y=165 +ygap*3)
cbtn5.place(x=402, y=165 +ygap*4)
cbtn6.place(x=402, y=165 +ygap*5)
cbtn7.place(x=402, y=165 +ygap*6)

textFilled = tkinter.Text()
textFilled.place(x=330, y=50, width=420, height=90)

btn = tkinter.Button(text="진단하기", font=("맑은 고딕", 24), bg='#CFF7EB')
btn.place

canvas.pack()# 이게 있어야 함.
root.mainloop()