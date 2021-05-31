#lambda

Used to define a CALLABLE anonymous function and its signature.

#def

1. Used to define a named function and its signature, the indented BLOCK that follows can then be re-used by calling that NAME using the function() syntax.
2. If used inside a class defines a named method instead, which is called using the class.method() syntax.
3. Can also be marked with `async` , to start an `async def`

#return

Used to immediately give up control and end execution of the function at the point at which it is encountered. If followed by an EXPRESSION, that is evaluated first and the resulting OBJECT is given back to the caller of the function. If no EXPRESSION is present None is returned instead. Has no meaning outside a function, thus if present at all it must be inside a BLOCK that follows a def .

#yield

1. Used to immediately pause execution and temporarily give up control at the point at which it is encountered. If followed by an EXPRESSION, that is evaluated first and the resulting OBJECT is yielded back to the caller of the function; if no EXPRESSION is present None is yielded instead. Has no meaning outside a function, thus if present at all it must be used inside a BLOCK that follows a def .
2. Can be modified by `from` to form `yield from`.

