from flask import Flask , render_template, session, redirect # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'elsecreto'

@app.route('/')  
def visits():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
        
    return render_template('index.html', counter = session['counter'])

@app.route('/destroy_session')
def destroy():
    session['counter'] = 0
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.
