import re
def solution(m, musicinfos):
    new_dict = {
        'C#': 'H',
        "D#": 'I',
        "F#":'J',
        "G#":'K',
        "A#":'L',
    }
    
    musics = []
    for musicinfo in musicinfos:
        splited_info = musicinfo.split(',')
        start = splited_info[0].split(':')
        start_time = int(start[0])*60+int(start[1])
        end = splited_info[1].split(':')
        end_time = int(end[0])*60+int(end[1])
        run_time = end_time - start_time
        title = splited_info[2]
        mel = splited_info[3]
        for item in new_dict:
            mel = mel.replace(item, new_dict[item])
        mel = re.findall(r'[A-Z]{1}#*', mel)
        musics.append((title, mel, run_time))
        
    results = []
    for idx, music in enumerate(musics):
        music_runs = music[1]*(music[2]//len(music[1]))+music[1][:music[2]%len(music[1])]
        for item in new_dict:
            m = m.replace(item, new_dict[item])
        if m in "".join(music_runs):
            results.append(idx)
    if results == []:
        return "(None)"
    max_title = ""
    max_runtime = 0
    for idx in results:
        result = musics[idx]
        if max_runtime < result[2]:
            max_title = result[0]
            max_runtime = result[2]
            
    answer = max_title
    return answer