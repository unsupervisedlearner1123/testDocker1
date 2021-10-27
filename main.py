from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    
    file = open("count.txt","r")
    count = int(file.read())
    file.close()
    
    count+=1
    
    file = open("count.txt","w")
    file.write(str(count))
    file.close()
    
    return render_template("index.html", count=count)
    
@app.route('/about')
def about():
    return "The about page"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)