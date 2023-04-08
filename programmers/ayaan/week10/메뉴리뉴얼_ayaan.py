from itertools import combinations

def solution(orders, course):
    course_menu = []
    
    for num in course:
        combi_dict = {}
        for order in orders:
            if len(order) < num:
                continue
            for combination in list(combinations(order, num)):
                combination = sorted(combination)
                combi_dict["".join(combination)] = combi_dict.get("".join(combination), 0) + 1
        
        if len(combi_dict) > 0:
            combi_dict = sorted(combi_dict.items(), key=lambda x : -x[1])
            
            max = combi_dict[0][1]
            for combi in combi_dict:
                if max >= 2 and max == combi[1]:
                    course_menu.append(combi[0])
        
    return sorted(course_menu)
            
            
# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["XYZ", "XWY", "WXA"], [2,3,4])