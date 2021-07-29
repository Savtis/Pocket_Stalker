#действие отдых в баре:
def bar_sleep(med, wp, hp, fp, bloweff):
    if med > 0:
        print('я отдохнул в баре за 1 аптечку')
        med -= 1
        fp += 50
        wp += 50
        hp += 90
        bloweff -= 1
    else:
        print('у меня нет лишних аптечек')
    return[med, wp, hp, fp, bloweff]

#действие отдых:
def sleep(hp, fp, wp, hungry, dehydro):
    print('я устроил небольшой привал')
    fp -= 10
    wp -= 5
    if hungry == True or dehydro == True:
        hp += 0
    else:
        hp += 5
    return [hp, fp, wp]
#действие еда:
def eat (can, fp, wp, hp, info):
	if can > 0 and fp < 71:
		print('я съел консерву')
		can -= 1
		fp += 35
		wp -= 6
		hp += 5
	elif can <= 0:
		info = False
		print('у меня нет еды')
	elif fp > 70:
		info = False
		print('я не голоден')
	return [can, fp, wp, hp, info]
	
#действие вода:
def drink (fla, wp, hp, info):
	if fla > 0 and fp < 71:
		print('я выпил бутылку воды')
		fla -= 1
		wp += 50
		hp += 1
	elif fla <= 0:
		info = False
		print('у меня нет воды')
	elif wp > 70:
		info = False
		print('я не хочу пить')
	return [fla, wp, hp, info]
	
#действие аптечка:
def cure(hp, med, info):
	if med > 0 and hp < 71:
		print('я использовал аптечку')
		med -= 1
		hp += 30
	elif med == 0:
		info = False
		print('у меня нет медикаментов')
	elif hp > 70:
		info = False
		print('я хорошо себя чувствую')
	return [hp, med, info]

#выбор похода:
def translate_info(loca, ans, pda):
    print('0 - отмена')
    if loca != 4:
        print('1 - путешествовать по текущей локации')
    if not loca == 1:
        print('2 - перейти на кордон')
    if not loca == 2:
        print('3 - перейти на свалку')
    if not loca == 3:
        print('4 - перейти на болота')
    if loca != 4 and loca == 2:
        print('5 - перейти в бар')
    if pda == True:
        print('6 - искать тайник по метке в КПК')

def act(bloweff, ans, can, fla, med, hp, fp, wp, hungry, dehydro, loca, info, pda):
    if (ans == 2):
        hp, fp, wp = sleep(hp, fp, wp, hungry, dehydro)
    if (ans == 3):
        can, fp, wp, hp, info = eat(can, fp, wp, hp, info)
    if (ans == 4):
        fla, wp, hp, info = drink(fla, wp, hp, info)
    if (ans == 5):
        hp, med, info = cure(hp, med, info)
    if (ans == 1):
        translate_info(loca, ans, pda)
        info = False
    if (ans == 7):
        med, wp, hp, fp, bloweff = bar_sleep(med, wp, hp, fp, bloweff)
    return [bloweff, can, fla, med, hp, fp, wp, loca, info]
