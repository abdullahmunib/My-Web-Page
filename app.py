from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def home():
    my_name = "Abdullah Munib"  
    
    my_learnings = ["Python Automation", "HTML & CSS", "Flask Server", "Debugging"]

    return render_template("index.html", name_in_html=my_name, skills_list=my_learnings)

if __name__ == "__main__":

    app.run(debug=True)
