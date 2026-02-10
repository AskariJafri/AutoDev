from flask import Flask, jsonify, request
from backend.database import User  # Import updated database model

app = Flask(__name__)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    limit = int(request.args.get('limit', 10))  # Default limit to 10 records per page
    offset = int(request.args.get('offset', 0))
    users = User.query.offset(offset).limit(limit)
    data = [user.to_dict() for user in users]
    return jsonify(data), 200

if __name__ == '__main__':
    app.run()