# loader / views.py

# Сначала импортируем класс блюпринта
from flask import Blueprint, render_template, request

# Затем создаем новый блюпринт, выбираем для него имя
from functions import func_upload_json, extension_check

loader_blueprint = Blueprint('loader_blueprint', __name__)

# Создаем вьюшку, используя в декораторе блюпринт вместо app
@loader_blueprint.route('/upload')
def upload_page():
    return render_template('post_form.html')

@loader_blueprint.post('/upload/result')
def result_page():
    file = request.files.get('picture')
    if not file:
        return (f'Файл не найден!')
    else:
        file_name = file.filename
    content = request.form.get('content')
    if not extension_check(file_name):
        return (f'Расширение файла не правильное!')
    else:
        # Загрузка файла в папку /static/img/
        file.save(f'./static/img/{file_name}')

    # Загрузка нового постав в файл JSON
    json_data = {}
    json_data['pic'] = "../static/img/" + file_name
    json_data['content'] = content
    func_upload_json(json_data)
    return render_template('post_uploaded.html', content=content, pic=json_data['pic'])
