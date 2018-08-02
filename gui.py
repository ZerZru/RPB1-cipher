import re
from tkinter import *
from __init__ import rpb1
root = Tk()
root.title('RPB1 Cryptor')
root.geometry('300x400')
text_label = Label(root, text='Ваш текст для шифрования: ')
text_entry = Entry(root)
text_button = Button(root, text='Зашифровать')
def crypt(word_or_sentence):
    letter_z = 'z'
    letter_s = 's'
    letter_r = 'r'
    letter_v = 'v'
    letter_l = 'l'
    letter_k = 'k'
    letter_p = 'p'
    letter_e = 'e'
    letter_b = 'b'
    letter_f = 'f'
    letter_h = 'h'
    letter_g = 'g'
    letter_t = 't'
    letter_d = 'd'
    letter_m = 'm'
    letter_ts = 'ts'
    letter_ch = 'ch'
    letter_zh = 'zh'
    letter_sh = 'sh'
    letter_sch = 'sch'
    soft_letter = ''
    strong_letter = ''
    #vowels
    hiragana_letter_a = 'あ'
    hiragana_letter_i = 'い'
    hiragana_letter_u = 'う'
    hiragana_letter_e = 'え'
    hiragana_letter_o = 'お'
    #standart consonants
    hiragana_letter_ka = 'か'
    hiragana_letter_ki = 'き'
    hiragana_letter_ku = 'く'
    hiragana_letter_ke = 'け'
    hiragana_letter_ko = 'こ'
    hiragana_letter_sa = 'さ'
    hiragana_letter_si = 'し'
    hiragana_letter_su = 'す'
    hiragana_letter_se = 'せ'
    hiragana_letter_so = 'そ'
    hiragana_letter_ta = 'た'
    hiragana_letter_ti = 'ち'
    hiragana_letter_tu = 'つ'
    hiragana_letter_te = 'て'
    hiragana_letter_to = 'と'
    hiragana_letter_na = 'な'
    hiragana_letter_ni = 'に'
    hiragana_letter_nu = 'ぬ'
    hiragana_letter_ne = 'ね'
    hiragana_letter_no = 'の'
    hiragana_letter_ha = 'は'
    hiragana_letter_hi = 'ひ'
    hiragana_letter_hu = 'ふ'
    hiragana_letter_he = 'へ'
    hiragana_letter_ho = 'ほ'
    hiragana_letter_ma = 'ま'
    hiragana_letter_mi = 'み'
    hiragana_letter_mu = 'む'
    hiragana_letter_me = 'め'
    hiragana_letter_mo = 'も'
    hiragana_letter_ya = 'や'
    hiragana_letter_yu = 'ゆ'
    hiragana_letter_yo = 'よ'
    hiragana_letter_ra = 'ら'
    hiragana_letter_ri = 'り'
    hiragana_letter_ru = 'る'
    hiragana_letter_re = 'れ'
    hiragana_letter_ro = 'ろ'
    hiragana_letter_wa = 'わ'
    hiragana_letter_wo = 'を'
    hiragana_letter_n = 'ん'
    #voiced consonants
    hiragana_letter_ga = 'が'
    hiragana_letter_gi = 'ぎ'
    hiragana_letter_gu = 'ぐ'
    hiragana_letter_ge = 'げ'
    hiragana_letter_go = 'ご'
    hiragana_letter_za = 'ざ'
    hiragana_letter_zi = 'じ'
    hiragana_letter_zu = 'ず'
    hiragana_letter_ze = 'ぜ'
    hiragana_letter_zo = 'ぞ'
    hiragana_letter_da = 'だ'
    hiragana_letter_di = 'ぢ'
    hiragana_letter_du = 'づ'
    hiragana_letter_de = 'で'
    hiragana_letter_do = 'ど'
    hiragana_letter_ba = 'ば'
    hiragana_letter_bi = 'び'
    hiragana_letter_bu = 'ぶ'
    hiragana_letter_be = 'べ'
    hiragana_letter_bo = 'ぼ'
    #deaf consonants
    hiragana_letter_pa = 'ぱ'
    hiragana_letter_pi = 'ぴ'
    hiragana_letter_pu = 'ぷ'
    hiragana_letter_pe = 'ぺ'
    hiragana_letter_po = 'ぽ'
    if None:
        print('Совпадений не найдено')
    else:
        word_or_sentence.lower()
        word_or_sentence = re.sub('ка', hiragana_letter_ka, word_or_sentence)
        word_or_sentence = re.sub('ки', hiragana_letter_ki, word_or_sentence)
        word_or_sentence = re.sub('кы', hiragana_letter_ki, word_or_sentence)
        word_or_sentence = re.sub('ку', hiragana_letter_ku, word_or_sentence)
        word_or_sentence = re.sub('кю', hiragana_letter_ku, word_or_sentence)
        word_or_sentence = re.sub('ке', hiragana_letter_ke, word_or_sentence)
        word_or_sentence = re.sub('кэ', hiragana_letter_ke, word_or_sentence)
        word_or_sentence = re.sub('ко', hiragana_letter_ko, word_or_sentence)
        word_or_sentence = re.sub('са', hiragana_letter_sa, word_or_sentence)
        word_or_sentence = re.sub('си', hiragana_letter_si, word_or_sentence)
        word_or_sentence = re.sub('сы', hiragana_letter_si, word_or_sentence)
        word_or_sentence = re.sub('су', hiragana_letter_su, word_or_sentence)
        word_or_sentence = re.sub('сю', hiragana_letter_su, word_or_sentence)
        word_or_sentence = re.sub('се', hiragana_letter_se, word_or_sentence)
        word_or_sentence = re.sub('сэ', hiragana_letter_se, word_or_sentence)
        word_or_sentence = re.sub('со', hiragana_letter_so, word_or_sentence)
        word_or_sentence = re.sub('на', hiragana_letter_na, word_or_sentence)
        word_or_sentence = re.sub('ни', hiragana_letter_ni, word_or_sentence)
        word_or_sentence = re.sub('ны', hiragana_letter_ni, word_or_sentence)
        word_or_sentence = re.sub('ну', hiragana_letter_nu, word_or_sentence)
        word_or_sentence = re.sub('ню', hiragana_letter_nu, word_or_sentence)
        word_or_sentence = re.sub('не', hiragana_letter_ne, word_or_sentence)
        word_or_sentence = re.sub('нэ', hiragana_letter_ne, word_or_sentence)
        word_or_sentence = re.sub('но', hiragana_letter_no, word_or_sentence)
        word_or_sentence = re.sub('та', hiragana_letter_ta, word_or_sentence)
        word_or_sentence = re.sub('ти', hiragana_letter_ti, word_or_sentence)
        word_or_sentence = re.sub('ты', hiragana_letter_ti, word_or_sentence)
        word_or_sentence = re.sub('ту', hiragana_letter_tu, word_or_sentence)
        word_or_sentence = re.sub('тю', hiragana_letter_tu, word_or_sentence)
        word_or_sentence = re.sub('те', hiragana_letter_te, word_or_sentence)
        word_or_sentence = re.sub('тэ', hiragana_letter_te, word_or_sentence)
        word_or_sentence = re.sub('то', hiragana_letter_to, word_or_sentence)
        word_or_sentence = re.sub('ха', hiragana_letter_ha, word_or_sentence)
        word_or_sentence = re.sub('хи', hiragana_letter_hi, word_or_sentence)
        word_or_sentence = re.sub('хы', hiragana_letter_hi, word_or_sentence)
        word_or_sentence = re.sub('ху', hiragana_letter_hu, word_or_sentence)
        word_or_sentence = re.sub('хю', hiragana_letter_hu, word_or_sentence)
        word_or_sentence = re.sub('хе', hiragana_letter_he, word_or_sentence)
        word_or_sentence = re.sub('хэ', hiragana_letter_he, word_or_sentence)
        word_or_sentence = re.sub('хо', hiragana_letter_ho, word_or_sentence)
        word_or_sentence = re.sub('ма', hiragana_letter_ma, word_or_sentence)
        word_or_sentence = re.sub('ми', hiragana_letter_mi, word_or_sentence)
        word_or_sentence = re.sub('мы', hiragana_letter_mi, word_or_sentence)
        word_or_sentence = re.sub('му', hiragana_letter_mu, word_or_sentence)
        word_or_sentence = re.sub('мю', hiragana_letter_mu, word_or_sentence)
        word_or_sentence = re.sub('ме', hiragana_letter_me, word_or_sentence)
        word_or_sentence = re.sub('мэ', hiragana_letter_me, word_or_sentence)
        word_or_sentence = re.sub('мо', hiragana_letter_mo, word_or_sentence)
        word_or_sentence = re.sub('я', hiragana_letter_ya, word_or_sentence)
        word_or_sentence = re.sub('ё', hiragana_letter_yo, word_or_sentence)
        word_or_sentence = re.sub('ю', hiragana_letter_yu, word_or_sentence)
        word_or_sentence = re.sub('ра', hiragana_letter_ra, word_or_sentence)
        word_or_sentence = re.sub('ри', hiragana_letter_ri, word_or_sentence)
        word_or_sentence = re.sub('ры', hiragana_letter_ri, word_or_sentence)
        word_or_sentence = re.sub('ру', hiragana_letter_ru, word_or_sentence)
        word_or_sentence = re.sub('рю', hiragana_letter_ru, word_or_sentence)
        word_or_sentence = re.sub('ре', hiragana_letter_re, word_or_sentence)
        word_or_sentence = re.sub('рэ', hiragana_letter_re, word_or_sentence)
        word_or_sentence = re.sub('ро', hiragana_letter_ro, word_or_sentence)
        word_or_sentence = re.sub('ва', hiragana_letter_wa, word_or_sentence)
        word_or_sentence = re.sub('во', hiragana_letter_wo, word_or_sentence)
        word_or_sentence = re.sub('н', hiragana_letter_n, word_or_sentence)
        word_or_sentence = re.sub('га', hiragana_letter_ga, word_or_sentence)
        word_or_sentence = re.sub('ги', hiragana_letter_gi, word_or_sentence)
        word_or_sentence = re.sub('гы', hiragana_letter_gi, word_or_sentence)
        word_or_sentence = re.sub('гу', hiragana_letter_gu, word_or_sentence)
        word_or_sentence = re.sub('гю', hiragana_letter_gu, word_or_sentence)
        word_or_sentence = re.sub('ге', hiragana_letter_ge, word_or_sentence)
        word_or_sentence = re.sub('гэ', hiragana_letter_ge, word_or_sentence)
        word_or_sentence = re.sub('го', hiragana_letter_go, word_or_sentence)
        word_or_sentence = re.sub('за', hiragana_letter_za, word_or_sentence)
        word_or_sentence = re.sub('зи', hiragana_letter_zi, word_or_sentence)
        word_or_sentence = re.sub('зы', hiragana_letter_zi, word_or_sentence)
        word_or_sentence = re.sub('зу', hiragana_letter_zu, word_or_sentence)
        word_or_sentence = re.sub('зю', hiragana_letter_zu, word_or_sentence)
        word_or_sentence = re.sub('зе', hiragana_letter_ze, word_or_sentence)
        word_or_sentence = re.sub('зэ', hiragana_letter_ze, word_or_sentence)
        word_or_sentence = re.sub('зо', hiragana_letter_zo, word_or_sentence)
        word_or_sentence = re.sub('да', hiragana_letter_da, word_or_sentence)
        word_or_sentence = re.sub('ди', hiragana_letter_di, word_or_sentence)
        word_or_sentence = re.sub('ды', hiragana_letter_di, word_or_sentence)
        word_or_sentence = re.sub('ду', hiragana_letter_du, word_or_sentence)
        word_or_sentence = re.sub('дю', hiragana_letter_du, word_or_sentence)
        word_or_sentence = re.sub('де', hiragana_letter_de, word_or_sentence)
        word_or_sentence = re.sub('дэ', hiragana_letter_de, word_or_sentence)
        word_or_sentence = re.sub('до', hiragana_letter_do, word_or_sentence)
        word_or_sentence = re.sub('па', hiragana_letter_pa, word_or_sentence)
        word_or_sentence = re.sub('пи', hiragana_letter_pi, word_or_sentence)
        word_or_sentence = re.sub('пы', hiragana_letter_pi, word_or_sentence)
        word_or_sentence = re.sub('пу', hiragana_letter_pu, word_or_sentence)
        word_or_sentence = re.sub('пю', hiragana_letter_pu, word_or_sentence)
        word_or_sentence = re.sub('пе', hiragana_letter_pe, word_or_sentence)
        word_or_sentence = re.sub('пэ', hiragana_letter_pe, word_or_sentence)
        word_or_sentence = re.sub('по', hiragana_letter_po, word_or_sentence)
        word_or_sentence = re.sub('а', hiragana_letter_a, word_or_sentence)
        word_or_sentence = re.sub('и', hiragana_letter_i, word_or_sentence)
        word_or_sentence = re.sub('й', hiragana_letter_i, word_or_sentence)
        word_or_sentence = re.sub('у', hiragana_letter_u, word_or_sentence)
        word_or_sentence = re.sub('е', hiragana_letter_e, word_or_sentence)
        word_or_sentence = re.sub('э', hiragana_letter_e, word_or_sentence)
        word_or_sentence = re.sub('о', hiragana_letter_o, word_or_sentence)
        word_or_sentence = re.sub('з', letter_z, word_or_sentence)
        word_or_sentence = re.sub('с', letter_s, word_or_sentence)
        word_or_sentence = re.sub('р', letter_r, word_or_sentence)
        word_or_sentence = re.sub('в', letter_v, word_or_sentence)
        word_or_sentence = re.sub('л', letter_l, word_or_sentence)
        word_or_sentence = re.sub('к', letter_k, word_or_sentence)
        word_or_sentence = re.sub('п', letter_p, word_or_sentence)
        word_or_sentence = re.sub('б', letter_b, word_or_sentence)
        word_or_sentence = re.sub('ф', letter_f, word_or_sentence)
        word_or_sentence = re.sub('х', letter_h, word_or_sentence)
        word_or_sentence = re.sub('г', letter_g, word_or_sentence)
        word_or_sentence = re.sub('т', letter_t, word_or_sentence)
        word_or_sentence = re.sub('д', letter_d, word_or_sentence)
        word_or_sentence = re.sub('м', letter_m, word_or_sentence)
        word_or_sentence = re.sub('ц', letter_ts, word_or_sentence)
        word_or_sentence = re.sub('ч', letter_ch, word_or_sentence)
        word_or_sentence = re.sub('ж', letter_zh, word_or_sentence)
        word_or_sentence = re.sub('ш', letter_sh, word_or_sentence)
        word_or_sentence = re.sub('щ', letter_sch, word_or_sentence)
        word_or_sentence = re.sub('ь', soft_letter, word_or_sentence)
        word_or_sentence = re.sub('ъ', strong_letter, word_or_sentence)
    window = Toplevel()
    window.title('RPB1: {}'.format(word_or_sentence))
    window.geometry('1000x500')
    text = Text(window, width=1000, height=500)
    text.insert(1.0, '{}\n\n\nТекст скопирован в буфер обмена'.format(word_or_sentence))
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(word_or_sentence)
    root.update()
    text.place(x=0, y=0)
    scroll = Scrollbar(window, orient=HORIZONTAL)
    scroll.pack(side=BOTTOM, fill=X)
def info():
    window = Toplevel()
    window.title('RPB1: Information')
    window.geometry('400x400')
    text_label_l = Label(window, text='Не рекомендуется писать слишком длинные\nстроки, иначе вы не увидите весь текст')
    text_label_l.pack()
info_button = Button(text='Рекомендации к работе',  command=info)
text_button.bind('<Button-1>', lambda event: crypt(text_entry.get()))
text_button.place(x=0, y=30)
text_label.place(x=0, y=0)
text_entry.place(x=170, y=0)
info_button.place(x=0, y=60)
root.mainloop()