import wikipediaapi
import time

user_agent = "wikithing (yo0225jo0823@pusd.us)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(startPage,targetPage):
    links = fetch_links(startPage)

    for thing in links:
        if thing==targetPage.title:
            print("We found it!!11!1")
            break


startPage = wiki.page("Water bottle")
targetPage = wiki.page("Carboy")
wikipedia_game_solver(startPage,targetPage)

print(fetch_links(startPage))