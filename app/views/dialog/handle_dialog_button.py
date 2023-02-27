def handle_add_new_student(controller):
    def callback(x):
        controller.add_student_in_table()
    return callback

def hadle_cancel_add_new_student(controller):
    def callback(x):
        controller.close_window()
    return callback

def handle_filter_student(controller):
    def callback(x):
        controller.filter()
    return callback