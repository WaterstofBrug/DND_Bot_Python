import bs4 as soup
import requests


def scrape_info_creature(creature):
    url = f'https://roll20.net/compendium/dnd5e/{creature}#content'
    r = requests.get(url)
    x = soup.BeautifulSoup(r.content, 'html.parser')
    info_elements_rough = x.findAll('div', {'class': 'row attrListItem'})
    info_elements = []

    for list in info_elements_rough:
        if len(list) > 1:
            list_refined = list.findAll('div', {'class': ['attrName', 'attrValue']})
            for info in list_refined:
                info_elements.append(info.text)
        else:
            info_elements.append(list.text)

    info = ''
    for i, element in enumerate(info_elements):
        if i % 2 == 0:
            binder = '\n'
        else:
            binder = ': '
        info = binder.join((info, element.strip('\n')))

    return info

def scrape_info_rules(rule):
    url = f'https://roll20.net/compendium/compendium/whichone/dnd5e/{rule}'
    r = requests.get(url)

    


print(retrieve_info_creature('Hydra'))