with open ('poblado/values/valoresTienda.txt', 'a', encoding='utf8') as txtTienda:
    id = 0
    with open('poblado/data/calles.txt', 'r', encoding='utf8') as txtCalles:
        for line in txtCalles:
            id += 1
            line = line.strip()
            txtTienda.write(str(id))
            txtTienda.write(',')
            txtTienda.write(f"'{line}'")
            txtTienda.write('\n')