import googlesearch
import requests
from bs4 import BeautifulSoup
import re
import random
from gen_response_helper import gen_response

def web_search(search_query):
    search_response = ""
    try:
        blacklist = ["cloudfare" , "ray id" ]

        try: 
            search_results = googlesearch.search(search_query, num_results=5)
            links = list(search_results) 
        except Exception:
            response = requests.get(f"https://www.google.com/search?q={search_query}")
            soup = BeautifulSoup(response.content, 'html.parser')
            links = []
            for link in soup.find_all('a'):
                if len(links) > 5:
                    break
                href = link.get('href')
                if href.startswith('/url?q='):
                    links.append(href[7:])
            if links == []:
                response = requests.get(f"https://www.bing.com/search?q={search_query}")
                soup = BeautifulSoup(response.content, 'html.parser')
                trackers = ['privacy', 'microsoft', 'tracker' , "bing"]
                for link in soup.find_all('a'):
                    if len(links) > 5:
                        break
                    href = link.get('href')
                    if href.startswith('http') or href.startswith('https'):
                        if not any(tracker in href for tracker in trackers):
                            links.append(href)

        if len(links) == 0:
            print("No links")
            return ""
        
        while len(links) > 0:  
            url = random.choice(links)  
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            text = ' '.join([elem.text for elem in soup.find_all()])
            text = re.sub(' +', ' ', text)
            if any(keyword in text.lower() for keyword in blacklist):
                links.remove(url)  
                if len(links) == 0:
                    return ""
                continue
            break
    
        lines = re.split('\n|\.', text)
        lines = [line.strip() for line in lines if line.strip() != '']
        lines = [line for line in lines if len(line.split()) >= 10]

        patience = 3
        iterations = 0
        for line in lines:
            if iterations < patience:
                iterations += 1
                prompt = "search query: " + search_query + "response:" + line + "Does response have information related to the search query Yes/No:"
                response = gen_response(prompt , "text-davinci-003", ["\\n"], 10).replace("\n" , "")
                if response == "No":
                    continue
                if response == "Yes":
                    search_response = search_response + line + " "
            break
    except Exception as e:
        search_response = ""
    return search_response