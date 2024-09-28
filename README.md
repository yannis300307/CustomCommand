# One of the easyest way to make shell commands

## How to use?

Create a Python file named with the name of your command.
Here is a minimal exemple:

```python
import customcommand

@customcommand.command
def add_numbers(a:int, b:int):
    """Add the two numbers and print the result."""
    print(a + b)

customcommand.handle_commands()
```

Types will be automatically converted. Supported types are: `str`, `int` and `float`.
