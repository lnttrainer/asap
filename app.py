from flask import *
from database import Criminal

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/addcriminalform")
def addcriminalform():
    return render_template("addcriminalform.html")

# This function reads the new criminal data and calls the DB function
@app.route("/addcriminal", methods=["POST"])
def addcriminal():
    message = "Criminal Data inserted"

    if request.method == "POST":
        formData = request.form
        try:
            cri.InsertCriminal(formData)
        except:
            message = "Error encountered. Can't Insert Data"

    return render_template("criminalinserted.html", insertmessage=message)

@app.route("/showallcriminals")
def showallcriminals():
    CriminalData = cri.AllCriminals()
    return render_template("showallcriminals.html", data=CriminalData)

@app.route("/showcriminalupdate/<int:id>")
def showcriminalupdate(id):
    criminaldata = cri.RetrieveCriminal(id)[0]
    return render_template("showcriminalupdate.html", data=criminaldata)

@app.route("/updatecriminal", methods=["POST"])
def updatecriminal():
    if request.method == "POST":
        formData = request.form
        cri.UpdateCriminal(formData)

    CriminalData = cri.AllCriminals()
    return render_template("showallcriminals.html", data=CriminalData)

@app.route("/deletecriminal/<int:id>")
def deletecriminal(id):
    cri.DeleteCriminalData(id)
    CriminalData = cri.AllCriminals()
    return render_template("showallcriminals.html", data=CriminalData)

if __name__ == "__main__":
    DbName = "./database/criminals.db"  # Database Name

    cri = Criminal(DbName)  # New criminal object
    cri.CreateDBT()  # DB and Table creation
    app.run(debug=True)