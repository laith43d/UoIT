#async

1. Used to mark another KEYWORD as one that works asynchronously. As such, `async` cannot appear on its own.
2. With `def` as `async def` to define an asynchronous function, also known as a COROUTINE.
3. With `for` as `async for` to loop over an asynchronous iterator inside an `async def` .
4. With `with` as `async with` to use an asynchronous context manager inside an `async def`.

#await

Used to suspend the execution of the COROUTINE it is found within and waits for the COROUTINE to its right to complete; can only be used inside an `async def` .

