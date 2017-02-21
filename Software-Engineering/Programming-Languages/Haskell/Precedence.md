# Precedence

Haskell assigns numeric precedence values to its operators, with 1 being the lowest precedence and 9 being the highest.

A higher-precedence operator is applied before a lower-precedence one.

You can use **ghci** to inspect the precendence levels of operators using the **:info** command:

1```
:info(+)
```

will out put:
```
class (Eq a, Show a) => Num a where
   (+) :: a -> a -> a

infixl6 +
```

Here, the line _infixl 6 +_ tells us that the **+** operator has a precedence of 6.


