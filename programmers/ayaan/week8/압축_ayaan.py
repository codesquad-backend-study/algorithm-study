def solution(msg):
    # A~Z까지 dictionary 초기화
    dictionary = {chr(i+ord('A')-1):i for i in range(1,27)}

    def findWord(dictionary, msg, idx, plus):
        if msg[idx:idx + plus + 1] in dictionary.keys():
            print(findWord(dictionary, msg, idx, plus+1))
        else:
            dictionary[msg[idx:idx+plus+1]] = len(dictionary.keys())+1
            return dictionary[msg[idx:idx+plus]]
            
    for i in range(len(msg)):
        findWord(dictionary, msg, i, 0)
    
    
        
    

msg = "KAKAO"
# msg = "TOBEORNOTTOBEORTOBEORNOT"
solution(msg)