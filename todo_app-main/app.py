#calling flask
from flask import Flask, render_template, request, redirect , url_for

#creating app instance
app = Flask(__name__, template_folder="templates")

tasks = []


#Rotuing 
@app.route("/")

def home():
    return render_template("index.html", tasks=tasks)

#creating an instance or function
@app.route("/add_tasks", methods=["POST"])

def create_task(): #Creating the task
    task = request.form.get("task")#
    tasks.append(task)
    return redirect(url_for("home")) #Calling the page


#debugging
if __name__ == "__main__":
    app.run(debug=True)

