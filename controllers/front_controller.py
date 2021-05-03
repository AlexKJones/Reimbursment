from controllers import employee_controller, home_controller, request_controller


def route(app):
    # Calls all other other controllers
    employee_controller.route(app)
    home_controller.route(app)
    request_controller.route(app)
