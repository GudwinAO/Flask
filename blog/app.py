
from .views import index, greet_name, read_user, custom_status_code, power_value, do_zero_division, handle_zero_division_error, app
from blog.views.users import users_app
from blog.views.articles import articles_app

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

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")