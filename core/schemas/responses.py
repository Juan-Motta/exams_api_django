from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

import pytz


@dataclass
class ApiResponse:
    success: bool
    message: Optional[str] = None
    data: Optional[Dict] = None
    datetime: datetime = datetime.now(tz=pytz.UTC)

    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "datetime": self.datetime.strftime('%Y-%m-%dT%H:%M:%S%z'),
        }


@dataclass
class ErrorResponse(ApiResponse):
    success: bool = False


@dataclass
class SuccessResponse(ApiResponse):
    success: bool = True
