from flask import Flask, request, jsonify
from backend/services import register_user_service
from backend.validators import UserRegistrationSchema
from backend.database import db

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
    try:
        # Validate user input
        schema = UserRegistrationSchema()
        validated_data = schema.validate(request.json)

        # Call business logic layer to perform registration
        result = register_user_service(validated_data)
        db.session.add(result)
        db.session.commit()

        return jsonify({"status": "success", "message": "User registered successfully"}), 201

    except ValidationError as e:
        logger.warning(f"Validation error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        logger.error(f"Error registering user: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)