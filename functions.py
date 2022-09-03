import json

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def func_load_json():
    with open("posts2.json", "r", encoding='utf-8') as file:
        json_data = json.load(file)

    return json_data


def func_upload_json(data):
    json_data = func_load_json()
    json_data.append(data)
    with open("posts2.json", "w", encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False)
    return f'Файл загружен'

def extension_check(file_name):
    extension = file_name.split('.')[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

# json_data = func_load_json()
# for item in json_data:
#     print(item["content"].lower())

# data = {}
# data["pic"] = "../uploads/images/" + "cat.jpeg"
# data["content"] = "Какой-то текст"
#
# print(func_upload_json(data))


