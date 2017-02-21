# Referential Transparency

**Referential Transparency** is a property that a computer program/language can have.

An _expression_ is referentially transparent if it can be replaced with a corresponding value without changing the program's behaviour. In other words, **evaluating a referentially transparent function gives the same value for the same arguments**.

_Put simply_:

Same args --> f(x) --> Same output.
Every time.

Sometimes, these functions are also called **pure functions**.
If all functions involved in an expression are pure functions, then the whole expression is referentially transparent.

Any function/expression that is _not_ referentially transparent is called **referentially opaque**.

### Functions & Methods & Procedures

In math, all functions are referentially transparent by definition. However, this isn't tru in programming.

Sometimes, people will use the words function/method/procedure to differentiate between whether or not a function is referentially transparent or not.

### Sequence Points & Purely Functional Programming

Suppose we have an imperative language, and we have functions A, B, and C. All 3 functions have side effects, and they'll be called in the following sequence: A, then B, then C. B depends on the side effects of A, and C depends on the side effects of B.

A **sequence point** defines any point in a computer program's execution in which it is _guaranteed_ that all side effects of previous evaluations have been performed, and no subsequent evaluations have been performed yet. So in simple terms, a sequence point is a point in the program execution where all expected side effects are evaluated before going onto the next step. In our example, B has to be **sequenced after** A, and **sequenced before** C.

In imperative languages, sequence points can be a core cocept for determining the validity of expressions.

On the other hand, because a referentially transparent expression can be evaluated at any time, it's not necessary to define sequence points or guarantee the order of evaluation _at all_. This is very unlike **imperative programming**, where substitution of an expression with its value is only valid at certain points in the program. Programming without consideration to evaluation order or sequence points is called **purely functional programming**.

