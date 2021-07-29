import time #время
import player_default #данные об игроке
import acts #действия игрока
import start_menu #начальная заставка
import haverask #данные о инвентаре и параметрах
import random #рандомные числа
#импорт↑
start_menu.start(170)
#
def panel(loca):
    print('что делать дальше?\n1 - продолжить путь\n2 - отдохнуть\n3 - съесть консерву\n4 - выпить бутылку воды\n5 - применить аптечку\n6 - просмотр достижений')
    if loca == 4:
        print('7 - отдохнуть в баре за 1 аптечку')
# некоторые функции ↓
def translate(hp, wp, fp, ans, loca):
    if ans == 2:
        loca = 1
        print('я ушёл на кордон')
    if ans == 3:
        loca = 2
        print('я ушёл на свалку')
    if ans == 4:
        loca = 3
        print('я ушёл на болота')
    if ans == 5:
        loca = 4
        print('я ушёл в бар')
    hp += 1
    wp -= 30
    fp -= 35
    position_info = False
    return [hp, wp, fp, loca, position_info]
def position(loca):
    if loca == 1:
        print('я на кардоне')
    if loca == 2:
        print('я на свалке')
    if loca == 3:
        print('я на болотах')
    if loca == 4:
        print('я в баре')
# на кордоне меньше опасности и меньше ресурсов
# на свалке больше опасности и больше ресурсов
# на болотах средняя опасность и гнетущая обстановка(возможен сюжет)

# варианты ответов
def ans_2():
	ans = -999
	while ans != 1 and ans != 2:
		ans = int(input('выбор: '))
		if ans == 1 or ans == 2:
			break
		else:
			print('чта?')
	return [ans]
def ans_3():
	ans = -999
	while ans < 1 or ans > 3:
		ans = int(input('выбор: '))
		if ans < 1 or ans > 3:
			break
		else:
			print('чта?')
	return [ans]
def control_parametrs(hp, fp, wp):
#верхняя граница
	if hp > 100:
		hp = 100
	if fp > 100:
		fp = 100
	if wp > 100:
		wp = 100
	#нижняя граница
	if hp < 0:
		hp = 0
	if fp < 0:
		fp = 0
	if wp < 0:
		wp = 0
	#голод и обезвоживание и последствия
	dehydro = False
	hungry = False
	if fp == 0:
		hungry = True
		hp -= 5
	if wp == 0:
		dehydro = True
		hp -= 6

	return [hp, fp, wp, dehydro, hungry]
	
#СОБЫТИЯ, ОЧЕНЬ МНОГО ФУНКЦИЙ!
#НАЧАЛО:
def ivent_default():
	print('[за день ничего не произошло]')
def ivent_rain(fla, fp, hp):
	print('сгустились тучи и в далеке загремел гром\n1 - спрятатся в ближайшем здании\n2 - продолжить идти')
	ans = ans_2()
	if ans == 1:
		fp -= 2
		wp -= 1
		print('я переждал ливень в заброшке')
	if ans == 2:
		fla += 1
		hp -= 1
		fp -= 5
		print('я попал под дождь и сильно промок, зато сумел набрать бутылку воды')
	return [fla, fp, hp]
def ivent_deadbody_r(can, med, fla):
    d = random.random()*10
    if d >= 0 and d < 5:
	    bn = 'одиночки'
    if d > 4 and d < 8:
	    bn = 'свободовца'
    if d > 7 and d < 11:
	    bn = 'бандита'
    i = random.random()*4
    if i == 1 or i == 2:
	    h = 'пару консерв'
	    can += 2
    print('идя по заброшенному хутору я увидел труп '+bn+', обыскав его, я нашёл '+h+' и пошёл дальше')
    return [can, med, fla]
def ivent_sun(wp):
        wp -= 10
        print('сегодня солнце крайне сильно припекло, жарковато...')
        return [wp]
def ivent_blowout(can, fla, med, hp, wp, fp):
        print('дерьмо! земля встряхнулась, небо стало приобретать алый оттенок. это выброс! надо прятатся!\n1 - спрятатся в гараже\n3 - спрятатся в неопознанный бетонный до\n3 - спрятатся в заброшенной избушке')
        ans = ans_3()
        if ans == 3:
            fp -= 3
            wp -= 2
            can += 1
            fla += 1
            print('я быстро забежал в ветхий домик из брёвен и закрыл дверь. за окном без стёкол, прогремел гром и земля переодически тряслась. обыскав всё это небольшое помещение, я нашёл банку тушёнки и бутылку воды, которую оставили хозяева')
        if ans == 1:
            fp -= 2
            wp -= 1
            print('я побежал к металлическому гаражу, зайдя в него я увидел спящего кровососа\n1 - убить его огнестрельным оружием\n2 - попытаться его зарезать\n3 - кинуть в него что-нибудь')
            ans = ans_3
            if ans == 1:
                print('я взял свой ПМ и нацелился ему в голову, но как только я собрался выстрелить землю снова встряхнуло, я выстрелил, но, к сожалению, в стену, выше головы монстра. тот проснулся и тут же кинулся на меня\n1 - бить ножом\n2 - стрелять дальше из пистолета')
                ans = ans_2
                if ans == 1:
                    hp -= 10
                    fp -= 9
                    wp -= 17
                    print('я начал стрелять, но, учитывая мою меткость, из 10 выстрелов попало только 4, но в конце концов тот упал в крови')
                if ans == 2:
                    print('я схватил кусок трубы рядом с собой и со всей силы ударил монстра, я попал ему в висок и тот упал замертво')
                    hp -= 1
            if ans == 3:
                print('я тихо взял кусок трубы рядом с собой и со всей силы швырнул в монстра, в этоге я попал ему в висок и тот упал замертво')
            if ans == 3:
                print('я тихо подкрался к мутанту и набросился на него, начав бить его ножом в туловище и шею, тот успел нанести мне пару ударов, но он быстро успокоился')
                hp -= 2
                fp -= 1
            print('что мне теперь делать с этой тушей?\n1 - оставить как есть\n2 - разделать на мясо')
            ans = ans_2()
            if ans == 1:
                print('я оставил мёртвого мутанта лежать на полу и, когда выброс кончился, я ушёл из этого гаража')
            if ans == 2:
                print('я, при помощи своего ножа, разделал его и срезал мясо, оно было прожилистое. когда выброс кончился, я вышел на улицу и пожарил это мясо на костре и поел. на вкус так себе, но есть можно.\nчасть мяса я не смог съесть и поэтому распихал по пустым консервным банкам')
                can += 3
                fp += 100
                wp -= 30
        bloweff = 3
        return [can, fla, med, hp, wp, fp, bloweff]
def ivent_toxic_rain(hp, fp, wp):
    print('сгустились зелёного цвета тучи и в далеке загремел гром\n1 - спрятатся в ближайшем здании\n2 - продолжить идти')
    ans = ans_2()
    if ans == 1:
        fp -= 2
        wp -= 1
        print('я переждал токсичный ливень в заброшке')
    if ans == 2:
        hp -= 10
        fp -= 7
        print('я попал под кислотный дождь и сильно промок, это очень неприятно')
    return [fla, fp, hp]
def ivent_stash_r(can, fla, med):
    ans = - 1
    code = random.random() * 3
    un = False
    print('я был в кустах и нашёл там странный ящик с кодовым замком, к ящику был приклеен листок, на котором было написано: ')
    if code == 1:
        title = 'чЕслО Пи бЭз 3апетОй'
        while ans != 314:
            ans == int(input('0 - чтобы бросить подбор пароля\nпопробовать код: '))
            if ans != 314:
                print('код подобран неверно, замок не поддаётся')
            elif ans == 0:
                break
            else:
                un = True
                break
    if code == 2:
        num = 10 + random.random() * 3
        title = 'чиСло {0} в 2 Степени'.format(num)
        while ans != num*num:
            ans = int(input('0 - чтобы бросить подбор пароля\nпопробовать код: '))
            if ans != num*num:
               print('код подобран неверно, замок не поддаётся')
            elif ans == 0:
                break
            else:
                un = True
                break
    if code == 3:
        ad0 = 2 + random.random() * 7
        ad1 = 11 + random.random() * 9
        ad2 = 10 + random.random() * 6
        title = '8×{0}+({1}-{2})'.format(ad0, ad1, ad2)
        while ans != 8*ad0+(ad1-ad2):
            ans = int(input('0 - чтобы бросить подбор пароля\nпопробовать код: '))
            if ans != 8*ad0+(ad1-ad2):
                print('код подобран неверно, замок не поддаётся')
            elif ans == 0:
                break
            else:
                un = True
                break
    if un == False:
        print('я не стал подбирать пароль и ушёл оттуда')
    else:
        t = random.random()*4
        if t == 1:
            hab = 'банку тушёнки'
            can += 1
        if t == 2:
            hab = 'пару бутылок воды'
            fla += 2
        if t == 3:
            hab = 'аптечку'
            med += 1
        if t == 4:
            hab = 'банку тушёнки и бутылочку воды'
            can += 1
            fla += 1
        print('есть! замок поддался и я нашёл {0}!'.format(hab))
    return [can, fla, med]
def ivent_dog(can, fp, hp, wp):
    print('я услышал гавканье собак, а затем увидел как на меня бежит стая слепых псов\n1 - атаковать\n2 - убегать')
    ans = ans_2()
    if ans == 1:
        hp -= 9
        fp -= 3
        wp -= 2
        can += 1
        print('я перебил всю стаю и получил с них мясо')
    if ans == 2:
        print('я унёс ноги от этих псов и пошёл дальше')
        fp -= 6
        wp -= 3
    return [wp, fp, can, hp]
def ivent_group_fight(hp, wp, fp):
    print('я случайно попал под пули во время битвы между долгом и свободой. ', end = '', flush = True)
    d = random.random()*20
    fp -= 5
    wp -= 4
    if d > 0:
        print('я попытался как можно быстрее покинуть место битвы, но меня всё равно задело')
        hp -= d
        if hp < 1:
            print('чуть не умер...')
            hp = 1
    else:
        print('я бежал как можно быстрее и, к счастью, меня не задело')
    return [hp, wp, fp]
def ivent_river(wp, fla):
    print('я шёл по редкому лесу и вдруг набрёл на ручёй. дозиметр не показал признаков заражения воды радиацией и поэтому я попил из него и набрал бутылку воды')
    wp += 70
    fla += 1
    return [wp, fla]
def ivent_stash_bomb_dump(hp, can):
    p = 1 + random.random()
    print('идя около мусорных куч, я услышал странный звук, похожий на тиканье\n1 - подойти к источнику звука\n2 - идти дальше')
    ans = ans_2()
    col = ''
    if ans == 2:
        print('зачем испытывать судьбу? идём отсюда')
    if ans == 1:
        print('подойдя к ближе, я увидел ящик, к которому прикреплён динамит и механизм, который подорвёт ящик, если его попробуют открыть. можно попробовать обрезать один из проводов\n1 - резать красный!\n2 - резать синий!\n3 - ничего не резать и убежать оттуда!')
        ans = ans_3()
        if ans == 1:
            col = 'красный'
        if ans == 2:
            col = 'синий'
        if ans == 0:
            print('я удрал оттуда, мало ли, когда эта штука взорвётся')
        if ans == p and ans != 0:
            print('ура! обрезав {0} провод, я отключил тиканье и, открыв ящик, я достал... одну банку тушёнки...'.format(col))
            can += 1
        if ans != p and ans != 0:
            print('обрезав {0} провод, бомба, привязанная к ящику как рванула, что я аж отлетел оттуда на 5 метров. ай...')
            hp -= 50
    return [hp, can]
def ivent_malina(fp, wp, hp):
    b = random.random() * 9
    if b == 0:
        berry = 'малины'
        yum = 5 + random.random()*9
        fp += yum
        yum1 = int(yum/2)
        wp += yum1
        yum2 -= yum - 1
        yum2 = int(yum/3)
        hp += yum2
    if b > 0 and b < 10:
        berry = 'мутировавшей земляники'
        yum = 5 + random.random()*19
        fp += yum
        yum1 = int(yum/2.5)
        wp += yum1
    return[fp, wp, hp]

    print('в лесу оказался куст '+berry+' поэтому я поел и побрёл дальше')
	#КОНЕЦ ВСЕХ СОБЫТИЙ!

#поход
#лока на 1 больше, чем ответ
def pda0(pda, loca, way, med, can, fla, fp, wp):
    fp -= 15
    wp -= 8
    way += 1
    brek = False
    print('я пошёл к указанному месту\nпрогресс:')
    if way == 1:
        print('○▲――――■')
    if way == 2:
        print('○―▲―――■')
    if way == 3:
        print('○――▲――■')
    if way == 4:
        print('○―――▲―■')
    if way == 5:
        print('○――――▲■')
        print('я добрался  до тайника, благодаря метке в найденом КПК. в тайнике оказался запас провизии и медикаментов')
        can += 3
        fla += 2
        med += 2
        pda = False
        brek = True
    return [brek, loca, way, pda, loca, med, can, fla, fp, wp]
def walk (loca, can, med, fla, ans, hp, wp, fp, pda, way, position_info):
    brek = False
    ans = -1
    a = 1
    while a == 1:
        ans = int(input('идти: '))
        if ans == loca + 1:
            print('я уже тут')
        if ans == 0:
            break
        if ans == 1 and loca != 5:
            print('функция недоступна, следуйте за мной в ГИТХАБе')
            info = False
            break
        elif loca == 5:
            print('тут нечего искать')
            info = False
            break
        if ans == 2 and ans != loca + 1:
            hp, wp, fp, loca, position_info = translate(hp, wp, fp, ans, loca)
            break
        if ans == 3 and ans != loca + 1:
            hp, wp, fp, loca, position_info = translate(hp, wp, fp, ans, loca)
            break
        if ans == 4 and ans != loca + 1:
            hp, wp, fp, loca, position_info = translate(hp, wp, fp, ans, loca)
            break
        if ans == 5 and ans != loca + 1 and loca == 2:
            hp, wp, fp, loca, position_info = translate(hp, wp, fp, ans, loca)
            break
        elif loca != 2 and ans == 5:
            print('это куда?')
        hp += 1
        wp -= 30
        fp -= 35
        position_info = False
        if ans == 6 and loca != 4 and pda == True:
            brek, loca, way, pda, loca, med, can, fla, fp, wp =  pda0(pda, loca, way, med, can, fla, fp, wp)
            fp -= 10
            wp -= 6
        elif loca == 4:
            print('я тут этого не найду')
        elif pda == False:
            print('это куда?')
        if ans < 0 or ans > 6:
            print('это куда?')
        if brek == True:
            break
	#рандом
	#дальше идут события
    return [pda, hp, wp, fp, loca, position_info]

hp, wp, fp, can, fla, med, pda, dehydro, hungry, brek, info, position_info, loca, way, bloweff = player_default.start_player()

 #ИГРОВОЙ ЦИКЛ ↓
while hp > 0:
    ans = -1
    hp, fp, wp, dehydro, hungry = control_parametrs(hp, fp, wp)
    if info == True:
        if position_info == True:
            position(loca)
    haverask.haversack(med, can, fla, hp, fp, wp, bloweff)
    panel(loca)
    info = True
    position_info = True
    if loca == 4:
        m = 7
    else:
         m = 6
    while ans > m or ans < 1:
        ans = int(input('выбор: '))
        if ans > m or ans < 1:
            print('не понял')
        else:
            break
    bloweff, can, fla, med, hp, fp, wp, loca, info = acts.act(bloweff, ans, can, fla, med, hp, fp, wp, hungry, dehydro, loca, info, pda)
    if ans == 1:
        info == True
        pda, hp, wp, fp, loca, position_info = walk(loca, can, med, fla, ans, hp, wp, fp, pda, way, position_info)
    info = True
print('ЕЩЁ ОДИН ПРОПАВШИЙ В ЗОНЕ. . .'.center(consolSize+4))
print('введите что-нибудь'.center(consolSize, '░'))
input()
