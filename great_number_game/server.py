from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)


app.secret_key = 'super secret key'


@app.route('/')
def start_game():
    # session['key'] = random.randint(1, 100)
    # print(session['chance'])
    # session['list'] = []
    # print(session['list'])
    if 'key' in session:
        print(session['key'])
    if 'key' not in session:
        session['key'] = random.randint(1, 100)
    if 'chance' in session:
        print(session['chance'])
    if 'chance' not in session:
        session['chance'] = 0
    if 'list' in session:
        print(session['list'])
    if 'list' not in session:
        session['list'] = []
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    print(session['key'])
    print(request.form)
    print(session['list'])
    my_number = request.form['guess']
    # print(type(session['key']))  # type() prints the TYPE (i.e class 'int') for the value in the parenthesis.
    if int(my_number) == session['key']:
        session['chance'] += 1
        print(session['chance'])
        session['list'].append('you win!')
        print(session['list'])
        return redirect('/')
    if int(my_number) > session['key']:
        session['chance'] += 1
        print(session['chance'])
        session['list'].append('Too High')
        print(session['list'])
    if int(my_number) < session['key']:
        session['chance'] += 1
        print(session['chance'])
        session['list'].append('Too low')
        print(session['list'])
    if session['chance'] >= 3:
        return 'You are out of chances, go back to play again!'
    return redirect('/')  # If everything is broken (or all else fails) This is a fail safe, Or Someone puts in an improper Value or invalid Value then send them back to the main page or the beginning.


@app.route('/clear')
def clear_data():
    session.clear()
    return redirect('/')


# Uncomment if I want to use my refresh game feature. I don't need both refresh and clear data because clear data clears my Session (cookies) and then I can start over Because clear data Redirects me back to the home page and my form redirects me back to my home page, so that means I am starting a new game when I clear my data (I have to in order to play another game).
# @app.route('/refresh')
# def refresh_game():
#     return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)