# One of the easiest way to make shell commands

## How to use?

Create a Python file named with the name of your command.
Here is a minimal example:

```python
import customcommand

@customcommand.command
def add_numbers(a: int, b: int):
    """Add two numbers and prints the result."""
    print(a + b)
```

Types will be automatically converted. Supported types are: `str`, `int` and `float`.
The help command is automatically generated using the function's docstring.
