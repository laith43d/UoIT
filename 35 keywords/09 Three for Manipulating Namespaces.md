#global

Used to declare a NAME as part of the global namespace; the NAME cannot have been used previously in the same namespace. In effect this allows a local STATEMENT to both create and assign to a global NAME it otherwise could only read. Can be used within the global namespace, but has no effect.

#nonlocal

Used exclusively inside nested functions / methods (also known as closures) to bind a pre-existing NAME in the parent’s namespace. This allows a STATEMENT in the child to have write access to a NAME defined in its parent. Must appear before any reference to that NAME in the local scope.

#del

1. Used to delete a NAME (or NAMEs) from a namespace; if no other references exist to the OBJECT that NAME referred to, the underlying OBJECT is deleted as well.
2. Can also be used to delete an attribute of an OBJECT or a member (or members) of a COLLECTION if the specific type has allowed this operation.
