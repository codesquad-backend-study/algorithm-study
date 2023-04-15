def solution(m, musicinfos):
    umm = {'C#':'0', 'D#':'1', 'F#':'2', 'G#':'3', 'A#':'4'}
    sequence = {}
    # m과 musicinfos의 음을 umm의 value로 변경
    for u in umm :
        m = m.replace(u,umm[u])

    for i in range(len(musicinfos)) : # 계이름 바꾸고, 제목:순서 저장
        music = musicinfos[i][3]
        for u in umm :
            music = music.replace(u,umm[u])
        musicinfos[i][3] = music
        title = musicinfos[i][2]
        sequence[title] = i

    runtime = {}

    for info in musicinfos : # 음악 총 시간 계산, 제목:시간 저장
        h1, m1 = info[0].split(':')
        h2, m2 = info[1].split(':')
        if h2 == '00' and m2 == '00':
            h2 = '24'
        t1 = int(h1)*60+int(m1)
        t2 = int(h2)*60+int(m2)
        runtime[info[2]] = t2-t1

    # 음악 시간만큼 붙이기

    for _, _, mu, music in musicinfos :
        t = runtime[mu]
        if t > len(music) :
            music = music*(t//len(music))
            tmp = music[:t%len(music)]
            music += tmp

    # 포함되는 것 찾기

    corr = []
    for _,_,title,music in musicinfos :
        if m in music :
            corr.append(title)

    if len(corr) == 0 :
        return 'None'
    elif len(corr) == 1 :
        return title
    title = ''
    max = 0
    cnt = 0
    for c in corr :
        if runtime[c] > max :
            max = runtime[c]
            title = c
            cnt = 1
        elif runtime[c] == max :
            cnt += 1
    if cnt == 1 :
        return title

    for c in corr :
