def convertHourToMin(time):
    h, m = list(map(int,(time.split(':'))))
    return h*60 + m

def change(melody):
    melody = melody.replace('C#','c')
    melody = melody.replace('D#','d')
    melody = melody.replace('F#','f')
    melody = melody.replace('G#','g')
    melody = melody.replace('A#','a')
    return melody

def solution(m, musicinfos):
    
    music_info = []
    m = change(m)
    
    for index, musicinfo in enumerate(musicinfos):
        start, end, music_name, melody = musicinfo.split(',')
        play_time = convertHourToMin(end) - convertHourToMin(start)
        melody = change(melody)
        
        
        if play_time < len(melody):
            melody = melody[:play_time]
            music_info.append((play_time, music_name, melody, index))
        else:
            melody = (melody * (play_time // len(melody)) + melody[:play_time%len(melody)])
            music_info.append((play_time, music_name, melody, index))
        
    music_info = [music_info[i] for i in range(len(music_info)) if m in music_info[i][2]]
    music_info = sorted(music_info, reverse=True, key = lambda x : [x[0], -x[3]])
    
    return music_info[0][1] if music_info else "(None)"