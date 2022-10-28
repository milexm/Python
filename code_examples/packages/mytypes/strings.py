""" 
Shows how to use string.
""" 

class mystring:

    def useString(self):
        astring = "\"Hello World!\""
        message = '{0} {1}'.format('This is a string: ', astring)
        print(message)
        
    def subString(self):
        astring = "\"Hello World!\""
        message = '{0} {1}'.format('This is a substring: ', astring[2:10])
        print(message)

    def stripWhiteSpaces(self):
        astring = "\"  Hello World!  \""
        message = '{0} {1}'.format('This is a string without white spaces: ', 
                astring.strip(' '))
        print(message)
        
    def lowerString(self):
        astring = "\"Hello World!\""
        message = '{0} {1}'.format('Lower case string: ', astring.lower())
        print(message)
        
    def upperString(self):
        astring = "\"Hello World!\""
        message = '{0} {1}'.format('Upper case string: ', astring.upper())
        print(message)
        
    def splitString(self):
        astring = "\"Hello, World!\""
        message = '{0} {1}'.format('Split string: ', astring.split(','))
        print(message)    