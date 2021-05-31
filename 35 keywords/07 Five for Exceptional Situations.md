#raise

1. Used to raise a specified EXCEPTION, which will cause the program to stop immediately and exit if not handled by an except BLOCK.
2. If used without an argument inside an except or finally BLOCK, re-raises the EXCEPTION being handled by the BLOCK.

#assert

Used to test if some EXPRESSION is considered True, and if not raise an AssertionError.

#try

Starts an exception handler BLOCK; must be followed either an except BLOCK, an else block or a finally BLOCK in order to be valid syntax.


#except

Optionally continues an exception handler BLOCK by catching EXCEPTIONs; can (and should) be limited to specific types of EXCEPTION. More than one of these can follow a try and each will be checked in turn until either the EXCEPTION is handled or no more except statements remain.


#finally

Optionally cleans up an exception handler BLOCK to provide a means of always performing some action whether or not the EXCEPTION was handled. Must follow any except BLOCKS that are present, as well as the optional else BLOCK if that is also present. If no except BLOCK is present then finally must terminate the exception handler.

## examples

```
try:
    [connect to database]
    [query the database]
except ConnectionError as error:
    [log the error]
else:
    [log success]
finally:
    [close the connection]
```

