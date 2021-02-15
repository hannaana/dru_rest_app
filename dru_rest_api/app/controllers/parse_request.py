from flask import request


def get_request_data():
    """
    Get keys & values from request (Note that this method should parse requests with content type "application/x-www-form-urlencoded")
    """
    # data = request.form
    data = list(request.forms.keys())[0]
    return data