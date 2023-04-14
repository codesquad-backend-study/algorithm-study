def solution(orders, course):
    course_menu = []
    
    for num in course:
        global combi_dict
        combi_dict = {}
        for order in orders:
            if len(order) < num:
                continue
            
            combinationOrder("", order, num)
        
        if len(combi_dict) > 0:
            combi_dict = sorted(combi_dict.items(), key=lambda x : -x[1])
            
            max = combi_dict[0][1]
            for combi in combi_dict:
                if max >= 2 and max == combi[1]:
                    course_menu.append(combi[0])

    return sorted(course_menu)
            
def combinationOrder(word, order, count):
    if count == 0:
        word = sorted(word)
        combi_dict["".join(word)] = combi_dict.get("".join(word), 0) + 1
        return
    for i in range(len(order)):
        combinationOrder(word + str(order[i]), order[i+1:], count-1)
            
# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["XYZ", "XWY", "WXA"], [2,3,4])