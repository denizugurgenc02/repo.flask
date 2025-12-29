from datetime import datetime, timezone
from typing import Any

from flask import Response, jsonify
from flask.views import MethodView


class BaseRoutes(MethodView):
    @staticmethod
    def format_response(data: Any, pagination: bool = False) -> Response:
        response = {
            "server_time": datetime.now(timezone.utc).isoformat(),
            "count": len(data) if isinstance(data, list) else 1,
            "items": data if isinstance(data, list) else [data],
        }

        if pagination:
            pass

        return jsonify(response)
