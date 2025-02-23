from flask import Flask, render_template, request
import random
from datetime import datetime
import string

app = Flask(__name__)


def generate_password(length=12, use_letters=True, use_numbers=True, use_special_chars=True):
    letters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation

    characters = ''
    if use_letters:
        characters += letters
    if use_numbers:
        characters += numbers
    if use_special_chars:
        characters += special_chars

    if not characters:
        return "Выберите хотя бы один тип символов"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.route('/', methods=['GET', 'POST'])
def index():
    generated_password = None
    time = None

    if request.method == 'POST':
        use_letters = 'btncheck1' in request.form
        use_numbers = 'btncheck2' in request.form
        use_special_chars = 'btncheck3' in request.form
        password_length = int(request.form.get('password_length', 12))

        generated_password = generate_password(
            length=password_length,
            use_letters=use_letters,
            use_numbers=use_numbers,
            use_special_chars=use_special_chars
        )

        time = datetime.now().strftime("%H:%M:%S")

    return render_template('index.html', generated_password=generated_password, time=time)


if __name__ == '__main__':
    app.run(debug=True)
