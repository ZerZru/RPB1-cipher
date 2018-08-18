# RPB1-cipher
Cipher, using Russian in English transliteration, in Japanese characters

pりvえt! や vいzhう, chと vi れshいlい ざいち v えとt れぽじとりい な GitHub. わm いんてれsの, かk らsshいfろわt えとt てkst? mね pりdよtsや ぺれvえsち えご s るssこご な あんglいいsきい, たk chと sみsl shいfら(い えご slおzhのst) もzhえt ぽてrやtsや

Transliteration: Privet! Ya vizhu, chto vi reshili zaiti v etot repozitori na GitHub. Vam interesno, kak rasshifrovat etot tekst? Mne pridyotsya perevesti ego s russkogo na angliiskii, tak chto smisl shifra(i ego slozhnost') mozhet poteryat'sya.

In Russian: Привет! Я вижу, что вы решили зайти в этот репозиторий на GitHub. Вам интересно, как рассшифровать этот текст? Мне придётся его перевести его с русского на английский, так что смысл шифра(и его сложность) может потеряться.

In English: Hello! I see, what you go to this repository on GitHub. You are interesting, how to decrypt this text? I should translate it from Russian into English, but cipher(and him complexity) can lost point.

For using this cipher in English, use the rpb1e() function.

# Importing

If you want to use RPB1, use this:
```python
from RPB1 import rpb1 #if english: rpb1e
```

Else if you want to use RPB2:
```python
from RPB1 import rpb2 #if english: rpb2
```

# About system

The cipher use regular extensions for change literals to japanase symbols. Programm search russian(or english) literals, like "на(na)" and others, and change to "な".

log.TXT - in this file write text(or word) ID, and message. But it look like \xna898. You can check it.

USER_INFO.TXT - if you edit or modificied code and will publish it somewhere, you must to fill info in that file: date of changing, name, changing type(edit, mode or another), and licenses.

# Different between RPB1 and PPB2

RPB1 looks like "るssきい やじk"(русский язык, russian language), RPB2 looks like "ロシア語"(русский язык, russian language).
In RPB2-cipher words with countries and nations translated to japanese words: ROSIA, ROSIAGO, ROSIAJIN and anothers: US, Japan, England and Korea

Sometimes this cipher can translate incorrectly.
