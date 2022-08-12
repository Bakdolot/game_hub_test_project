from http import HTTPStatus

from django.db.models import IntegerChoices, Choices


def extend_enum(inherited_enum):
    """
    Function to inherit from Enum
    """
    def wrapper(added_enum):
        joined = {}
        for item in inherited_enum:
            joined[item.name] = item.value
        for item in added_enum:
            joined[item.name] = item.value
        return Choices(added_enum.__name__, joined)
    return wrapper


@extend_enum(HTTPStatus)
class HTTPStatusChoice(IntegerChoices):
    pass
