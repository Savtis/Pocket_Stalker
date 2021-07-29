def haversack(med, can, fla, hp, fp, wp, bloweff):
    if bloweff > 0:
        print('после выброса по всей зоне повысился уровень радиации')
        if hp > 30:
            hp -= 7
            if hp < 30:
                hp = 30
    print('моё самочувствие:',hp, '%', end = '')
    if hp < 1:
        print(' я при смерти...')
    else:
        print('')
    print('моя сытость:',fp, '%')
    print('мой водный баланс:', wp, '%')
    if med > 0:
        print('аптечек в рюкзаке:',med)
    else:
        print('аптечек нет')
    if can > 0:
        print('консерв в рюкзаке:',can)
    else:
        print('консерв нет')
    if fla > 0:
        print('бутылок воды в рюкзаке:',fla)
    else:
        print('бутылок с водой нет')
