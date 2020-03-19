# rememberTheApplePy
A ToDo App built with Python

## API
Is the Python REST API the frontend will use to interact with the backend/DB

start development env
`python API/run.py`

### Spec
* Python 3.8
* SQLite
* pipenv
* Flask for Web Framework
* SQLAlchemy for ORM
* Marshmallow for serialization

### REST Endpoints
* AddTodo
* GetAllTodos
* UpdateTodo
* DeleteTodo


### Todo Item Fields
Each todo will contain
* ID - integar
* Title - string
* Description (maybe) - string
* Date Added - date
* Date Due (maybe) - date
* complete - boolean


## Client
Is the frontend app that will connect to the REST API.

start development env
`cd client`
`npm start`

### Spec
* NPM
* ReactJS
* HTML/CSS Framework ??

### Components
There will be two high level components:
* List of Todo's - TodoList
* Form to add a todo - AddTodo