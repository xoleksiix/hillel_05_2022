import functools


# MODIFY THIS DECORATOR
def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            data[target_key] = replace_with * len(data[target_key])
            return data

        return wrapper

    return decorator


# TARGET FUNCTIONS
@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {"name": name, "age": age}


# TEST OUPUT
print(get_user(name="Alice", age=30), get_user(name="Bob", age=25), sep="\n")
