## BGG 10x10 Forum post generator

This is based on work by eviljelloman from:
http://nbviewer.ipython.org/gist/anonymous/861acb2a52fa6d1ad2e4

His description sums it up better than me:

> The following code snippits take, as inputs:
>
> * a BoardGameGeek geeklist containing a set of games
> * a username
> * a minimum date
>
> and generates the text for a nicely formatted BoardGameGeek post describing the number of times the user has played the games on that list since the minimum date. This is intended primarily to make it easier to update posts for the BGG 10x10 challenge, where players commit to playing a list of ten games at least ten times each.

> This code should work correctly on both Python 2 and 3, with no modifications. In order to use all functionality, you will need to ensure that you have installed the following libraries:

> * lxml
> * BeautifulSoup4
> * pyperclip

My usage is simple:

* put in your username, date to start counting your plays, and the Geeklist of your games in your 10x10
* Then, every so often run 

       ./bgg_counter.py

Then paste into your 10x10 comment.

### Changes

This is pretty much the original. I put the original notebook snippets into one script and made a fix so it accepts game plays without a comment

