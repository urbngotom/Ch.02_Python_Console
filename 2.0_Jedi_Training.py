'''
2.0 Jedi Training (20pts)  Name: Tommy Ngo

UPLOAD YOUR CH 2 PDF LOG! (6pts)

1.) How do you enter a single line comment in a program? Give an example. (1pt)
You use a # symbol to comment a single line #This is a single line comment.

2.) If a=2 and b=5, predict all of the following below and record your predictions. (9pts)
Then in the Python Console window, enter a=2 and b=5 and then all of the following and record the actual output.
If the output is an error record the error and try to determine what the error is!
Comment about any of your predictions that didn't match the actual output

b/a                 = 2.5
b//a                = 3 #I forgot the floor operator rounds down (floors it)
b**a                = 25
b%a                 = 1
a+B                 = error because B is not defined
type(42)            = <class 'int'>
type(42.0)          = <class 'float'>
type("C3PO")        = <class 'str'>
type(True)          = <class 'bool'>


3.) Predict what would be the final output of (a) and type(a) if you enter the following 5 lines        (2pts)
into the Python Console Window? Then actually do it and record the output and comment on differences
between your predictions and the output.

a=2
a*=10
a/=2
a+=12
a-=7
a             = 15 #I was wrong, the answer was 15.0 because the int turned into a float when dividing
type(a)       = <class 'int'> #The answer should've been <class 'float'> because when using the divide operator, it turns the value into a float


4.) What is the mistake in the following code? Comment it and fix it!  (1pt)

x,y = (4,5)
a = 3*(x + y) # I added a multiplication operator after the 3 because Python does not recognize that a number outside paratheses are multiplying
a


5.) What is the mistake in the following code so it will calculate the average? Comment it and fix it!  (1pt)

x,y,z =(3,4,5)
ave = (x+y+z)/3 #I added paratheses surrounding the addition of the variables because otherwise it would divide z by 3 first
ave
'''