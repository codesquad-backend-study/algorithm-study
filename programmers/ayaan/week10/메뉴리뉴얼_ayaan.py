from itertools import combinations

def solution(orders, course):
    result = []
    menu = []
    for order in orders:
        menu += order
    menu = set(menu)
    
    for num in course:
        menu_combination_list = list(combinations(menu, num))
        for menu_combination in menu_combination_list:
            count = 0
            
            for order in orders:
                include = 0
                for i in range(num):
                    if menu_combination[i] not in order:
                        break
                    include += 1
                    
                    if include == num:
                        count += 1
                
                if count == 2:
                    course_menu = []
                    for i in range(num):
                        course_menu.append(menu_combination[i])
                    result.append(course_menu)
                    break
    print(result)
            
            
    
    
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])