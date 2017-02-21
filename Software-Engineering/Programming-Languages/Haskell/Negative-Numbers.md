# Negative Numbers

We often have to enclose a negative number in parentheses. This is because negative numbers like "-3" aren't a "negative number", they're the number "3" with the **-** operator applied to it.

The **-** operator is Haskell's only unary operator and we can't mix it with infix operators.

For example,
_2 + -3_
will give the error:

_Precedence parsing error, cannot mix "+' [infixl 6] and prefix '-' [infixl 6] in the same infix expression_

So, if we want to use unary minus near an infix operator, we need to wrap the expression it applies to with a parentheses.

_3 + (-3)_

_3 + (-(13 * 37))_

This avoids a parsing ambiguity.

e.g. _f-3_ . Does this mean :"apply function f to the number -3" or "subtract 3 from the variable f"? The parentheses helps us with this!

Actually, **the unary minus is syntactic sugar for the Prelude function _negate_**.

