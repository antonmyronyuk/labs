from bs4 import BeautifulSoup
import urllib.request


class MyList:
    def __init__(self):
        self.list = list()

    def __getitem__(self, index):
        return self.list[index - 1]

    def __setitem__(self, index, value):
        self.list[index - 1] = value

    def __len__(self):
        return len(self.list)

    def append(self, item):
        self.list.append(item)


class Leaderboard:
    def __init__(self):
        self.users = MyList()

    def add_user(self, user):
        self.users.append(user)

    @property
    def position(self):
        return self.users


class User:
    def __init__(self, name, clan, honor):
        self.name = name
        self.clan = clan or ''
        self.honor = int(honor)


def get_user_info(table_row):
    # td: 0 - rank, 1 - username, 2 - clan, 3 - honor
    table_items = table_row.find_all('td')
    name = table_items[1].a.contents[1]
    clan = table_items[2].string
    honor = table_items[3].string
    return User(
        name=name,
        clan=clan,
        honor=honor
    )


url = 'https://www.codewars.com/users/leaderboard'
file = urllib.request.urlopen(url).read()
soup = BeautifulSoup(file, 'html.parser')


if __name__ == '__main__':
    '''
    print(soup.prettify())
    items = soup.find_all('td', {'class': 'is-big'})
    usernames = [it.a.contents[1] for it in items]

    print('\n'.join(map(str, usernames)))
    print(len(usernames))
    '''
    leaderboard = Leaderboard()
    items = soup.find_all('tr')[1:]
    for it in items:
        leaderboard.add_user(get_user_info(it))
    print(leaderboard.position[1].name)
