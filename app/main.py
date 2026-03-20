cards={
'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

print("Это помощник для покера.")
print("Введите Вашу руку. \n Номинал: 2 3 4 5 6 7 8 9 10 J Q K A \n Масть: Пики - spades  Черви - hearts  Бубны -  diamonds  Черви - clubs ")
print(" s h d c")
hand1,hand2=input().upper().split()

if hand1[:-1] in cards and hand2[:-1] in cards:
    yc1,yc2=[hand1[:-1],hand2[:-1]]
    ys1,ys2=[hand1[-1],hand2[-1]]

    urhand = sorted([yc1, yc2], key=lambda x: cards[x], reverse=True)

    group1 = ['AA', 'KK', 'QQ', 'JJ', 'TT', 'AK']
    group2 = ['AQ', 'AJ', 'KQ', '99', '88']
    group3 = ['A9', 'A8',  # Туз с 9 или 8
    'K9', 'K8',  # Король с 9 или 8
    'Q9', 'Q8',  # Дама с 9 или 8
    'J9', 'J8',  # Валет с 9 или 8
    'T9', 'T8',  # Десятка с 9 или 8
    '98' ]
    low_pairs = ['77', '66', '55', '44', '33', '22']

    hand_str = "".join(urhand)
    is_suited = (ys1 == ys2)
    if hand_str in group1 or hand_str in group2:
        print("Хорошие карты. Рейз")
    elif is_suited and hand_str in group3:
        print("Карты сойдут. Рейз")
    elif hand_str in low_pairs:
        print("Можно попытаться.Пара.")
    else:
        print("Пасс")

    print("Этап Флопа. Введите 3 карты и их масти.")
    f1,f2,f3=input().upper().split()

    if f1[:-1] in cards and f2[:-1] in cards and f3[:-1] in cards:
        flopcard=f1[:-1],f2[:-1],f3[:-1]
        flopsuit=f1[-1],f2[-1],f3[-1]
        print(flopcard,flopsuit)
else:
    print("Это не номинал карт.")