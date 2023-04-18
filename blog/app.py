
from flask import Flask
from .views import index, greet_name, read_user, custom_status_code, power_value, do_zero_division, handle_zero_division_error, app


VIEWS = [
    index,
    greet_name,
    read_user,
    custom_status_code,
    power_value,
    do_zero_division,
    handle_zero_division_error
]

def create_app():
    return app

