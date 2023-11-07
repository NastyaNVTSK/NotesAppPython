import json
from datetime import datetime

def add_note():
    note_id = len(notes) + 1
    
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "created_at": created_at,
        "updated_at": created_at
    }
    
    notes.append(note)

def edit_note():
    note_id = int(input("Введите номер заметки для редактирования: "))
    
    note = next((n for n in notes if n["id"] == note_id), None)

    if note:
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новый текст заметки: ")
        updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note["title"] = title
        note["body"] = body
        note["updated_at"] = updated_at
    else:
        print("Заметка с указанным номером не найдена.")

def delete_note():
    note_id = int(input("Введите номер заметки для удаления: "))
    note = next((n for n in notes if n["id"] == note_id), None)

    if note:
        notes.remove(note)
        print("Заметка успешно удалена.")
    else:
        print("Заметка с указанным номером не найдена.")

def list_notes():
    for note in notes:
        print(f"Номер: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Создано: {note['created_at']}")
        print(f"Обновлено: {note['updated_at']}")
        print("--------")

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def load_notes():
    global notes
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []

def main():
    load_notes()

    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Вывести список заметок")
        print("5. Выйти")
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            list_notes()
        elif choice == "5":
            save_notes()
            break
        else:
            print("Неверный номер действия. Попробуйте ещё раз.")

if __name__ == "__main__":
    notes = []

    main()