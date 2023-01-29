from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, "html.parser")
articles = soup.find_all(name="a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_vote = [int(score.getText().split(" ")[0])
                for score in soup.find_all(name="span", class_="score")]

article_links = article_links[11:]
article_links = [url
                 for url in article_links
                 if url.startswith("https://") or url.startswith("http://")]

article_texts = article_texts[11:]
article_texts_length = len(article_texts)
new_article_texts = [article_texts[i]
                     for i in range(0, article_texts_length)
                     if i % 7 == 0]

max_vote = max(article_vote)
max_vote_index = article_vote.index(max_vote)

print(article_vote[max_vote_index])
print(article_links[max_vote_index])
print(new_article_texts[max_vote_index])
