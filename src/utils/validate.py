def validate_name(name):
    if not isinstance(name, str):
        return False
    if len(name) < 1 or len(name) > 50:
        return False
    if not name.isalpha():
        return False
    return True