#!/usr/bin/env python 

from __future__ import print_function 
from bs4 import BeautifulSoup as bs
import lxml
# python 2/3 compatibility
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


import time
import io
import pyperclip

    
def get_plays(username,thing_id,date):
    url = "http://www.boardgamegeek.com/xmlapi2/plays?username={0}&mindate={1}&id={2}".format(
           username, date, thing_id)
    page=urllib2.urlopen(url)
    soup=bs(page,'xml')
    return soup

def get_list(id):
    url = 'http://www.boardgamegeek.com/xmlapi/geeklist/{0}'.format(id)
    page=urllib2.urlopen(url)
    soup=bs(page,'xml')
    thing_ids = [(item.attrs['objectname'],item.attrs['objectid']) for item in soup.findAll('item')]
    time.sleep(1)
    return thing_ids

def create_post(username, thing_id, date):

    thing_ids = get_list(geeklist_id)
    s = io.StringIO()

    for name,thing_id in thing_ids:
        #print(name + " *********** ")
        print(u'[b][u][thing={0}]{1}[/thing][/b][/u]'.format(thing_id,name),file=s)
        soup = get_plays(username,thing_id,date)
        num_stars = sum([int(play.attrs['quantity']) for play in soup.findAll('play')])
        print(u':star:'*num_stars,end=u'',file=s)
        if num_stars < 10:
            print(u':nostar:'*(10-num_stars),end=u'',file=s)
        print(u'',file=s)
        for play in soup.findAll('play'):

            #print(play)

            comments =""
            if play.find("comments"):
                comments = play.find('comments').contents[0]
            #print(play.attrs['id'])
            if play.attrs['incomplete'] == '0':
                print(u"[u]{0}[/u] (x{1}): {2}".format(play.attrs['date'],
                                               play.attrs['quantity'],
                                               comments), file=s)
        print(u'',file=s)
        # bgg doesn't like when you hit the database really fast
        # let's play it SUPER conservative and only try once a second
        time.sleep(1)
        
    return s.getvalue()


username = 'squarepegsys'
date = '2015-01-01'
geeklist_id = 183144

post = create_post(username, geeklist_id, date)

# copy the post text to the clipboard, so it's easier to paste it into a BGG post
pyperclip.copy(post)