import re
"""
  [STEP]
  1. 각 html의 주소 추출
  2. 해당 페이지의 점수 체크
  3. 연결된 링크 체크 후 적재
  4. 점수 계산
"""
def solution(word, pages):
    total_score = []
    basic_score = {} # 각 html의 점수 적재
    exlink_cnt = {}  # 링크 갯수
    to_me_link = {}  # 페이지에 연결되어있는 링크 적재하기
    
    for page in pages:
        title = re.search('<meta property="og:url" content="(https://\S+)"', page).group(1)
        basic_score[title] = 0
        exlink_cnt[title] = 0
        
        # 기본 점수 체크
        for find in re.findall('[a-zA-Z]+', page):
            if find.upper() == word.upper():
                basic_score[title] += 1
                
        # 현재 페이지를 to_me_link에 연결해주기 -> 결과적으로 각 페이지에 연결된 페이지를 체크할 수 있음
        for link in re.findall('<a href="(https://\S+)"', page):
            exlink_cnt[title] += 1
            if link in to_me_link:
                to_me_link[link].append(title)
            else:
                to_me_link[link] = [title]
                
    for curr in basic_score:
        link_score = 0
        if curr in to_me_link:
            for ex in to_me_link[curr]:
                link_score += basic_score[ex] / exlink_cnt[ex]
        total_score.append(basic_score[curr] + link_score)
        
    return total_score.index(max(total_score))
