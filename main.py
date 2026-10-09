import customcommand

@customcommand.command
def test(a:float, b: int = 5, c: str = "hello"):
    """A test function.
    This function ca do something. But that thing is very important in my program. Why?
    In case this function would not exist, this file would be empty. So it's worth having it"""
    print(f"Hello, world! a: {a}, b: {b}, c: {c}")
