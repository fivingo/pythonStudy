"""인터넷 아카이브에서 부분 제목으로 영화를 찾아서 브라우저에 표시한다."""

import sys
import webbrowser
import requests

def search(title):
    """제목이 부분적으로 일치하는 영화에 대한 3가지 항목 튜플 (identifier, title, description) 리스트를 반환한다"""
    search_url = "http://archive.org/advancedsearch.php"
    params = {
        "q": "title:({}) AND mediatype:(movies)".format(title),
        "fl": "identifier,title,description",
        "output": "json",
        "rows": 10,
        "page": 1,
    }
    resp = requests.get(search_url, params=params)
    data = resp.json()
    docs = [(doc["identifier"], doc["title"], doc["description"])
            for doc in data["response"]["docs"]]
    return docs

def choose(docs):
    """docs의 각 튜플의 줄 번호, 제목, 축약된 설명을 출력한다.
    사용자가 줄 번호를 선택하도록 한다.
    줄 번호가 유요하면 튜플의 첫 번째 항목(identifier)를 반환한다.
    그렇지 않으면 None을 반환한다."""
    last = len(docs) - 1
    for num, doc in enumerate(docs):
        print(f"{num}: ({doc[1]}) {doc[2][:30]}...")
    index = input(f"Which would you like to see (0 to {last})? ")
    try:
        return docs[int(index)][0]
    except:
        return None

def display(identifier):
    """인터넷 아카이브에서 identifier를 사용하여 브라우저에 영화를 표시한다."""
    details_url = "http://archive.org/details/{}".format(identifier)
    print("Loading", details_url)
    webbrowser.open(details_url)

def main(title):
    """제목과 일치하는 영화를 찾는다.
    사용자가 선택한 것을 브라우저에 표시한다."""
    identifiers = search(title)
    if identifiers:
        identifier = choose(identifiers)
        if identifier:
            display(identifier)
        else:
            print("Nothing selected")
    else:
        print("Nothing found for", title)

if __name__ == "__main__":
    main(sys.argv[1])
