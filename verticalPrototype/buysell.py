# library.py
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)
# Database connection info. Note that this is not a secure connection.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '#PASSWORD OF DB#'
app.config['MYSQL_DATABASE_DB'] = 'prototypedb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
#endpoint for search
@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
    #COPY FROM HERE, PLEASE MODIFY THE COLUMN NAMES IN THE QUERY AS NECESSARY
        category = request.form['category']
        item = request.form['item']
        # all in the search box will return all the tuples
        if len(item) == 0:
            if category == "All":
                cursor.execute("SELECT P.title, P.description, C.name FROM posts P, categories C WHERE P.category=C.cID")
                conn.commit()
                data = cursor.fetchall()
            else:
                cursor.execute("SELECT P.title, P.description, C.name FROM posts P, categories C WHERE P.category = C.cID AND C.name = '%s'" %(category))
                conn.commit()
                data = cursor.fetchall()
        # search by category
        else:
            if category == "All":
                cursor.execute("SELECT P.title, P.description, C.name FROM posts P JOIN categories C ON P.category = C.cID WHERE P.description LIKE '%%%s%%' OR P.title LIKE '%%%s%%'" %(item, item))
                conn.commit()
                data = cursor.fetchall()
            else:
                cursor.execute("SELECT P.title, P.description, C.name FROM posts P JOIN categories C ON P.category = C.cID WHERE C.name = '%s' AND (P.description LIKE '%%%s%%' OR P.title LIKE '%%%s%%')" %(category, item, item))
                conn.commit()
                data = cursor.fetchall()
    #END COPY HERE
        return render_template('search.html', data=data)
    return render_template('search.html')
if __name__ == '__main__':
    app.debug = True
    app.run()
