from flask import Flask, render_template


app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def base(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    prof2 = prof
    if 'строитель' in prof2:
        prof2 = 'строитель'
    elif 'инженер' in prof2:
        prof2 = 'инженер'
    return render_template('training.html', prof=prof2)


@app.route('/list_prof/<list>')
def list_prof(list):
    user_list = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, \
    климатолог, специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, \
    метеоролог, оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')
    return render_template('list_prof.html', list=list, user_list=user_list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    title = 'Анкета легенды'
    surname = 'Arataki'
    name = 'Itto'
    education = 'высшее'
    profession = 'Дата саентист'
    sex = 'male'
    motivation = 'Хочу анализировать статистические данные о Марсе!'
    ready = 'True'
    d = {'Заголовок': title, 'Фамилия': surname, 'Имя': name, 'Образование': education,
         'Профессия': profession, 'Пол': sex, 'Мотивация': motivation, 'Готовы остаться на Марсе?': ready}
    return render_template('auto_answer.html', d=d)


@app.route('/distribution')
def places():
    passangers = ['Ривер Сонг', 'Амелия Понд', 'Рори Понд', 'Роуз Тайлер', 'Марта Джонс',
                  'Джон Смит', 'Клара Освальд', 'Билл Спот', 'Донна Ноубл']
    return render_template('distribution.html', passangers=passangers)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
