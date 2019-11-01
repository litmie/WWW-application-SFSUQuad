
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/ourTeam')
def outTeam():
    return render_template('about.html')

@app.route('/about_Alex')
def alexProfile():
    return render_template('about_team_members/about_Alex.html')

@app.route('/about_AlexLee')
def alexLeeProfile():
    return render_template('about_team_members/about_AlexLee.html')

@app.route('/about_Andrew')
def andrewProfile():
    return render_template('about_team_members/about_Andrew.html')

@app.route('/about_Emanuel')
def emanuelProfile():
    return render_template('about_team_members/about_Emanuel.html')

@app.route('/about_Kevin')
def kevinProfile():
    return render_template('about_team_members/about_Kevin.html')

@app.route('/about_Tim')
def timProfile():
    return render_template('about_team_members/about_Tim.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)