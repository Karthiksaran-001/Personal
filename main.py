from flask import Flask,request,jsonify,render_template,redirect
from flask_cors import CORS,cross_origin 


app =app = Flask(__name__ , template_folder= "templates")


@app.route('/' , methods =['GET'])
@cross_origin()
def index():
    return render_template('html/index.html')



if __name__ == '__main__':
    app.run(debug=True)