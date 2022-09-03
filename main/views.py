# main / views.py

# Сначала импортируем класс блюпринта
from flask import Blueprint, render_template, request

# Затем создаем новый блюпринт, выбираем для него имя
from functions import func_load_json

main_blueprint = Blueprint('main_blueprint', __name__)


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route('/search')
def search_page():
    s = request.args.get('s')
    json_data = func_load_json()
    items = []
    item_content = False
    for item in json_data:
        if s.lower() in item["content"].lower():
            items.append(item)
            item_content = True
    if not item_content:
        return (render_template('post_item_None.html', request=s))
    else:
        return render_template('post_item.html', request=s, items=items)
