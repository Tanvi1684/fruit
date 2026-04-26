from flask import Flask,render_template,request,url_for
#import mysql.connector
app=Flask(__name__,template_folder='templates')


#db=mysql.connector.connect(
 #   host="localhost",
  #  user="root",
   # passwd="",
    #database="python_db"
#)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/chackout')
def chackout():
    return render_template('chackout.html')
@app.route('/shop')
def shop():
    return render_template('shop.html')
@app.route('/shop-detail')
def shop_detail():
    return render_template('shop-detail.html')
@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
       # name=request.form['name']
        #email=request.form['email']
        #message=request.form['message']
        #cursor=db.cursor()
        #sql="INSERT INTO flask_tbl(name,email,message) VALUES(%s,%s,%s)"
        #val=(name,email,message)
        #cursor.execute(sql,val)
        #db.commit()
        return "successed"

    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)
