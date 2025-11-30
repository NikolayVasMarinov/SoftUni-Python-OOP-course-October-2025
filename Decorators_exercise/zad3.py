def make_bold(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"<b>{text}</b>"

    return wrapper

def make_italic(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"<i>{text}</i>"

    return wrapper

def make_underline(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"<u>{text}</u>"

    return wrapper