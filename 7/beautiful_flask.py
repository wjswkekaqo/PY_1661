from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def books():
    # Books to Scrape 페이지 요청
    req = request.Request(
        "https://books.toscrape.com/",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response = request.urlopen(req)
    soup = BeautifulSoup(response, "html.parser")

    # 책 목록 추출
    output = "<h1>Books to Scrape 도서 목록</h1>"
    books = soup.select("article.product_pod")

    for i, book in enumerate(books[:10], 1):
        title  = book.select_one("img.thumbnail")
        price  = book.select_one("p.price_color")
        rating = book.select_one("p.star-rating")

        title_text  = title["alt"] if title else "제목 없음"
        price_text  = price.get_text(strip=True) if price else "가격 없음"
        rating_text = rating["class"][1] if rating else "별점 없음"

        output += "<h3>{}. {}</h3>".format(i, title_text)
        output += "가격: {}<br/>".format(price_text)
        output += "별점: {}<br/>".format(rating_text)
        output += "<hr/>"

    return output