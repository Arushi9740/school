students = {'001' : ['5','hgd739'],
            '002' : ['3','rq67M'],
            '003' : ['6','gtcU87Z'],
            '004' : ['hyd782O']
            }

Students_id = {}

def add_students(ID,name):
    if ID in Students_id:
        return "Student already exist"
    else:
        Students_id[ID] = name
        return "Student added"
    
def view_students(id):
    if id in Students_id:
        return f"{id} : {Students_id[id]}"
    return "Student ID not found"

def left_out(ID):
    for i in range(students):
        if i not in Students_id:
            return f"Student left : {i}"
        return "No students left more"
    
    
# if __name__=='__main__':
#     id = "005"
#     name = "nithya"
#     print(add_students(id,name))
#     print(view_students("005"))
#     i = "001"
#     n = "manu"
#     print(add_students(i,n))
#     print(add_students(i,n))
    
    
