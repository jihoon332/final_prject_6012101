from graphics import *
import random
from time import sleep

# 문제들
questions = [
    ("주먹도끼", 0),
    ("찍개", 0),
    ("슴베찌르개", 0),
    ("빗살무늬 토기", 1),
    ("갈돌과 갈판", 1),
    ("조개껍데기 가면", 1),
    ("청동 거울", 2),
    ("비파형 동검", 2),
    ("고인돌", 2),
    ("반달돌칼", 2)
]

choices = ["구석기", "신석기", "청동기"]


def draw_button(win, x1, y1, x2, y2, text, color):
    btn = Rectangle(Point(x1, y1), Point(x2, y2))
    btn.setFill(color)
    btn.draw(win)

    label = Text(Point((x1+x2)/2, (y1+y2)/2), text)
    label.draw(win)

    return btn, label


def inside(click, rect):
    x = click.getX()
    y = click.getY()
    p1 = rect.getP1()
    p2 = rect.getP2()
    return p1.getX() <= x <= p2.getX() and p1.getY() <= y <= p2.getY()


def get_rank(score):
    if score >= 60: return "역사 박사"
    elif score >= 40: return "역사 탐험가"
    elif score >= 20: return "역사 초보"
    else: return "다시 도전"



# 유물 함수

def draw_artifact(win, name):
    drawn_objects = []
    
    # 기준 중심 가로 중간 세로 중간
    cx, cy = 350, 180

    if name == "주먹도끼":
       
        shape = Polygon(Point(cx, cy-40), Point(cx+30, cy+30), Point(cx-30, cy+30))
        shape.setFill("gray")
        
        line1 = Line(Point(cx, cy-40), Point(cx, cy+30))
        line2 = Line(Point(cx-15, cy), Point(cx+15, cy))
        for obj in [shape, line1, line2]:
            obj.draw(win)
            drawn_objects.append(obj)

    elif name == "찍개":
        
        shape = Oval(Point(cx-40, cy-30), Point(cx+40, cy+40))
        shape.setFill("darkgray")
        
        edge = Line(Point(cx-35, cy-10), Point(cx+35, cy-10))
        edge.setWidth(3)
        for obj in [shape, edge]:
            obj.draw(win)
            drawn_objects.append(obj)

    elif name == "슴베찌르개":
        
        blade = Polygon(Point(cx, cy-40), Point(cx+20, cy+10), Point(cx-20, cy+10))
        blade.setFill("lightgray")
        tang = Rectangle(Point(cx-6, cy+10), Point(cx+6, cy+45))
        tang.setFill("peru")
        for obj in [tang, blade]: 
            obj.draw(win)
            drawn_objects.append(obj)

    elif name == "빗살무늬 토기":
       
        pot = Polygon(Point(cx-35, cy-40), Point(cx+35, cy-40), Point(cx+30, cy+10), Point(cx, cy+45), Point(cx-30, cy+10))
        pot.setFill("sienna")
        pot.draw(win)
        drawn_objects.append(pot)
      
        for i in range(-25, 25, 15):
            l = Line(Point(cx-25, cy+i), Point(cx+25, cy+i-5))
            l.draw(win)
            drawn_objects.append(l)

    elif name == "갈돌과 갈판":
       
        plate = Rectangle(Point(cx-60, cy+5), Point(cx+60, cy+45))
        plate.setFill("gray")         
         
   
        stone = Rectangle(Point(cx-45, cy-25), Point(cx+45, cy+15))
        stone.setFill("lightgray")          

        for obj in [plate, stone]:
            obj.draw(win)
            drawn_objects.append(obj)

    elif name == "조개껍데기 가면":
      
        shell = Polygon(Point(cx-15, cy+35), Point(cx-40, cy), Point(cx-30, cy-35), Point(cx, cy-45), Point(cx+30, cy-35), Point(cx+40, cy), Point(cx+15, cy+35))
        shell.setFill("white")
        shell.draw(win)
        drawn_objects.append(shell)

        l1 = Line(Point(cx-15, cy+35), Point(cx-30, cy-35))
        l2 = Line(Point(cx-15, cy+35), Point(cx, cy-45))
        l3 = Line(Point(cx+15, cy+35), Point(cx, cy-45))
        l4 = Line(Point(cx+15, cy+35), Point(cx+30, cy-35))
        
        eye1 = Circle(Point(cx-15, cy-10), 5)
        eye1.setFill("black")
        eye2 = Circle(Point(cx+15, cy-10), 5)
        eye2.setFill("black")
        mouth = Circle(Point(cx, cy+15), 7)
        mouth.setFill("black")

        for obj in [l1, l2, l3, l4, eye1, eye2, mouth]:
            obj.draw(win)
            drawn_objects.append(obj)

    elif name == "청동 거울":
     
        mirror = Circle(Point(cx, cy), 45)
        mirror.setFill("darkolivegreen")
        center = Circle(Point(cx, cy), 8)
        center.setFill("black")
        
        ring = Circle(Point(cx, cy), 35)
        ring.setOutline("gold")
        for obj in [mirror, ring, center]:
            obj.draw(win)
            drawn_objects.append(obj)

    elif name == "비파형 동검":
       
        blade = Polygon(Point(cx, cy-50), Point(cx+12, cy-20), Point(cx+22, cy), Point(cx+8, cy+25), Point(cx-8, cy+25), Point(cx-22, cy), Point(cx-12, cy-20))
        blade.setFill("cadetblue")
        handle = Rectangle(Point(cx-4, cy+25), Point(cx+4, cy+50))
        handle.setFill("goldenrod")
        for obj in [handle, blade]:
            obj.draw(win)
            drawn_objects.append(obj)

    elif name == "고인돌":
        
        top = Rectangle(Point(cx-45, cy-20), Point(cx+45, cy+2))
        top.setFill("gray")
        leg1 = Rectangle(Point(cx-30, cy+2), Point(cx-15, cy+40))
        leg1.setFill("darkgray")
        leg2 = Rectangle(Point(cx+15, cy+2), Point(cx+30, cy+40))
        leg2.setFill("darkgray")
        for obj in [leg1, leg2, top]:
            obj.draw(win)
            drawn_objects.append(obj)

    elif name == "반달돌칼":
        
        blade = Polygon(Point(cx-45, cy), Point(cx-20, cy-30), Point(cx+20, cy-30), Point(cx+45, cy), Point(cx+25, cy+20), Point(cx-25, cy+20))
        blade.setFill("gray")
        h1 = Circle(Point(cx-15, cy-5), 3)
        h2 = Circle(Point(cx+15, cy-5), 3)
        h1.setFill("white")
        h2.setFill("white")
        for obj in [blade, h1, h2]:
            obj.draw(win)
            drawn_objects.append(obj)

    return drawn_objects


def main():
    win = GraphWin("행소박물관 퀴즈", 700, 500)
    win.setBackground("skyblue")

   
    # 시작화면 그리기
    
    sun = Circle(Point(600, 80), 40)
    sun.setFill("gold")
    sun.draw(win)

    mountain1 = Polygon(Point(0, 250), Point(120, 100), Point(240, 250))
    mountain1.setFill("sienna")
    mountain1.draw(win)

    mountain2 = Polygon(Point(180, 250), Point(350, 80), Point(520, 250))
    mountain2.setFill("peru")
    mountain2.draw(win)

    mountain3 = Polygon(Point(420, 250), Point(580, 120), Point(700, 250))
    mountain3.setFill("saddlebrown")
    mountain3.draw(win)

    ground = Rectangle(Point(0, 250), Point(700, 500))
    ground.setFill("green")
    ground.draw(win)

    rock1 = Oval(Point(80, 360), Point(140, 400))
    rock1.setFill("gray")
    rock1.draw(win)

    rock2 = Oval(Point(520, 370), Point(590, 410))
    rock2.setFill("gray")
    rock2.draw(win)

    stone_top = Rectangle(Point(290, 220), Point(410, 250))
    stone_top.setFill("gray")
    stone_top.draw(win)

    stone_left = Rectangle(Point(300, 250), Point(330, 310))
    stone_left.setFill("gray")
    stone_left.draw(win)

    stone_right = Rectangle(Point(370, 250), Point(400, 310))
    stone_right.setFill("gray")
    stone_right.draw(win)

    title = Text(Point(350, 70), "행소박물관 유물 퀴즈")
    title.setSize(22)
    title.setStyle("bold")
    title.setTextColor("white")
    title.draw(win)

    subtitle = Text(Point(350, 110), "구석기 · 신석기 · 청동기")
    subtitle.setSize(15)
    subtitle.setTextColor("white")
    subtitle.draw(win)

    info = Text(Point(350, 340), "랜덤 7문제가 출제됩니다")
    info.setSize(14)
    info.setTextColor("white")
    info.draw(win)

    start_btn = Rectangle(Point(250, 390), Point(450, 450))
    start_btn.setFill("orange")
    start_btn.draw(win)

    start_text = Text(Point(350, 420), "게임 시작")
    start_text.setSize(16)
    start_text.setStyle("bold")
    start_text.draw(win)

    while True:
        click = win.getMouse()
        if inside(click, start_btn):
            break

    # 시작화면 지우기
    for obj in [title, subtitle, info, start_btn, start_text, sun, mountain1, mountain2, mountain3, ground, rock1, rock2, stone_top, stone_left, stone_right]:
        obj.undraw()

    win.setBackground("white")

    # 카운트다운
    for num in ["3", "2", "1", "START!"]:
        txt = Text(Point(350, 250), num)
        txt.setSize(30)
        txt.setStyle("bold")
        txt.draw(win)
        sleep(1)
        txt.undraw()

    random.shuffle(questions)
    quiz_list = questions[:7]
    score = 0

    # 퀴즈 진행
    for number, (artifact, answer) in enumerate(quiz_list):
        objects = []

        q_num = Text(Point(350, 40), f"{number+1} / 7 문제")
        q_num.setSize(16)
        q_num.draw(win)
        objects.append(q_num)

        score_text = Text(Point(600, 40), f"점수 : {score}")
        score_text.draw(win)
        objects.append(score_text)

        question = Text(Point(350, 80), "이 유물은 어느 시대일까요?")
        question.setSize(15)
        question.draw(win)
        objects.append(question)

        # 배경 박스 
        artifact_box = Rectangle(Point(220, 120), Point(480, 260))
        artifact_box.setFill("white") 
        artifact_box.setOutline("lightgray")
        artifact_box.draw(win)
        objects.append(artifact_box)

        # 유물 그래픽 그리기 함수 호출
        artifact_shapes = draw_artifact(win, artifact)
        objects.extend(artifact_shapes) # 지울 때 같이 지우기

        # 유물 이름 텍스트
        artifact_name = Text(Point(350, 285), artifact)
        artifact_name.setSize(16)
        artifact_name.setStyle("bold")
        artifact_name.draw(win)
        objects.append(artifact_name)

        btn1, txt1 = draw_button(win, 60, 330, 210, 390, "구석기", "lightblue")
        btn2, txt2 = draw_button(win, 275, 330, 425, 390, "신석기", "lightgreen")
        btn3, txt3 = draw_button(win, 490, 330, 640, 390, "청동기", "pink")

        while True:
            click = win.getMouse()
            choice = -1
            if inside(click, btn1): choice = 0; break
            elif inside(click, btn2): choice = 1; break
            elif inside(click, btn3): choice = 2; break

        result = Text(Point(350, 435), "")
        result.setSize(16)

        if choice == answer:
            score += 10
            result.setText("정답! +10점")
            result.setTextColor("blue")
        else:
            score -= 5
            result.setText(f"오답! 정답은 [{choices[answer]}]")
            result.setTextColor("red")

        result.draw(win)

        next_msg = Text(Point(350, 465), "클릭하여 다음 문제")
        next_msg.draw(win)

        win.getMouse()

        for obj in objects: obj.undraw()
        result.undraw()
        next_msg.undraw()
        btn1.undraw()
        btn2.undraw()
        btn3.undraw()
        txt1.undraw()
        txt2.undraw()
        txt3.undraw()

    # 결과 화면
    win.setBackground("lightyellow")

    end_title = Text(Point(350, 120), "퀴즈 종료!")
    end_title.setSize(24)
    end_title.setStyle("bold")
    end_title.draw(win)

    final_score = Text(Point(350, 220), f"최종 점수 : {score}점")
    final_score.setSize(20)
    final_score.draw(win)

    rank = Text(Point(350, 280), f"나의 등급 : {get_rank(score)}")
    rank.setSize(22)
    rank.setStyle("bold")
    rank.setTextColor("darkgreen")
    rank.draw(win)

    msg = Text(Point(350, 360), "클릭하면 종료됩니다")
    msg.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
