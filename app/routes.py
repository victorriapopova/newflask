from flask import render_template, flash, redirect, url_for
from app import app, db
from app.models import Headphone
from forms.forms import AddHeadphoneForm  # Поменяйте импорт в соответствии с вашей структурой

from flask import Flask, request

app = Flask(__name__)


@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'POST':
        # Обработка POST-запроса
        return 'POST запрос успешно обработан'
    else:
        # Обработка GET-запроса
        return 'GET запрос успешно обработан'


@app.route('/')
def index():
    headphones = Headphone.query.all()
    return render_template('index.html', title='Интернет-магазин наушников', headphones=headphones)


@app.route('/add', methods=['GET', 'POST'])
def add_headphone():
    form = AddHeadphoneForm()
    if form.validate_on_submit():
        headphone = Headphone(name=form.name.data, description=form.description.data,
                              price=form.price.data, image_url=form.image_url.data)
        db.session.add(headphone)
        db.session.commit()
        flash('Наушники добавлены!')
        return redirect(url_for('index'))
    return render_template('add_headphone.html', title='Добавить наушники', form=form)
