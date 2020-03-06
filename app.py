from flask import Flask, escape, request
app=Flask(__name__)

dict_student = {"student_id":"student_name"}
dict_class = {"class_id":"class_name"}
dict_stuAndcla = {"cla_id":{"sid": "sname"}}
stu_id = 10001
cla_id = 2001

@app.route('/student', methods=['POST'])
def create_student():
    global stu_id
    name = request.get_json()['name']
    stu_id += 1
    dict_student.update({stu_id : name})
    return {
        "id" : stu_id,
        "name" : name
    }, 201

@app.route('/student/<stu_id>', methods=['GET'])
def get_student(stu_id):
    name = dict_student.get(int(stu_id))
    return {
        "id" : stu_id,
        "name" : name
    }, 201

@app.route('/class', methods=['POST'])
def create_class():
    global cla_id
    name = request.get_json()['name']
    cla_id += 1
    dict_class.update({cla_id : name})
    return {
        "id" : cla_id,
        "name" : name
    }, 201

@app.route('/class/<cla_id>', methods=['GET'])
def get_class(cla_id):
    name = dict_class.get(int(cla_id))
    return {
        "id" : cla_id,
        "name" : name
    }, 201


@app.route('/class/<cla_id>', methods=['PATCH'])
def add_student_to_class(cla_id):
    class_name = dict_class.get(int(cla_id))
    student_id = request.get_json()["stu_id"]
    student_id = int(student_id)
    student_name = dict_student.get(student_id)
    dict_stuAndcla.update({int(cla_id):{student_id:student_name}})
    return {
        "id": cla_id,
        "name": class_name,
        "student id": student_id,
        "student name": student_name
    }