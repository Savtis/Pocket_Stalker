def start_player():
    hp = fp = wp = 100 #уровни здоровья, сытости, гидрации
    can = 2 #еда
    fla = med = 1# вода
    pda = dehydro = hungry = brek = False#есть ли метка в пда, обезвоживание, голод, отображение, интерфейса после поиска тайника
    info = position_info = True #отображение интерфейса, отображение текущей локации
    loca = 1 #начальная позиция
    way = bloweff = 0 #прогресс поиска тайника
    return [hp, wp, fp, can, fla, med, pda, dehydro, hungry, brek, info, position_info, loca, way, bloweff]
