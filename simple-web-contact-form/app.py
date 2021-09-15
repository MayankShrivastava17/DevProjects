from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display', methods=['get', 'post'])
def display():
    name = request.form.get('name')
    email = request.form.get('email')
    issue = request.form.get('select')
    message = request.form.get('message')
    return render_template(
        'detail.html',
        name=name,
        email=email,
        issue=issue, 
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)