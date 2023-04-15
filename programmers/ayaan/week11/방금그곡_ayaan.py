def solution(m, musicinfos):
    playList = {}
    
    for musicinfo in musicinfos:
        musicinfo = musicinfo.split(",")
        start_time = list(map(int, musicinfo[0].split(":")))
        end_time = list(map(int, musicinfo[1].split(":")))
        play_time = (end_time[0]*60 + end_time[1]) - (start_time[0]*60 + start_time[1])
        
        info = musicinfo[3]
        play_music_info = ""
        if play_time > len(info):
            play_music_info = info * (play_time // len(info))
            if play_time % len(info) != 0:
                play_music_info += info[0:play_time % len(info)]
        else:
            play_music_info = info[0:play_time]
        print(play_music_info)    
        playList[musicinfo[2]] = play_music_info
    
    answer = ""
    max_time = 0
    for title, play_music_info in playList.items():
        if m in play_music_info:
            if m+"#" in play_music_info:
                continue
            if max_time < len(play_music_info):
                max_time = len(play_music_info)
                answer = title
    print(answer)
    return answer

solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])