# Python Anti-patterns

## Mutable Default Arguments

- Avoid using mutable objects (lists, dictionaries) as default arguments
- Use None as default and initialize inside the function

## Global Variables

- Minimize use of global variables
- Use class attributes or function parameters instead
- Consider using dependency injection

## Exception Handling

- Don't use bare except clauses
- Be specific about exceptions to catch
- Don't use exceptions for flow control

## String Concatenation

- Avoid using + for string concatenation in loops
- Use str.join() or f-strings instead

## List Comprehensions

- Don't use list comprehensions for side effects
- Keep list comprehensions simple and readable

## Import Statements

- Don't use wildcard imports (\*)
- Group imports (standard library, third-party, local)
- Use absolute imports over relative imports

## Class Design

- Avoid too many instance attributes
- Don't use @staticmethod unless necessary
- Prefer composition over inheritance

## Function Design

- Functions should do one thing
- Avoid too many parameters
- Use type hints for better documentation

## Resource Management

- Always use context managers (with statements)
- Don't leave file handles open
- Clean up resources properly

## Testing

- Don't test implementation details
- Avoid complex test setup
- Use meaningful test names
