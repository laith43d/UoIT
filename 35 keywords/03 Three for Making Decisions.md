#if
Starts a conditional BLOCK by checking the truth-value of the EXPRESSION that follows it; the STATEMENT(s) indented underneath the if will be executed only if the EXPRESSION is considered True.

#elif
Optionally continues a conditional by adding another BLOCK; if present it must follow either the initial if or another elif . Behaves exactly like an if , except that its conditional EXPRESSION will only be evaluated when no previous if /elif STATEMENT has evaluated as True.

#else
Optionally terminates a conditional by adding a final BLOCK; if present it must follow the last if /elif in the BLOCK. If no previous if /elif STATEMENT evaluated to True then the indented STATEMENT(s) below else will be run.
Can also be used to terminate blocks started with other KEYWORDs; see for , while , and try below.

