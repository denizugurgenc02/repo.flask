from flask import jsonify
from werkzeug.exceptions import HTTPException


class ErrorHandler:
    @staticmethod
    def init_app(app):
        @app.errorhandler(Exception)
        def handle_exception(e):
            if isinstance(e, HTTPException):
                response = {"error": e.name, "message": e.description, "code": e.code}
                return jsonify(response), e.code

            response = {
                "error": "Internal Server Error",
                "message": f"Flask error: {e}",
                "code": 500,
            }
            return jsonify(response), 500
