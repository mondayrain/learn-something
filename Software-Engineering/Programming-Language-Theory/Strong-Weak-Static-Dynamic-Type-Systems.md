# Strong/Weak and Static/Dynamic Type Systems

Often the meanings of Strong/Static and Weak/Dynamic typing are used interchangeably. In fact, they mean different things.

Put simply, Strong/Weak typing refers to **how strictly** the types in the language are differentiated. Static/Dynamic refers to **when** the type rules are enforced.

### Strong/Weak

Languuages are often called _strongly typed_ or _weakly typed_. There is actually no universally accepted definition of what these terms mean; every language will have a different definition. But in general, they are talking about the degree to which they enforce their type rules: how "strict" it is.

In _general_, a strongly typed language is more likely to generate an error or refuse to compile if an argument passed to a function doesn't match the expected type. So, a very strongly typed language probably wouldn't do any implicit casting (e.g. accepting a float for a function that's supposed to take an int and casting it for you).

On the other hand, languages with "weak typing" will often make it easy to use the value of one type as if it were the value of another type.

### Static/Dynamic

On the other hand, static/dynamic refers to **when** we do the type-checking. 
**Static** type checking is the process of verifying the type based on analysis of the program's source. That is, types are checked at compile-time, and usually if the type rules are violated, the compiler will through a type error.

With **dynamic** type checking, type safety is verified at runtime. This is usually done by associating each runtime object with a **type tag** containing its type information. This means that if there are type errors, it will throw the exception _while_ the program is running.

Some languages allow both static and dynamic type checking, which is sometimes called **soft typing**. For example, Java supports **downcasting** types to their subtypes.

