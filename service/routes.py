from flask import jsonify, request, abort
from service import app

accounts = {}
next_id = 1

@app.route("/accounts", methods=["POST"])
def create_account():
    global next_id
    data = request.get_json()
    accounts[next_id] = data
    data["id"] = next_id
    next_id += 1
    return jsonify(data), 201

@app.route("/accounts", methods=["GET"])
def list_accounts():
    return jsonify(list(accounts.values())), 200

@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    account = accounts.get(account_id)
    if not account:
        abort(404)
    return jsonify(account), 200

@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    if account_id not in accounts:
        abort(404)
    data = request.get_json()
    data["id"] = account_id
    accounts[account_id] = data
    return jsonify(data), 200

@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    accounts.pop(account_id, None)
    return "", 204