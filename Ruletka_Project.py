import random
import plotly
import plotly.graph_objs as go

startmoney = 1000000
c1 = 0.001
win = 0
loose = 0
games = 0
# статистика для первой стратегии
balance1 = []
games1 = []
# статистика для второй стратегии
balance2 = []
games2 = []
# статистика для третьей стратегии
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
# обнуляем статистику
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
    # крутим рулетку, на которой 18 чёрных чисел, 18 красных. Так как всего поровну, матожидание будет равно нулю.
    # Ставим, как и в прошлом случае, на чёрное
    ball = random.randint(1, 36)
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

# выводим результат игры по второй  стратегии
print("Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + " Проиграно ставок: " + str(
    loose) + " (" + str(loose / games * 100) + "%). ")
# началась третья стратегия, тоже стартуем с полной суммой
# третья стратегия — с положительным матожиданием
money = startmoney
# обнуляем статистику
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

# выводим результат игры по третьей  стратегии
print("Выиграно ставок: " + str(win) + " (" + str(win / games * 100) + "%). " + " Проиграно ставок: " + str(
    loose) + " (" + str(loose / games * 100) + "%). ")

# строим графики
fig = go.Figure()
# для первой стратегии
fig.add_trace(go.Scatter(x=games1, y=balance1, name="Отрицательное матожидание"))
# для второй
fig.add_trace(go.Scatter(x=games2, y=balance2, name="Нулевое матожидание"))
# и для третьей
fig.add_trace(go.Scatter(x=games3, y=balance3, name="Положительное матожидание"))
# выводим графики в браузер
fig.show()
