from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20260402.xml")

soup = BeautifulSoup(target, "html.parser")
for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()