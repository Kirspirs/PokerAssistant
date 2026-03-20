cards = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}
#НАЧАЛО
print("Это помощник для покера.")
print("Введите Вашу руку (например: As Ks):")
hand1, hand2 = input().upper().split()

# ПРОВЕРКА И АНАЛИЗ ПРЕФЛОПА
if hand1[:-1] in cards and hand2[:-1] in cards:
    yc1, yc2 = hand1[:-1], hand2[:-1]
    ys1, ys2 = hand1[-1], hand2[-1]

    urhand = sorted([yc1, yc2], key=lambda x: cards[x], reverse=True)
    hand_str = "".join(urhand)
    is_suited = (ys1 == ys2)

    # ГРУППЫ КАРТ ДЛЯ ПРЕФЛОПА
    group1 = ['AA', 'KK', 'QQ', 'JJ', '1010', 'AK']
    group2 = ['AQ', 'AJ', 'KQ', '99', '88']
    group3 = ['A9', 'A8', 'K9', 'K8', 'Q9', 'Q8', 'J9', 'J8', '109', '108', '98']
    low_pairs = ['77', '66', '55', '44', '33', '22']

    if hand_str in group1 or hand_str in group2:
        print(">>> Хорошие карты. Рейз")
    elif is_suited and hand_str in group3:
        print(">>> Карты сойдут. Рейз")
    elif hand_str in low_pairs:
        print(">>> Можно попытаться. Пара.")
    else:
        print(">>> Пасс")

    # ЭТАП ФЛОПА (3 КАРТЫ)
    print("\nЭтап Флопа. Введите 3 карты (например: 8d 10d 3c):")
    f1, f2, f3 = input().upper().split()

    if f1[:-1] in cards and f2[:-1] in cards and f3[:-1] in cards:
        all_cards = [yc1, yc2, f1[:-1], f2[:-1], f3[:-1]]
        all_suits = [ys1, ys2, f1[-1], f2[-1], f3[-1]]

        # АНАЛИЗ КОМБИНАЦИЙ НА ФЛОПЕ
        p_count = 0
        s_found = False
        q_found = False

        for val in set(all_cards):
            c = all_cards.count(val)
            if c == 4:
                q_found = True
            elif c == 3:
                s_found = True
            elif c == 2:
                p_count += 1

        if q_found:
            print("ИТОГ ФЛОПА: КАРЕ!")
        elif s_found and p_count >= 1:
            print("ИТОГ ФЛОПА: ФУЛЛ-ХАУС!")
        elif s_found:
            print("ИТОГ ФЛОПА: СЕТ")
        elif p_count >= 2:
            print("ИТОГ ФЛОПА: ДВЕ ПАРЫ")
        elif p_count == 1:
            print("ИТОГ ФЛОПА: ПАРА")
        else:
            print("ИТОГ ФЛОПА: Старшая карта")

        # ЭТАП ТЕРН (4-Я КАРТА)
        print("\n--- ЭТАП ТЕРН ---")
        turn_raw = input("Введите 4-ю карту (например, 2h): ").upper()

        if turn_raw[:-1] in cards:
            # ОБНОВЛЕНИЕ СПИСКОВ КАРТ
            all_cards.append(turn_raw[:-1])
            all_suits.append(turn_raw[-1])
            print(f"Карты для анализа: {all_cards}")

            # АНАЛИЗ КОМБИНАЦИЙ НА ТЕРНЕ
            p_count = 0
            s_found = False
            q_found = False
            for val in set(all_cards):
                c = all_cards.count(val)
                if c == 4:
                    q_found = True
                elif c == 3:
                    s_found = True
                elif c == 2:
                    p_count += 1

            if q_found:
                print("ИТОГ ТЕРНА: КАРЕ!")
            elif s_found and p_count >= 1:
                print("ИТОГ ТЕРНА: ФУЛЛ-ХАУС!")
            elif s_found:
                print("ИТОГ ТЕРНА: СЕТ")
            elif p_count >= 2:
                print("ИТОГ ТЕРНА: ДВЕ ПАРЫ")
            elif p_count == 1:
                print("ИТОГ ТЕРНА: ПАРА")
            else:
                print("ИТОГ ТЕРНА: Старшая карта")

            # ЭТАП РИВЕР (5-Я КАРТА)
            print("\n--- ЭТАП РИВЕР ---")
            river_raw = input("Введите 5-ю карту (например, As): ").upper()

            if river_raw[:-1] in cards:
                # ОБНОВЛЕНИЕ СПИСКОВ КАРТ (ФИНАЛ)
                all_cards.append(river_raw[:-1])
                all_suits.append(river_raw[-1])

                # ФИНАЛЬНЫЙ АНАЛИЗ КОМБИНАЦИЙ
                p_count = 0
                s_found = False
                q_found = False
                for val in set(all_cards):
                    c = all_cards.count(val)
                    if c == 4:
                        q_found = True
                    elif c == 3:
                        s_found = True
                    elif c == 2:
                        p_count += 1

                print(f"\nФИНАЛЬНЫЙ НАБОР: {all_cards}")
                if q_found:
                    print("ИТОГ РИВЕРА: КАРЕ!")
                elif s_found and p_count >= 1:
                    print("ИТОГ РИВЕРА: ФУЛЛ-ХАУС!")
                elif s_found:
                    print("ИТОГ РИВЕРА: СЕТ")
                elif p_count >= 2:
                    print("ИТОГ РИВЕРА: ДВЕ ПАРЫ")
                elif p_count == 1:
                    print("ИТОГ РИВЕРА: ПАРА")
                else:
                    print("ИТОГ РИВЕРА: Старшая карта")
            else:
                print("Ошибка в номинале Ривера.")
        else:
            print("Ошибка в номинале Терна.")
    else:
        print("Ошибка в номинале Флопа.")
else:
    print("Ошибка в номинале Руки.")
