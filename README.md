# lazy_cat_lang

Lazy cat is a programming language that aims to be so simple that any programmer can learn its features in around a half hour

# how to use

Currently there are two main ways to use lady cat, you may run a script that uses the extension .lc by using the command

```
lazy_run hello_world.lc
```

## Basics

### Variables

Lazy cat is a weak typed language so if you want to create a variable it is only required that you say its name and then its value like this:

```
var a = 10
var b = "abc"
```
### Print

To show the variables content just print it!

```
print a
print b
```

### Loops

For now there are only two types of loop, the iterative one and the not iterativo.

The iterative loop is used when you need to know the index of the loop, you can assign the index to a variable like I for example as shown below

```
for i in 1 to 5:
  print i
endfor
```

this loop will go from 1 to 5, the number of the iteration is represented by the variable I, it's also important to pay attention on the 'endfor' token, it specifies where is the end of this loop

The non iterative loop is used when you just need to repeat some action at certain number of times

```
for 1 to 5:
  print "hello world!"
endfor
```

In this example the string "hello world" will be printed 5 times

### If

the if statement is pretty simple, you just have to write a boolean expression after the 'if', if it is true the lines of code inside the block will be executed, otherwise the program will jump to the end of the block

```
var a = 1
if a < 2:
  print "1 is greater then 2!"
endif
```

in if statement we use 'endif' token to represent the end of the statement

### Functions

To create a function you just have to use the token 'fun' and define a name to your function, then you just need to define what your function does. to mark the end of the function you have to use the 'endfun' token

```
fun f:
  print "hello from function f!"
endfun

fun f2():
  print "hello from function f2!"
  f()
endfun
```

to call the function just put its name and parentheses like this:

```
f2()
```

## Current features

* Arithmetic calculations with integers
* Assignment of values in variables (only strings and integers for now)
* String concatenation
* Print function
* For loop
* For in I loop
* If block
* Functions
