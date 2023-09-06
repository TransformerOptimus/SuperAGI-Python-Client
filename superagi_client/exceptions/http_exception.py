from superagi_client.exceptions.bad_request_exception import BadRequestException
from superagi_client.exceptions.conflict_exception import ConflictException
from superagi_client.exceptions.internal_server_error_exception import (
    InternalServerErrorException,
)
from superagi_client.exceptions.not_found_exception import NotFoundException
from superagi_client.exceptions.unauthorized_exception import UnauthorizedException
from superagi_client.lib.logger import logger


def http_status_code_to_exception(status_code, additional_info):
    status_code_to_exception_map = {
        400: BadRequestException,
        401: UnauthorizedException,
        404: NotFoundException,
        409: ConflictException,
        500: InternalServerErrorException,
    }

    exception = status_code_to_exception_map.get(status_code)
    if exception is None:
        logger.error(f"Status Code:{status_code}, Additional Info:{additional_info}")
    raise Exception() if exception is None else exception(
        additional_info=additional_info
    )
