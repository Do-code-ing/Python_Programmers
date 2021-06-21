# https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    # 기억하고 있는 음에 대해 변환
    def transform(string):
        # 음별 데이터 테이블
        table = {
            "C#":"c",
            "D#":"d",
            "F#":"f",
            "G#":"g",
            "A#":"a",
            "E#":"e"
        }
        # 데이터 테이블에 따라 입력값 변환
        melody = []
        for i in range(len(string)-1):
            if string[i+1] == "#":
                melody.append(table[string[i]+"#"])
            elif string[i] != "#":
                melody.append(string[i])
        if string[-1] != "#":
            melody.append(string[-1])
        
        return "".join(melody)
    
    # 재생시간 계산
    def cal(time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)
    
    # 계산 시작
    m = transform(m)
    song = {}
    for music in musicinfos:
        start, end, name, melody = music.split(",")
        start, end, melody = cal(start), cal(end), transform(melody)
        temp, n = end-start, len(melody)
        melody = melody * (temp//n) + melody[:temp%n]
        song[name] = melody

    answer, time = "", ""
    for name, melody in song.items():
        if m in melody and len(melody) > len(time):
            answer = name
            time = melody
        
    return answer if answer else "(None)"