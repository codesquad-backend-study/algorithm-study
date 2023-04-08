orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
# 메뉴 개수

result = ["AC", "ACDE", "BCFG", "CDE"]
# 코스 메뉴 구성

menu_counter = {}
for order in orders:
    for menu in order:
        if menu not in menu_counter:
            menu_counter[menu] = 1
        else:
            menu_counter[menu] += 1

menu_counter = sorted(menu_counter.items(), key=lambda x: x[1], reverse=True)
print(menu_counter)

menu_guest = {}

for idx, order in enumerate(orders):
    for menu in order:
        if menu not in menu_guest:
            menu_guest[menu] = []

        menu_guest[menu].append(idx)

print(menu_guest)

ans = []
for menu, menu_count in menu_counter:
    tmp = []
    for cut in course:
        if cut <= menu_count:

            maximum = 0
            fivot_guests = menu_guest[menu]
            for other_menu, other_menu_count in menu_counter:
                if menu == other_menu:
                    continue

                other_guests = menu_guest[other_menu]

                fivot_guests.





