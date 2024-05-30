import pyperclip
from pynput import keyboard

# Словарь соответствия английских и русских букв
eng_to_rus = {
    'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н', 'K': 'К', 'M': 'М', 'O': 'О', 'P': 'Р', 'T': 'Т', 'X': 'Х',
    'a': 'а', 'c': 'с', 'e': 'е', 'o': 'о', 'p': 'р', 'x': 'х', 'y': 'у'
}

def replace_eng_to_rus(text):
    # Проходим по каждому символу в тексте и заменяем его, если он есть в словаре
    return ''.join(eng_to_rus.get(char, char) for char in text)

def process_clipboard():
    # Получаем текст из буфера обмена
    text = pyperclip.paste()
    # Преобразуем текст
    converted_text = replace_eng_to_rus(text)
    # Записываем преобразованный текст обратно в буфер обмена
    pyperclip.copy(converted_text)
    print("Text in clipboard has been converted.")

# Определяем комбинацию клавиш
COMBINATION = {keyboard.Key.ctrl_l, keyboard.Key.shift, keyboard.KeyCode(char='e')}
EXIT_KEY = keyboard.Key.esc

current_keys = set()

def on_press(key):
    if key in COMBINATION:
        current_keys.add(key)
        if all(k in current_keys for k in COMBINATION):
            process_clipboard()
    elif key == EXIT_KEY:
        print("Exiting...")
        return False  # Это завершит работу слушателя клавиатуры

def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass

# Запускаем слушатель клавиатуры
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Press CTRL+SHIFT+E to convert the text in the clipboard. Press ESC to exit.")
    listener.join()
