import tkinter
import random
import tkinter.messagebox

index = 0
timer = 0
score = 0
hisc = 0
difficulty = 0
tsugi = 0

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
play_timer = 0
inactive_timer = 0

#공간정보 저장
neko = []
check = []
for i in range(12):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#리스트안에 리스트가 있음.
    check.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#가로 8개가 세로 10번 반복됨.

#블럭 정보 저장 #4번
blockcount=[0,0,0,0,0,0] #0~5까지 index를 갖고있음

#함수 영역
def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1

def draw_neko(): #NEKO를 지우고 생성하는 과정을 반복.
    cvs.delete("NEKO") #캔버스에서 "NEKO"을 삭제
    for y in range(12): #세로 #80번 실행된다는디
        for x in range(10): #가로
            if neko[y][x] > 0: #모든 칸에 대해서 실행
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[7], tag="NEKO") #NEKO 생성
            else:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image=img_neko[neko[y][x]], tag="NEKO")
# 첫번째 시작할 위치값(60)에 동일한 값(72)으로 이동하는 것.
def check_neko():
    global blockcount #4번
    for y in range(12):
        for x in range(10): #모든 칸에 대해서 실행
            check[y][x] = neko[y][x] #neko-> check(복사)

    for y in range(1,11):
        for x in range(10): #  맨 위와 맨 아래줄을 제외한 모든 칸에 대해서 실행
            if check[y][x] > 0: #세로 블럭
                if y < 11 and check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]: 
                    neko[y - 1][x] = 7 #관련된 모든 블럭을 7로 바꿔줌 #파괴전 이펙트
                    neko[y][x] = 7
                    neko[y + 1][x] = 7

    for y in range(12):
        for x in range(1, 9):  #  맨 왼쪽과 맨 오른쪽을 제외한 모든 칸에 대해서 실행
            if check[y][x] > 0: #가로블럭
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7

    for y in range(1, 11):
        for x in range(1, 9):
            if check[y][x] > 0: #대각선 블럭
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]: #왼쪽 상단 오른쪽 하단
                    neko[y - 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y + 1][x + 1] = 7
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    neko[y + 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y - 1][x + 1] = 7

    for y in range(11):
        for x in range(9):
            if check[y][x] > 0: #대각선 블럭
                if check[y][x + 1] == check[y][x] == check[y + 1][x] == check[y + 1][x + 1]: #왼쪽 상단 오른쪽 하단
                    neko[y][x] = 7
                    neko[y][x + 1] = 7
                    neko[y + 1][x] = 7
                    neko[y + 1][x + 1] = 7

def sweep_neko():
    global score
    num = 0
    for y in range(12):
        for x in range(10): #모든 칸에 대해서 실행
            if neko[y][x] == 7:
                neko[y][x] = 0 #빈칸
                num = num + 1 #파괴된 블럭개수를 표현
    if num >= 10:
        score += (num // 10) * 10
        print("blockcount:", blockcount) #4번
    return num

def drop_neko(): 
    flg = False
    for y in range(10, -1, -1): #아래에서 위로 검사
        for x in range(10): #모든 블럭에 대해서 검사
            if neko[y][x] != 0 and neko[y + 1][x] == 0:  # neko[y + 1][x] == 0: -->블럭이 비어있다는 것을 의미.
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():#게임 종료 조건
    for x in range(10):
        if neko[0][x] > 0: #첫번째줄을 의미 #맨 윗줄에 블럭이 있으면
            return True #게임 종료을 의미
    return False

def set_neko():
    for x in range(10):
        neko[0][x] = random.randint(0, difficulty)  #블럭을 생성(0 빈블럭, 1-6 일반블럭)

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def game_main():
    global index, timer, score, hisc, difficulty, tsugi
    global cursor_x, cursor_y, mouse_c
    global play_timer, inactive_timer
    if index == 0:  # 타이틀 로고
        draw_txt("야옹야옹", 312, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        draw_txt("Easy", 312, 420, 40, "white", "TITLE")
        cvs.create_rectangle(168, 528, 456, 600, fill="lightgreen", width=0, tag="TITLE")
        draw_txt("Normal", 312, 564, 40, "white", "TITLE")
        cvs.create_rectangle(168, 672, 456, 744, fill="orange", width=0, tag="TITLE")
        draw_txt("Hard", 312, 708, 40, "white", "TITLE")
        index = 1 
        mouse_c = 0

    elif index == 1:  # 타이틀 화면, 시작 대기
        difficulty = 0 #초기값
        if mouse_c == 1:
            if 168 < mouse_x and mouse_x < 552 and 384 < mouse_y and mouse_y < 456:
                difficulty = 4
            if 168 < mouse_x and mouse_x < 552 and 528 < mouse_y and mouse_y < 600:
                difficulty = 5
            if 168 < mouse_x and mouse_x < 552 and 672 < mouse_y and mouse_y < 744:
                difficulty = 6 #디피컬트는 0이 아님을 의미.
        if difficulty > 0:
            for y in range(12):
                for x in range(10):
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            tsugi = 0
            cursor_x = 0
            cursor_y = 0
            play_timer = 0 #시간
            inactive_timer = 0
            set_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2

    elif index in [2,3,4,5]: #게임 플레이 중일 때
            play_timer += 1 # 경기 시간 증가
            inactive_timer += 1 # 조작 없음 시간 증가

            if mouse_c == 1:
                inactive_timer = 0

            if inactive_timer >= 300 : #약 5초
                drop_neko() # 자동 블럭 낙하
                inactive_timer = 0 # 타이머 리셋

    elif index == 2:  # 블록 낙하
        if drop_neko() == False:
            index = 3
        draw_neko()
    elif index == 3:  # 나란히 놓인 블록 확인
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:  # 나란히 놓인 고양이 블록이 있다면 #삭제 조건
        sc = sweep_neko()
        score = score + sc * difficulty * 2
        if score > hisc:
            hisc = score
        if sc > 0:
            index = 2
        else:
            if over_neko() == False:
                tsugi = random.randint(1, difficulty)
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()
    elif index == 5:  # 마우스 입력 대기
        if 24 <= mouse_x and mouse_x < 24 + 72 * 10 and 24 <= mouse_y and mouse_y < 24 + 72 * 12:
            # 24 <= mouse_x and mouse_x < 24 + 72 * 8 -> 체크박스 안에서만 마우스 입력이 되게. #가로
            cursor_x = int((mouse_x - 24) / 72) # 칸 수 만큼 입력 0~7
            cursor_y = int((mouse_y - 24) / 72) # 칸 수 만큼 입력 0~9
            if mouse_c == 1: #클릭하면
                mouse_c = 0
                set_neko()
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                index = 2 #블록낙하
        cvs.delete("CURSOR") #이미지를 지우고 생성하는것.
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6:  # 게임 오버
        timer = timer + 1
        if timer == 1:
            draw_txt("GAME OVER", 360, 348, 60, "red", "OVER")
        if timer == 50: #타이머가 50이되면
            cvs.delete("OVER")
            index = 0
    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 160, 60, 32, "blue", "INFO")
    draw_txt("HISC " + str(hisc), 550, 60, 32, "yellow", "INFO")
    draw_txt("TIME" + str(play_timer), 300, 100, 28, "white", "INFO") #시간 출력
    draw_txt("5초 이상 클릭 없으면 자동 낙하!", 312, 920, 24, "red", "INFO")
    if tsugi > 0:
        cvs.create_image(792, 128, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

#게임 루프 함수 아래에 esc_key 함수 추가
def esc_key(event):
    global index
    if index in [2,3,4,5]:
        res = tkinter.messagebox.askyesno("종료 확인","게임을 종료하시겠습니까?" )
        if res:
            #게임 상태 초기화
            for y in range(12):
                for x in range(10):
                    neko[y][x]=0
            cvs.delete("NEKO")
            cvs.delete("CURSOR")
            cvs.delete("INFO")
            index = 0
            game_main()

root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<Escape>", esc_key)
cvs = tkinter.Canvas(root, width=912, height=960) #이미지 사이즈 #나중에 수정
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="neko1.png"),
    tkinter.PhotoImage(file="neko2.png"),
    tkinter.PhotoImage(file="neko3.png"),
    tkinter.PhotoImage(file="neko4.png"),
    tkinter.PhotoImage(file="neko5.png"),
    tkinter.PhotoImage(file="neko6.png"),
    tkinter.PhotoImage(file="neko_niku.png")
] # 0,1,2,3,4,5,6,7,8 블럭 이미지

cvs.create_image(456, 480, image=bg)
game_main()
root.mainloop()
