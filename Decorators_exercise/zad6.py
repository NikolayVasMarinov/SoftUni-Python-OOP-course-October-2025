def tags(tag: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            return f"<{tag}>{text}</{tag}>"

        return wrapper
    return decorator