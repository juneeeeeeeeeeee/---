import turtle as t
import sys
from time import sleep
#X:-1, O:1
#0(-200, 200), 1(0, 200), 2(200, 200), ...
def drawx(x, y):
  t.up()
  t.goto(x, y)
  t.down()
  t.goto(x+50, y+50)
  t.up()
  t.goto(x, y)
  t.down()
  t.goto(x-50, y+50)
  t.up()
  t.goto(x, y)
  t.down()
  t.goto(x+50, y-50)
  t.up()
  t.goto(x, y)
  t.down()
  t.goto(x-50, y-50)
  t.up()
  t.goto(0, 0)
def drawo(x, y):
  t.up()
  t.goto(x+50, y)
  t.setheading(90)
  t.down()
  t.circle(50)
  t.up()
  t.goto(0, 0)
def drawgrid():
  t.up()
  for i in range(0, 4):
    t.goto(-300+200*i, 300)
    t.down()
    t.goto(-300+200*i, -300)
    t.up()
  for i in range(0, 4):
    t.goto(-300, 300-200*i)
    t.down()
    t.goto(300, 300-200*i)
    t.up()
  t.goto(0, 0)
def gameend_winlose(playboard):
  for (a, b, c) in ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)):
    if playboard[a]==playboard[b] and playboard[b]==playboard[c] and ((playboard[a])*(playboard[b])*(playboard[c]))!=0:
      if playboard[a]==-1:
        return 'X'
      elif playboard[a]==1:
        return 'O'
def gameend_draw(playboard):
  product=1
  for i in range(0, 9):
    product=product*playboard[i]
  if product!=0: #누군가 이기거나 지는 경우는 이미 winlose함수에서 체크됨
    return 'draw'
  else:
    return 'notdone'
def depththingy(playboard, depth):
  if depth%2==0:
    maximum=-1000
    maxindex=-1000
    for i in range(0, 9):
      if playboard[i]==0:
        playboard_new=playboard.copy()
        if player=='X':
          playboard_new[i]=1
        elif player=='O':
          playboard_new[i]=-1
        if gameend_winlose(playboard_new)=='X' or gameend_winlose(playboard_new)=='O':
          return i, 10-depth
        elif gameend_draw(playboard_new)=='draw':
          return i, 0
        i_index, i_value=depththingy(playboard_new, depth+1)
        if maximum<i_value:
          maximum=i_value
          maxindex=i
    return maxindex, maximum
  elif depth%2==1:
    minimum=1000
    minindex=-1000
    for i in range(0, 9):
      if playboard[i]==0:
        playboard_new=playboard.copy()
        if player=='X':
          playboard_new[i]=-1
        elif player=='O':
          playboard_new[i]=1
        if gameend_winlose(playboard_new)=='X' or gameend_winlose(playboard_new)=='O':
          return i, -10+depth
        elif gameend_draw(playboard_new)=='draw':
          return i, 0
        i_index, i_value=depththingy(playboard_new, depth+1)
        if minimum>i_value:
          minimum=i_value
          minindex=i
    return minindex, minimum
while True:
  playboard_now=[0 for i in range(0, 9)]
  t.speed('fastest')
  drawgrid()
  player=t.textinput("입력", "O, X중 골라주세요(X가 선)/Cancel을 눌러 게임을 그만할 수 있습니다. ")
  while player!='O' and player!='X' and player!=None:
    player=t.textinput("입력", "잘못 입력하였습니다! \nO, X중 골라주세요(X가 선)/Cancel을 눌러 게임을 그만할 수 있습니다. ")
  if player==None:
    sys.exit(0)
  turn='X'
  while gameend_winlose(playboard_now)!='O' and gameend_winlose(playboard_now)!='X' and gameend_draw(playboard_now)=='notdone':
    if turn==player:
      clickedindex=int(t.numinput("입력", "숫자 선택: 0(왼쪽 위)~8(오른쪽 아래)/Cancel을 누르지 마세요. "))
      while playboard_now[clickedindex]!=0:
        clickedindex=int(t.numinput("입력", "잘못 입력하였습니다! \n숫자 선택: 0(왼쪽 위)~8(오른쪽 아래)/Cancel을 누르지 마세요. "))
      if player=='X':
        playboard_now[clickedindex]=-1
        drawx(((clickedindex%3)-1)*200, (1-(clickedindex//3))*200)
      elif player=='O':
        playboard_now[clickedindex]=1
        drawo(((clickedindex%3)-1)*200, (1-(clickedindex//3))*200)
      turn='XO'.strip(turn)
    elif turn!=player:
      #각각의 위치에 대해 기댓값 확인, 가장 큰 값으로 플레이보드 조작, 화면 조작
      maxindex, maxvalue=depththingy(playboard_now, 0)
      if player=='X':
        playboard_now[maxindex]=1
        drawo(((maxindex%3)-1)*200, (1-(maxindex//3))*200)
      elif player=='O':
        playboard_now[maxindex]=-1
        drawx(((maxindex%3)-1)*200, (1-(maxindex//3))*200)
      turn='XO'.strip(turn)
  if gameend_winlose(playboard_now)=='O':
    t.goto(0, 0)
    t.write("O Win", False, "center", ("", 20))
  elif gameend_winlose(playboard_now)=='X':
    t.goto(0, 0)
    t.write("X Win", False, "center", ("", 20))
  elif gameend_draw(playboard_now)=='draw':
    t.goto(0, 0)
    t.write("Draw", False, "center", ("", 20))
  sleep(1.5)
  print("u succ")
  t.clear()