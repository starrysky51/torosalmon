# coding: utf-8
import random

# 山札の準備
cards = []
for i in range(1, 53):
    cards.append(i)

# AさんとBさんの点数
point_a = 0
point_b = 0

# カードから点数の計算
def getPoint(card):
    if card % 13 == 0:
        return 13
    else:
        return card % 13

# カードを引いて点数を返す
def drawCard():
    # cardsをシャッフル
    random.shuffle(cards)

    # cardsの先頭を引く
    card = cards[0]
    print('{0}です。'.format(card))
    # cardsの先頭を削除
    del cards[0]
    return getPoint(card)

def judge():
    if point_a < 21 and point_b < 21:
        return None
    else:
        abs_a = abs(21 - point_a)
        abs_b = abs(21 - point_b)
        if abs_a > abs_b:
            return 'B'
        elif abs_a < abs_b:
            return 'A'
        else:
            return None

winner = None
while winner == None:
    print('Aさんがカードを引きます。Aさんのカードは', end='')
    point_a += drawCard()
    print('Bさんがカードを引きます。Bさんのカードは', end='')
    point_b += drawCard()
    winner = judge()

print('{0}さんの勝ちー。'.format(winner))
