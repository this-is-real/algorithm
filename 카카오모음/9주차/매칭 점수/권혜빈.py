import re

def solution(word, pages):
    page = []
    pageName = []
    graph = dict()

    for p in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', p).group(1)
        basic_score = 0
        for f in re.findall(r'[a-zA-Z]+', p.lower()):
            if f == word.lower():
                basic_score += 1
        ex_Link = re.findall('<a href="(https://[\S]*)"', p)

        for link in ex_Link:
            if link not in graph.keys():
                graph[link] = [url]
            else:
                graph[link].append(url)

        pageName.append(url)
        page.append([url, basic_score, len(ex_Link)])

    max_score = 0
    result = 0

    for i in range(len(page)):
        url = page[i][0]
        score = page[i][1]

        if url in graph.keys():
            for link in graph[url]:
                a, b, c = page[pageName.index(link)]
                score += (b / c)
        if max_score < score:
            max_score = score
            result = i
    
    return result
