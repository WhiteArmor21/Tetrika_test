import requests
from bs4 import BeautifulSoup


url = 'https://inlnk.ru/jElywR'


def _get_links(soup, result):
    next_page = ''
    links = soup.find_all('li')[2:-63]
    for link in links:
        try:
            animal = link.find('a').get('title')
        except AttributeError:
            break
        if animal[0] != 'H':  # For some reason, one page with Eng letter "H" found among the pages in Russian
            if animal[0] == 'A':  # Finish collecting when found first Eng letter
                return False
            if animal[0] not in result.keys():
                print(f'Collecting animals with the letter: {animal[0]}')
                result[animal[0]] = 0
            result[animal[0]] += 1
        next_page = _get_next_page(soup)
    return next_page


def _get_next_page(soup):
    next_page = 'https://ru.wikipedia.org'
    for link in soup.find(id='mw-pages').find_all('a'):
        if link.text == 'Следующая страница':
            next_page += link.get('href')
            break
    return next_page


def _print_result(result):
    for key in sorted(list(result.keys())):
        print('{}: {}'.format(key, result[key]))


def main():
    result = {'А': 0}
    page = url
    print('Collecting animals with the letter: А')
    while page:
        soup = BeautifulSoup(requests.get(page).content, 'lxml')
        page = _get_links(soup, result)
    print('Done')
    _print_result(result)


if __name__ == '__main__':
    main()
