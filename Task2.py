a = {
    'Ad: ': "Amil",
    'Soyad: ': 'Xidirov',
    'Seher: ': 'Sumqayit',
}

b = input('Daxil edin (1), (2): ')


if b == str('1'):
    print(a.keys())

elif b == str('2'):
    print(a.values())

elif b == str(''):
    print('Melumat daxil etmediniz..')