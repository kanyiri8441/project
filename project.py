from flask import Flask,redirect,make_response,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("movie.html")


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
@app.route('/movie')
def movie():
   dict = {'action':1998,'demons':1960,'horror':2000}
   return render_template('movie.html', movie = dict)



if __name__ == '__main__':
   app.run(debug = True)