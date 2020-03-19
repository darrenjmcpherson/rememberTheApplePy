from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Success'

#Create todo
@main.route('/todo/create') #, methods=['POST'])
def createTodo():
    return 'Create todo'

#Read all todos
@main.route('/todo') #, methods=['GET'])
def getAllTodos():
    return 'Get todos'

#Update todo
@main.route('/todo/update')#, methods=['PUT'])
def updateTodo():
    return 'Update todo'

#Delete todo
@main.route('/todo/delete')#, methods=['DELETE'])
def deleteTodo():
    return 'Delete Todo'



