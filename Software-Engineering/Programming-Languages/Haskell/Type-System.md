# Haskell's Type System

In Haskell, types are _strong_, _static_, and can be automatically _inferred_.

### Strong

When a program doesn't comply with Haskell's type rules, there will be a **type error**. Haskell will not automatically coerce/cast from one type to another (e.g. It won't cast from an int to a float for us). In other words, the types in Haskell are very _strictly_ distinguished.


### Static

The compiler knows the type of every value and every expression at compile time, before any code is executed. It will detect when we try to use expressions whose types don't match, and reject our code with an error message before we run it.

However, Haskell also has **typeclasses**, which tries to provide all the benefits of dynamic typing.

### Inference

The Haskell compiler can automatically deduce the types of almost all expressions in the program. Although we can explicitly declare the type of any value, type inference means that this is almost always option.

### Why?

Strong, static typing makes Haskell safe, and type inference makes it concise.

### Aside: Impure functions

Haskell tells us whether a function is pure or impure (whether it has a side effect) through its type signature. The type of the function's result will be gin with **IO** if there is a side-effect.

```
ghci> :type readFile
readFile:: FilePath -> IO String
```

So, Haskell's type system also prevents one from accidentally mixing pure and impure code.
 
