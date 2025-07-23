from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = datetime.now()
        response = self.get_response(request)
        duration = datetime.now() - start_time

        logger.info(
            f"Audit - {request.method} {request.path} | "
            f"Status: {response.status_code} | "
            f"Duration: {duration.total_seconds():.2f}s"
        )

        return response
