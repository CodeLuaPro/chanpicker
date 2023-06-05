import requests
import json
import random
from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

boards = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'gif', 'h', 'hr', 'k', 'm', 'o', 'p', 'r', 's', 't', 'u', 'v', 'vg', 'vm', 'vmg', 'vr', 'vrpg', 'vst', 'w', 'wg', 'i', 'ic', 'r9k', 's4s', 'vip', 'wa', 'cm', 'hm', 'lgbt', 'y', '3', 'aco', 'adv', 'an', 'bant', 'biz', 'cgl', 'ck', 'co', 'diy', 'fa', 'fit', 'gd', 'hc', 'his', 'int', 'jp', 'lit', 'mlp', 'mu', 'n', 'news', 'out', 'po', 'pol', 'pw', 'qst', 'sci', 'soc', 'sp', 'tg', 'toy', 'trv', 'tv', 'vp', 'vt', 'wsg', 'wsr', 'x', 'xs']

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def pick_board():
    return random.choice(boards)

def generate_thread():

    text = strip_tags(r_d[random_page]['threads'][random_thread].get('com'))
    id = int(r_d[random_page]['threads'][random_thread].get('no'))
    print("\n")
    print(text)
    print(id)
    board_input = input("Press Enter to generate thread")
    
board_input = input("Press Enter to generate thread")

while True:
    
    random_board = pick_board()

    random_page = random.randint(0, 9)
    random_thread = random.randint(0, 15)

    r = requests.get("https://a.4cdn.org/{}/catalog.json".format(random_board))
    r_d = r.json()

    try:
        generate_thread()
    except:
        pass