# import os
# import json
# import requests
# from langchain.tools import tool


# class SearchTools():

#   @tool("Search the internet")
#   def search_internet(query):
#     """Useful to search the internet 
#     about a a given topic and return relevant results"""
#     url = "https://google.serper.dev/search"
#     payload = json.dumps({
#       "q": "네이버웹툰 AI",
#       "location": "Seoul, South Korea",
#       "gl": "kr",
#       "hl": "ko",
#       "num": 50,
#       "tbs": "qdr:d"
#     })
#     headers = {
#         'X-API-KEY': os.environ['SERPER_API_KEY'],
#         'content-type': 'application/json'
#     }
#     response = requests.request("POST", url, headers=headers, data=payload)
#     results = response.json()['organic']
#     string = []
#     for result in results:
#       string.append('\n'.join([
#           f"Title: {result['title']}", f"Link: {result['link']}",
#           f"Snippet: {result['snippet']}", "\n-----------------"
#       ]))

#     return '\n'.join(string)


import os
import http.client
import json
from langchain.tools import tool


class SearchTools():

  @tool("Search the internet")
  def search_internet(query):
    """Useful to search the internet 
    about a a given topic and return relevant results"""
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({
      "q": "naver webtoon ai",
      "location": "Seoul, South Korea",
      "gl": "kr",
      "hl": "ko",
      "num": 50,
      "tbs": "qdr:d"
    })
    headers = {
      'X-API-KEY': os.environ['SERPER_API_KEY'],
      'Content-Type': 'application/json'
    }
    conn.request("POST", "/news", payload, headers)
    res = conn.getresponse()
    data = res.read()
    results = data.decode("utf-8")["news"]
    return results
    # print(results)
    # string = []
    # for result in results:
    #   string.append('\n'.join([
    #       f"Title: {result['title']}", f"Link: {result['link']}",
    #       f"Snippet: {result['snippet']}", "\n-----------------"
    #   ]))

    # return '\n'.join(string)
