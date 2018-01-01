# lazy_cat_lang

Lazy cat is a programming language that aims to be so simple that any programmer can learn its features in around a half hour

# how to use

Currently there are two main ways to use lady cat, you may run a script that uses the extension .lc by using the command

```
lazy_cat hello_world.lc
```

## Basics

* variables

Lazy cat is a weak typed language so if you want to create a variable it is only required that you say its name and then its value like this:

```
a = 10
b = "abc"
```
* print

To show the variables content just print it!

```
print a
print b
```

* loops

For now there are only two types of loop, the iterative one and the not iterativo.

The iterative loop is used when you need to know the index of the loop, you can assign the index to a variable like I for example as shown below

```
for i in 1 to 5:
  print i
end
```

this loop will go from 1 to 5, the number of the iteration is represented by the variable I, it's also important to pay attention on the 'end' token, it specifies where is the end of this loop

The non iterative loop is used when you just need to repeat some action at certain number of times

```
for 1 to 5:
  print "hello world!"
end
```

In this example the string "hello world" will be printed 5 times

* If

the if statement is pretty simple, you just have to write a boolean expression after the 'if', if it is true the lines of code inside the block will be executed, otherwise the program will jump to the end of the block

```
a = 1
if a < 2:
  print "1 is greater then 2!"
end
```

in if statement we also use 'end' token to represent the end of the statement

* Procedures

Procedures are functions without parameters

```
fun f:
  print "hello world!"
end

f()
```

## current features

* arithmetic calculations with integers
* assignment of values in variables (only strings and integers for now)
* string concatenation
* print function
* for loop
* for in I loop
* if block
* procedures
