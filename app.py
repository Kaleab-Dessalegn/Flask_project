from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Health Office",
        "location": "Derba Cement Factory",
        "salary": "Negotiable"
    },
    {
        "id": 2,
        "title": "Nurse",
        "location": "Derba Cement Factory",
        "salary": "Negotiable"
    },
    {
        "id": 3,
        "title": "Pharmacist",
        "location": "Derba Cement Factory",
        "salary": "Negotiable"
    },
]


@app.route("/")
def members():
    return render_template('index.html', jobs=JOBS, Company_name="Derba Cement")
# {["Kaleab","nana","Abi","maya","koki"]}


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
    # print("I am in the if")
    # app.run(debug=True)
