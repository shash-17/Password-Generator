from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)
 
def generate_password(length):
    """Generates a strong random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        length = int(request.json.get('length', 12))  # Default length 12
        if length < 6 or length > 32:
            return jsonify({'error': 'Password length must be between 6 and 32'}), 400
        password = generate_password(length)
        return jsonify({'password': password})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
