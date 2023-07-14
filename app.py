from flask import Flask, render_template
from database import engine
from sqlalchemy import text


app = Flask(__name__)


# JOBS = [
#     {
#         "id": 1,
#         "title": "Health Office",
#         "location": "Derba Cement Factory",
#         "salary": "Negotiable"
#     },
#     {
#         "id": 2,
#         "title": "Nurse",
#         "location": "Derba Cement Factory",
#         "salary": "Negotiable"
#     },
#     {
#         "id": 3,
#         "title": "Pharmacist",
#         "location": "Derba Cement Factory",
#         "salary": "Negotiable"
#     },
# ]

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from clients"))
    jobs = []
    for row in result.all():
        jobs.append(row._mapping)
    return jobs


@app.route("/")
def members():
    jobs = load_jobs_from_db()
    return render_template('index.html', jobs=jobs, Company_name="Derba Cement")
# {["Kaleab","nana","Abi","maya","koki"]}


# @app.route("/jobs")
# def list_jobs():
#     return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
    # print("I am in the if")
    # app.run(debug=True)
