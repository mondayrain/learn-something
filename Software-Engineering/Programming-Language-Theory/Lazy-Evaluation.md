# Lazy Evaluation

**Lazy Evaluation** (also known as **Call-by-Need**) is an evaluation strategy that delays the evaluation of the expression until its value is needed. It also tries to avoid repeated evaluations. It is the opposite of **eager evaluation**, in which an expression is evaluated as soon as it is bound to a variable. Eager evaluation is used by most traditional programming languages, whereas lazy evaluation is used particularly in functional programming languages.

In lazy programming langauges, an expression is not evaluated until the evaluator is _forced_ to produce the expression's value (usually because something is depending on it).

For example, if we have a statement like **x = expression**, what is actually in x is irrelevant until something somewhere actually has to use x. So, in an eager language, _expression_ would be evaluated then placed in x, whereas in a lazy language, we wouldn't evaluate the expression until x is actually used somewhere.

### Applications

**Infinite Lists**

Delaying evaluation lets us create calculable infinite lists, without infinite loops or size intefering with computation. Often, infinite lists are called **streams**. 

**Control Structures**

In almost all common "eager" languages, _if_ statements evaluate in a lazy fashion (e.g. if **a** && **b**; if **a** is False, we already know the expression is False and do not need to evaluate **b**).

If the whole language is lazy, then all control structures are consistent with the rest of the language's evaluation.

### Why isn't Lazy Evaluation used everywhere?

The reason why most languages _aren't_ lazy is that laziness interferes with order of evaluation. In languages with side effects, we often have to evaluate things in the "right" order: hence, things need to be eagerly evaluated. However, in purely functional languages, where expressions have no side effect, there is no risk in lazy evaluation.

Put simply: mutable state + lazy evaluation = death.

### Cons of Lazy Evaluation

Lazyness incurs a significant overhead from keeping non-evaluated expressions around:
- Use up storage!
- Slower to work with than simple values

Sometimes you have to eager-ify code to make it fast enough.

As well, lazy evaluation also implies early optimization.

