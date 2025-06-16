import tkinter
import tkinter.messagebox
import random

index = 0
timer = 0
score = 0
try:
    with open("hisc.txt", "r") as f:
        hisc = int(f.read())
except:
    hisc = 0
difficulty = 0
tsugi = 0

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
#추가된 전역 변수
destroyed_total = 0
frame_count = 0
wait_count = 0 #블럭 배치 대기 시간
countdown_timer = 0 #추가 : 카운트다운용 타이머
frame_count_pause = False 
place_count = 0



# 새로운 게임 공간: 12행 x 10열
GRID_WIDTH = 10
GRID_HEIGHT = 12
CELL_SIZE = 72
GRID_START_X = 21
GRID_START_Y = 23

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

def draw_neko():
    cvs.delete("NEKO")
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if neko[y][x] > 0:
                cvs.create_image(x * CELL_SIZE + GRID_START_X + CELL_SIZE // 2,
                                 y * CELL_SIZE + GRID_START_Y + CELL_SIZE // 2,
                                 image=img_neko[neko[y][x]], tag="NEKO")
# 첫번째 시작할 위치값(60)에 동일한 값(72)으로 이동하는 것.
def check_neko():
    global blockcount #4번
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH): #모든 칸에 대해서 실행
            check[y][x] = neko[y][x] #neko-> check(복사)

    for y in range(1, GRID_HEIGHT - 1):
        for x in range(GRID_WIDTH):
            if check[y][x] > 0:
                # 세로 일치 + 조커 허용
                c = check[y][x]
                a = check[y - 1][x]
                b = check[y + 1][x]
                if (a > 0 and b > 0 and
                    ((a == c or a == 8 or c == 8) and
                    (b == c or b == 8 or c == 8))):
                    neko[y - 1][x] = 7
                    neko[y][x] = 7
                    neko[y + 1][x] = 7

    for y in range(GRID_HEIGHT):
        for x in range(1, GRID_WIDTH - 1):
            if check[y][x] > 0:
                c = check[y][x]
                a = check[y][x - 1]
                b = check[y][x + 1]
                if (a > 0 and b > 0 and
                    ((a == c or a == 8 or c == 8) and
                    (b == c or b == 8 or c == 8))):
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7

    for y in range(1, GRID_HEIGHT - 1):
        for x in range(1, GRID_WIDTH - 1):
            if check[y][x] > 0:
                c = check[y][x]
                # 좌상-우하
                a = check[y - 1][x - 1]
                b = check[y + 1][x + 1]
                if (a > 0 and b > 0 and
                    ((a == c or a == 8 or c == 8) and
                    (b == c or b == 8 or c == 8))):
                    neko[y - 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y + 1][x + 1] = 7
                # 우상-좌하
                a2 = check[y - 1][x + 1]
                b2 = check[y + 1][x - 1]
                if (a2 > 0 and b2 > 0 and
                    ((a2 == c or a2 == 8 or c == 8) and
                    (b2 == c or b2 == 8 or c == 8))):
                    neko[y + 1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y - 1][x + 1] = 7



    # 🔧 추가: 2x2 네모 형태 블럭 파괴 조건
    for y in range(GRID_HEIGHT - 1):
        for x in range(GRID_WIDTH - 1):
            if check[y][x] > 0:
                a = check[y][x]
                b = check[y][x + 1]
                c = check[y + 1][x]
                d = check[y + 1][x + 1]
                # 4개 중 1개라도 조커(8)거나, 모두 같은 숫자면 OK
                if (
                    (a == b or a == 8 or b == 8) and
                    (a == c or a == 8 or c == 8) and
                    (a == d or a == 8 or d == 8) and
                    (b == c or b == 8 or c == 8) and
                    (b == d or b == 8 or d == 8) and
                    (c == d or c == 8 or d == 8)
                ):
                    neko[y][x] = 7
                    neko[y][x + 1] = 7
                    neko[y + 1][x] = 7
                    neko[y + 1][x + 1] = 7


def sweep_neko():
    num = 0
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH): #모든 칸에 대해서 실행
            if neko[y][x] == 7:
                block_type = check[y][x]
                if 1 <= block_type <= 6:
                    blockcount[block_type -1] += 1
                neko[y][x] = 0 #빈칸
                num = num + 1 #파괴된 블럭개수를 표현
    print("blockcount:", blockcount) #4번
    return num

def drop_neko(): 
    flg = False
    for y in range(GRID_HEIGHT - 2, -1, -1): #아래에서 위로 검사
        for x in range(GRID_WIDTH): #모든 블럭에 대해서 검사
            if neko[y][x] != 0 and neko[y + 1][x] == 0:  # neko[y + 1][x] == 0: -->블럭이 비어있다는 것을 의미.
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0
                flg = True
    return flg

def over_neko():#게임 종료 조건
    for x in range(GRID_WIDTH):
        if neko[0][x] > 0: #첫번째줄을 의미 #맨 윗줄에 블럭이 있으면
            return True #게임 종료을 의미
    return False

def set_neko():
    for x in range(GRID_WIDTH):
        neko[0][x] = random.randint(0, difficulty)  #블럭을 생성(0 빈블럭, 1-6 일반블럭)

def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)

def on_esc():  #  ESC 키 처리
    global index, timer, frame_count_pause
    if index in [2, 3, 4, 5]:  # 게임 중일 때만 적용
        frame_count_pause = True  #  멈춤
        res = tkinter.messagebox.askyesno("종료 확인", "게임을 종료하시겠습니까?")
        frame_count_pause = False  #  재개
        if res:
            cvs.delete("CURSOR")
            cvs.delete("NEKO")
            cvs.delete("INFO")
            cvs.delete("COUNTDOWN")
            index = 0
            timer = 0

def game_main():
    global index, timer, score, hisc, difficulty, tsugi
    global cursor_x, cursor_y, mouse_c
    global destroyed_total, frame_count, wait_count, countdown_timer, frame_count_pause, place_count# 🔧 추가:
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
            if 368 < mouse_x < 656 and 384 < mouse_y < 456:
                difficulty = 4
            if 368 < mouse_x < 656 and 528 < mouse_y < 600:
                difficulty = 5
            if 368 < mouse_x < 656 and 672 < mouse_y < 744:
                difficulty = 6 #디피컬트는 0이 아님을 의미.
        if difficulty > 0:
            for y in range(GRID_HEIGHT):
                for x in range(GRID_WIDTH):
                    neko[y][x] = 0
            mouse_c = 0
            score = 0
            tsugi = 0
            frame_count = 0 #경기 시간 초기화
            destroyed_total = 0 # 파괴 수 초기화
            cursor_x = 0
            cursor_y = 0
            countdown_timer = 0#카운트다운 초기화
            set_neko()
            draw_neko()
            cvs.update()
            cvs.delete("TITLE")
            # 🔧 바로 3을 그려줌 (1프레임 대기 없이 즉시 반응)
            draw_txt("3", 551, 384, 80, "red", "COUNTDOWN")
            cvs.update()  # 🔧 강제로 캔버스 즉시 갱신
            index = 7
    elif index == 2:  # 블록 낙하
        if drop_neko() == False:
            for y in range(GRID_HEIGHT):
                for x in range(GRID_WIDTH):
                    if neko[y][x] == 8:
                        neko[y][x] = random.randint(1, difficulty)
            index = 3
        draw_neko()
    elif index == 3:  # 나란히 놓인 블록 확인
        check_neko()
        draw_neko()
        index = 4
    elif index == 4:  # 나란히 놓인 고양이 블록이 있다면 #삭제 조건
        sc = sweep_neko()
        destroyed_total += sc  # 🔧 추가
        score = score + sc * difficulty * 2

        if sc >= 10:  # 🔧 추가: 10개 이상 파괴 시 보너스 점수
            bonus = (sc // 10) * 10
            score += bonus

        if score > hisc:
            hisc = score
        if sc > 0:
            index = 2
        else:
            if over_neko() == False:
                tsugi = random.randint(1, difficulty)
                wait_count = 0 #추가: 대기 시간 초기화
                index = 5
            else:
                index = 6
                timer = 0
        draw_neko()
    elif index == 5:  # 마우스 입력 대기
        wait_count += 1  #  프레임 증가

        if wait_count >= 50:  # 5초(약 50프레임) 지나면 자동 배치
            for y in range(GRID_HEIGHT - 1, -1, -1):
                if neko[y][cursor_x] == 0:
                    neko[y][cursor_x] = tsugi
                    #place_count 증가 /  조커블럭 없음
                    tsugi = random.randint(1, difficulty)
                    index = 2
                    break

        if GRID_START_X <= mouse_x < GRID_START_X + CELL_SIZE * GRID_WIDTH and \
           GRID_START_Y <= mouse_y < GRID_START_Y + CELL_SIZE * GRID_HEIGHT:
            cursor_x = int((mouse_x - GRID_START_X) / CELL_SIZE)
            cursor_y = int((mouse_y - GRID_START_Y) / CELL_SIZE)
            if mouse_c == 1: #클릭하면
                mouse_c = 0
                set_neko()
                neko[cursor_y][cursor_x] = tsugi
                tsugi = 0
                place_count += 1
                if place_count % 5 == 0 :
                    tsugi = 8
                    tsugi = random.randint(1, difficulty)
                index = 2 #블록낙하
        cvs.delete("CURSOR") #이미지를 지우고 생성하는것.
        cvs.create_image(cursor_x * CELL_SIZE + GRID_START_X + CELL_SIZE // 2,
                         cursor_y * CELL_SIZE + GRID_START_Y + CELL_SIZE // 2,
                         image=cursor, tag="CURSOR")
        draw_neko()
    elif index == 6:  # 게임 오버
        timer = timer + 1
        if timer == 1:
            draw_txt("GAME OVER", 551, 455, 60, "red", "OVER")
            # 🔥 최고 점수 저장
            if score > hisc:
                hisc = score
                with open("hisc.txt", "w") as f:
                    f.write(str(hisc))
        if timer == 50: #타이머가 50이되면
            cvs.delete("OVER")
            index = 0
    elif index == 7:  # 🔧 추가: 카운트다운 화면
        countdown_timer += 1
        cvs.delete("COUNTDOWN")

        if countdown_timer < 5:
            draw_txt("3", 551, 384, 80, "red", "COUNTDOWN")
        elif countdown_timer < 10:
            draw_txt("2", 551, 384, 80, "red", "COUNTDOWN")
        elif countdown_timer < 15:
            draw_txt("1", 551, 384, 80, "red", "COUNTDOWN")
        elif countdown_timer < 20:
            draw_txt("GO!", 551, 384, 80, "yellow", "COUNTDOWN")
        else:
            cvs.delete("COUNTDOWN")
            set_neko()
            draw_neko()
            index = 2
    cvs.delete("INFO")
    draw_txt("SCORE " + str(score), 130, 60, 32, "blue", "INFO")
    draw_txt("HISC " + str(hisc), 960, 60, 32, "yellow", "INFO")
    draw_txt("DESTROYED " + str(destroyed_total), 660, 60, 32, "red", "INFO")  #  파괴 수 표시
    draw_txt("TIME " + str(frame_count), 360, 60, 32, "black", "INFO")  # 시간 표시 텍스트
    if index >= 2 and index <= 5 and not frame_count_pause: 
        frame_count += 1 
    if tsugi > 0:
        cvs.create_image(904, 164, image=img_neko[tsugi], tag="INFO")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("블록 낙하 퍼즐 '야옹야옹'")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
root.bind("<Escape>", lambda e: on_esc())  # 🔧 추가: ESC 키 이벤트 바인딩
cvs = tkinter.Canvas(root, width=1102, height=910) #이미지 사이즈 #나중에 수정
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
    tkinter.PhotoImage(file="neko_niku.png"),
    tkinter.PhotoImage(file="neko_joker.png")
] # 0,1,2,3,4,5,6,7,8 블럭 이미지

cvs.create_image(551, 455, image=bg)
game_main()
root.mainloop()