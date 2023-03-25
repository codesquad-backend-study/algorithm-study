def solution(msg):
    # (출력 -> 사전 등록) 이 순서를 잘 기억하자
    # "사전 색인 번호"를 배열로 출력하자
    answer = []

    # 노가다로 {색인번호: 단어} 형태의 딕셔너리 생성
    # my_dict = {
    #     1: 'A',
    #     2: 'B',
    #     3: 'C',
    #     4: 'D',
    #     5: 'E',
    #     6: 'F',
    #     7: 'G',
    #     8: 'H',
    #     9: 'I',
    #     10: 'J',
    #     11: 'K',
    #     12: 'L',
    #     13: 'M',
    #     14: 'N',
    #     15: 'O',
    #     16: 'P',
    #     17: 'Q',
    #     18: 'R',
    #     19: 'S',
    #     20: 'T',
    #     21: 'U',
    #     22: 'V',
    #     23: 'W',
    #     24: 'X',
    #     25: 'Y',
    #     26: 'Z'
    # }

    # -> {단어: 색인번호}의 형태로 다시 바꿈
    # 결국 단어를 기준으로 색인번호를 뽑아내는 게 맞으니
    my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
               'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
               'P': 16, 'Q': 17, 'R': 18, 'S': 19,
               'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    my_dict_index = 26

    # 압축 알고리즘은 대문자만 처리
    msg = msg.upper()

    # 이제 계속 색인 번호를 answer에 저장해주면서 my_dict에 사전 추가해주자
    # my_dict에 추가해 줄 때 이미 26인 my_dict_index를 가지고 하나씩 추가해주면서 key에 넣어주자!
    tmp_word = ''
    for word in msg:
        tmp_word += word

        # 만약 tmp_word가 사전에 없다면 무조건 tmp_word가 2글자임
        # 그 tmp_word를 사전에 value로 추가해주면 됨
        # 근데 dict에서 'in'의 기준이 key일까 value일까?
        # 여기서 원하는 건 단어인 key를 기준으로 뽑아내는 거 -> 상황에 따라 key와 value 자리 바꿔도 됨
        if tmp_word not in my_dict:
            my_dict_index += 1
            my_dict[tmp_word] = my_dict_index

            # 초기화 해주기 전에 전 index의 word 출력
            answer.append(my_dict[tmp_word[0]])

            # tmp_word를 완전 초기화해주는 게 아니라 다음 배열을 위해 현재 word를 저장해줘야지
            tmp_word = word

        # 만약 사전에 이미 존재하는 경우 3,4,5..글자 가능
        else:  # tmp_word in my_dict:
            my_dict_index += 1
            my_dict[tmp_word] = my_dict_index

            # 초기화 해주기 전에 전 index의 word 출력
            tmp_len = len(tmp_word)
            answer.append(my_dict[tmp_word[:tmp_len]])

            # 얘도 똑같이 현재 word 저장
            tmp_word = word

    return answer


print(solution('KAKAO'))
