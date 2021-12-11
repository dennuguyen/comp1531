"""
HTTP requests: GET, POST, DELETE
Body content type: application/json
Data type: string
"""
import flask

APP = flask.Flask(__name__)
NAME_LIST = []


@APP.route('/reset', methods=['POST'])
def reset():
    """
    Reset server state
    """
    global NAME_LIST  # pylint: disable=W0603
    NAME_LIST = []  # Reset the NAME_LIST
    return flask.jsonify({})  # Return {} on success


@APP.route('/name', methods=['GET'])
def list_names():
    """
    Returns the NAME_LIST
    """
    global NAME_LIST  # pylint: disable=W0603
    return flask.jsonify({'name': NAME_LIST})


@APP.route('/name/add', methods=['POST'])
def add_name():
    """
    Adds a name to NAME_LIST
    """
    global NAME_LIST  # pylint: disable=W0603
    NAME_LIST.append(flask.request.get_json()['name'])
    return flask.jsonify({})  # Return {} on success


@APP.route('/name/remove', methods=['DELETE'])
def remove_name():
    """
    Removes the name from NAME_LIST if it exists
    """
    global NAME_LIST  # pylint: disable=W0603
    name = flask.request.get_json()['name']
    if name in NAME_LIST:
        NAME_LIST.remove(name)
    return flask.jsonify({})  # Return {} on success


if __name__ == "__main__":
    APP.run(debug=True)

# # Adds a name to NAME_LIST using a form
# @APP.route('/name/add', methods=['GET', 'POST'])
# def add_name_form():

#     global NAME_LIST

#     try:
#         if flask.request.method == 'GET':
#             # Return the html form
#             return '''<form method="POST">
#                     name: <input type="text" name="name"><br>
#                     <input type="submit" value="Submit"><br>
#                     </form>'''
#         elif flask.request.method == 'POST':
#             # Get data from form
#             NAME_LIST.append(flask.request.form.get('name'))
#             return flask.jsonify({})

#     except Exception:
#         pass

# @APP.route('/name/add', methods=['POST'])
# # Adds a name to NAME_LIST using a query string
# def add_name_query():

#     global NAME_LIST

#     try:
#         if flask.request.method == 'POST':
#             # Get data from query string in form ?name=<put name here>
#             NAME_LIST.append(flask.request.args.get('name'))
#             return ('ok')

#     except Exception:
#         pass

# @APP.route('/name/remove/<string:name>', methods=['DELETE'])
# def remove_name(name):

#     global NAME_LIST

#     try:
#         if flask.request.method == 'DELETE':
#             # Check if name exists then remove it
#             if name in NAME_LIST:
#                 NAME_LIST.remove(name)
#                 return flask.jsonify({})

#             # Failed to get the name
#             return ('Name does not exist.')

#     except Exception:
#         pass
