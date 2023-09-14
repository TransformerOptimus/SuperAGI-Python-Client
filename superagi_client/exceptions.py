class BadRequestException(Exception):
    def __init__(self, message="Bad Request", status_code=400, additional_info=None):
        self.message = message
        self.status_code = status_code
        self.additional_info = additional_info
        super().__init__(
            f"{self.message} => {self.additional_info}"
            if self.additional_info
            else self.message
        )


class UnauthorizedException(Exception):
    def __init__(self, message="Unauthorized", status_code=401, additional_info=None):
        self.message = message
        self.status_code = status_code
        self.additional_info = additional_info
        super().__init__(
            f"{self.message} => {self.additional_info}"
            if self.additional_info
            else self.message
        )


class NotFoundException(Exception):
    def __init__(self, message="Not Found", status_code=404, additional_info=None):
        self.message = message
        self.status_code = status_code
        self.additional_info = additional_info
        super().__init__(
            f"{self.message} => {self.additional_info}"
            if self.additional_info
            else self.message
        )


class ConflictException(Exception):
    def __init__(self, message="Unauthorized", status_code=409, additional_info=None):
        self.message = message
        self.status_code = status_code
        self.additional_info = additional_info
        super().__init__(
            f"{self.message} => {self.additional_info}"
            if self.additional_info
            else self.message
        )


class UnprocessableContentException(Exception):
    def __init__(
        self, message="Unprocessable Content", status_code=422, additional_info=None
    ):
        self.message = message
        self.status_code = status_code
        self.additional_info = additional_info
        super().__init__(
            f"{self.message} => {self.additional_info}"
            if self.additional_info
            else self.message
        )


class InternalServerErrorException(Exception):
    def __init__(
        self, message="Internal Server Error", status_code=500, additional_info=None
    ):
        self.message = message
        self.status_code = status_code
        self.additional_info = additional_info
        super().__init__(
            f"{self.message} => {self.additional_info}"
            if self.additional_info
            else self.message
        )


def http_status_code_to_exception(status_code, additional_info):
    status_code_to_exception_map = {
        400: BadRequestException,
        401: UnauthorizedException,
        404: NotFoundException,
        409: ConflictException,
        422: UnprocessableContentException,
        500: InternalServerErrorException,
    }

    exception = status_code_to_exception_map.get(status_code)
    raise Exception(status_code, additional_info) if exception is None else exception(
        additional_info=additional_info
    )
