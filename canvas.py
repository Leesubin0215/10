import tkinter
import random
root = tkinter.Tk()

#좌표 출력기
def mouseMove(event):
    x= event.x
    y= event.y
    labelMouse["text"]=str(x)+","+str(y)

def click_btn():
    label["text"]=random.choice(["대길","중길","소길","흉"])
    text.insert(tkinter.END, label["text"])


#좌표 출력기
root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕", 10))
labelMouse.pack()

#캔버스 생성
root.title("캔버스 만들기")
#root.geometry- 창의 크기를 지정해줌
canvas=tkinter.Canvas(root, width=800, height=600, bg="beige")
#캔버스가 루트랑 연결되어야 실행이 됨

#캔버스 내 이미지 생성
bgimg=tkinter.PhotoImage(file="miko.png")#같은 파일 안에 있어야 불러오기 쉬움
canvas.create_image(400,300,image=bgimg) # 단 두줄이면 사진을 불러올 수 있음
#백그라운드이미지가 캔버스랑 연결이 되어야 실행이 됨
#세개가 연결이 됨.객체 루트,캔버스,백그라운드이미지.

#제비뽑기 뒤에 사각형을 만듦
canvas.create_rectangle(402, 371, 620,482, fill='pink', outline='skyblue', width='3')

label=tkinter.Label(root, text="??", font=("맑은고딕", 100))
label.place(x=427, y=90)

btn =tkinter.Button(root, text="제비뽑기", font=("맑은 고딕",30), command=click_btn)
btn.place(x=413, y=400, width=200, height=100)

text=tkinter.Text()
text.pack()

canvas.pack()# 이게 있어야 함.
root.mainloop()