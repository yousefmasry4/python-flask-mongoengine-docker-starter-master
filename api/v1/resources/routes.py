# some_file.py
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(0, '/code')
from api.v1.resources.todos import todos


def initialize_routes(apis):
    apis.add_namespace(todos)
