# Модуль для расчета результатов
txt_index = 'Ваш индекс Руфье: '
txt_workheart = 'Работоспособность сердца: '
txt_nodata = '''
    нет данных для такого возраста'''
txt_res = []
txt_res.append('''низкая.
    Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная.
    Обратитесь к врачу!''')
txt_res.append('''средняя
    Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
    выше среднего''')
txt_res.append('''
    высокая''')
# Здесь должен быть твой код

def ruffier_index(p1, p2, p3):
    return (4 * (p1+p2+p3) - 200) / 10

def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age * 1.5
    return result

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4
    if r_index >= level:
        return 1
    level = level - 5
    if r_index >= level:
        return 2
    level = level - 5.5
    if r_index >= level:
        return 3
    return 4


def test(p1, p2, p3, age):
    if age < 7:
        return(txt_index + '0', txt_nodata)
    else:
        r_index = ruffier_index(p1, p2, p3)
        result = txt_res[ruffier_result(r_index, neud_level(age))]
        return (txt_index + str(r_index), txt_workheart + result)