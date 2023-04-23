from datetime import datetime
from typing import Optional

from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exception, context) -> Optional[Response]:
    response: Optional[Response] = exception_handler(exception, context)

    if response is None:
        return response

    if "detail" not in response.data:
        response.data = {"detail": response.data}

    response.data.update({"status_code": response.status_code})
    response.data.update(
        {"datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    )

    return response
