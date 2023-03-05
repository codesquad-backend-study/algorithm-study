def solution(today, terms, privacies):
    answer = []
    
    year, month, day = map(int, today.split("."))
    today = (year * 12 * 28 + month * 28 + day)
    
    terms_data = {}
    for s in terms:
        term = s.split()
        terms_data[term[0]] = int(term[1])

    for i, s in enumerate(privacies, start=1):
        privacies_data = s.split()
        date = list(map(int, privacies_data[0].split(".")))
        type = privacies_data[1]
        
        privacy_day = (date[0] * 12 * 28) + (date[1] * 28) + date[2]
        privacy_day += terms_data[type] * 28
        
        if today >= privacy_day:
            answer.append(i)
    
    return answer


result = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
print(result)