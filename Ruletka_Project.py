import random
import plotly
import plotly.graph_objs as go

startmoney = 1000000
c1 = 0.001
win = 0
loose = 0
games = 0

balance1 = []
games1 = []

balance2 = []
games2 = []

balance3 = []
games3 = []
money = startmoney

while money > 0:
    bet = startmoney * c1
    if bet > money:
        bet = money
    money -= bet
    balance1.append(money)
    games1.append(len(games1) + 1)
    ball = random.randint(1, 37)
    
    if ball in range(1, 19):    
        money += bet * 2
        win += 1
    else:
        loose += 1
games = win + loose
print("Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + " Проиграно ставок: " + str(
    loose) + " (" + str(loose / games * 100) + "%). ")

money = startmoney

win = 0
loose = 0
money = startmoney
# играем, пока есть деньги или пока мы не сыграем столько же игр, как и в первый раз
while (money > 0) and (win + loose < games):
    bet = startmoney * c1
    # если ставка получилась больше, чем у нас осталось денег — ставим всё, что осталось, чтобы не уйти в минус
    if bet > money:
        bet = money
    money -= bet

    # записываем очередную игру в статистику — деньги и номер игры
    balance2.append(money)
    games2.append(len(games2) + 1)
    ball = random.randint(1, 36)
    if ball in range(1, 19):
        # получаем назад нашу ставку в двойном размере
        money += bet * 2
        win += 1
    else:
        loose += 1


print("Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + " Проиграно ставок: " + str(
    loose) + " (" + str(loose / games * 100) + "%). ")

money = startmoney
win = 0
loose = 0
money = startmoney
while (money > 0) and (win + loose < games):
    bet = startmoney * c1
    if bet > money:
        bet = money
    money -= bet
    balance3.append(money)
    games3.append(len(games3) + 1)
    ball = random.randint(1, 35)
    # пусть первые 18 будут чёрными — для простоты алгоритма
    # если наша ставка сыграла — мы попали в нужный диапазон
    if ball in range(1, 19):
        # получаем назад нашу ставку в двойном размере
        money += bet * 2
        # увеличиваем количество побед
        win += 1
    else:
        # иначе — увеличиваем количество проигрышей
        loose += 1

print("Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + " Проиграно ставок: " + str(
    loose) + " (" + str(loose / games * 100) + "%). ")


fig = go.Figure()
fig.add_trace(go.Scatter(x=games1, y=balance1, name="Отрицательное матожидание"))
fig.add_trace(go.Scatter(x=games2, y=balance2, name="Нулевое матожидание"))
fig.add_trace(go.Scatter(x=games3, y=balance3, name="Положительное матожидание"))

fig.show()
