# Sci-fi story generator by Stanislaw Lem, 1973(c)

from random import randrange
import random

list0 = ['scientists ', 'is invaded by ', 'turns into a frozen desert', 'turns into a scorched desert', 'is collide with a giant comet ']
list1 = ['are create ', 'are discover ']
list2 = ['and collapses. The end.', 'and remains unscratched. The end', 'and do not collapses, but ']
list3 = ['all are dying. The end.', 'almost all are dying. The end.']
list4 = ['and all are dying. The end.', 'and almost all are dying. The end.']
list5 = ['tiny ', 'big ']
list6 = ['Martians ', 'Tentacles ', 'Star Swarm ']
list7 = ['insects ', 'snakes ', 'robots ', 'dinosaurs ', 'spiders ', 'various weird things ']
list8 = ['who desire our women, steal them and disappear. The end.', 'who behave in a friendly manner. The end.',
         'who behave in a friendly manner, but no one can understand them ', 'who do not understand us ', 'who surprisingly well understand us ',
         'who percieve us only as a food ']
list9 = ['also they are radioactive ', 'also they are not radioactive ']
list10 = ['and can be destroyed ', 'and can not be destroyed ']
list11 = ['by crowd of people with hayforks and torches ', 'by army, navy, aviation and/or marines ',
         'by nuclear bomb ']
list12 = ['that does not work ', 'that kill them all. The end.', 'that turns them into weird rocks. The end.']
list13 = ['but they are dying due to black desease. The end.', 'and so they are kill us all. The end.', 'so they are establish the dictatorship. The end.',
          'so they are eat us all. The end.']
list14 = ['but one cunning guy convinces them, that people are "OK" ', 'but priest tell them about the God ', 'but they are falling in love with a young girl ']
list15 = ['and so they are dying. The end.', 'and so they are flying away. The end', 'and they are turns into weird rocks. The end.']


def fate():
    rand = random.random()
    if rand > 0.5:
        return True
    return False


def rand(length):
    return randrange(0, length)


def add_text(txt):
    txt += random.choice(list0)
    if 'turns' in txt:
        txt += random.choice(list4)
        return txt
    if 'comet' in txt:
        txt += random.choice(list2)
        if 'but' in txt:
            txt += random.choice(list3)
        return txt
    if 'scientists' in txt:
        txt += random.choice(list1)
        txt += random.choice(list5)
        txt += random.choice(list7)
    if 'invaded' in txt:
        txt += random.choice(list5)
        txt += random.choice(list6)
        txt += random.choice(list7)
    txt += random.choice(list8)
    if 'women' in txt:
        return txt
    if 'manner.' in txt:
        return txt
    if 'food' in txt:
        if fate():
            return txt + ' and eat us all. The end.'
    txt += random.choice(list9)
    txt += random.choice(list10)
    txt += random.choice(list11)
    if 'can be' in txt:
        return txt[:-1] + '. The end.'
    if fate():
        if fate():
            txt = txt[:-1] + ', but scientists create a new weapon '
            txt += random.choice(list12)
            if 'not work' in txt:
                txt += random.choice(list13)
                return txt
        else:
            txt += random.choice(list13)
            return txt
    else:
        txt += random.choice(list14)
        if 'girl' in text:
            if fate():
                txt = txt[:-1] + ', they are marrying and live long and prosper. The end'
                return txt
        txt += random.choice(list15)
    return txt


text = 'The Earth '
text = add_text(text)


print(text)
