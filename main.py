import customcommand


@customcommand.command
def test(a:float, b: int = 5, c: str = "hello"):
    """A test function.
    That make things. But that things are very important in my program. Why?
    I don't know... If I remove it, it's not working the yeah, I will keep it."""
    print("salut")


customcommand.handle_commands()
