#calling flask
from flask import Flask, render_template, request, redirect , url_for

#creating app instance
app = Flask(__name__, template_folder="templates")

tasks = []


#Rotuing 
@app.route("/")

def home():
    return render_template("work.html", tasks=tasks)

#creating an instance or function
@app.route("/add_tasks", methods=["POST"])

def create_task(): #Creating the task
    task = request.form.get("task")#
    tasks.append(task)
    return redirect(url_for("home")) #Calling the page

#The delete task deletes the user tasks when the user clicks the delete button
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    del tasks [task_id]
    
    return redirect(url_for('home'))

#debugging
if __name__ == "__main__":
    app.run(debug=True)


