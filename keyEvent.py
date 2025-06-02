import tkinter

#전역 변수(key를 선언함)
key=0
cx = 400
cy = 300
#함수 영역 # 춘식이가 이동하는 코드( 왜 안되는거지)
def main_proc():
    global cx, cy, key
    #lable["text"]= key

    #키보드 입력으로 위치 변경
    if key == "Up":
        cy -=20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx = cx -20
    if key == "Right":
        cx = cx + 20

    #시간에 따라 캐릭터가 내려감
    cy += 10


    #변경된 위치의 경계를 확인 # 가장자리에 경계를 형성하고 이미지가 그 경계를 벗어나지 못하게 함
    if cy < 40 : cy = 40
    if cy> 600-40 : cy = 600-40 #cy의 한계점이 형성
    if cx < 40 : cx = 40
    if cy> 800-40 : cy = 800-40  #cx의 한계점이 형성
    #변겨된 위치에 이미지를 옮김
    canvas.coords("춘식",cx, cy)
    key = 0
    root.after(100, main_proc)


def key_down(e):
    global key
    key= e.keysym #keycode

def key_up(e):
    global key
    key = 0



#메인 영역
root = tkinter.Tk()
root.title("키 이벤트")
root.bind("KeyPress", key_down)
root.bind("KeyPress", key_up)
#lable = tkinter.Label(font=("맑은 고딕",80))
#lable.pack()
canvas = tkinter.Canvas(width=800, height=600, bg='skyblue')
canvas.pack()

img = tkinter.PhotoImage(file="춘식.png")
canvas.create_image(400,300, image=img, tag="춘식")
canvas.coords("춘식",500, 400)

main_proc()
root.mainloop()