from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

# Connect to the MySQL database
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'prototypedb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


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


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        item = request.form['item']
        # Search by post name
        cursor.execute("select p.title as 'Post Title' , p.description , c.name from posts p inner join categories c on p.category = c.cID where p.title like %s", ("%" + item + "%"))
        conn.commit()
        data = cursor.fetchall()
        #TODO
        return render_template('index.html', data=data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
