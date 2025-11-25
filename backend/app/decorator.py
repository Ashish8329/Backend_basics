from rest_framework.pagination import LimitOffsetPagination
from functools import wraps


def add_pagination(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        result = func(self, request, *args, **kwargs)
        paginator = LimitOffsetPagination()
        paginated = paginator.paginate_queryset(result.data, request, view=self)

        if paginated is not None:
            return paginator.get_paginated_response(paginated)

        # Fallback: normal response
        return result

    return wrapper
