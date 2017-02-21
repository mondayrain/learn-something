# Haskell

### Environment

There are 2 main implementations of Haskell: **Hugs**, an interpreter used mostly for teacing, and **Glasgow Haskell Compiler (GHC)**, which is more popular for "real" applications.

GHC has 3 main components:
**ghc**, an optimizing compiler that generates native code.

**ghci**, an interactive interpreter and debugger.

**runghc**, a program for running Haskell programs as scripts, without needing to compile them first.

Haskell's default standard library is called **Prelude**. It is defined by the Haskell 98 standard and is always implicitly available. It is sometimes referred to as "the standard prelude".

### GHCI

When running GHCI, the word _Prelude_ in the prompt indicates that _Prelude_ is loaded and ready to use. When we load other modules or source files, they will show up in the prompt, too.

To keep the prompt from growing too long, you can set the prompt with **:set prompt "prompt here> "**

To use definitions from modules other than prelude, we have to load them using the **:module** command.

**:?** will print a help message.


