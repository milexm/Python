"""
It evaluates the value and the type of the global variable __name__ and executes the relevant code. 

The following behavior is supported:

1) If you execute this module as the top level code the idiom __name__ == "__main__" evaluates to true and the indented code is executed.
2) If you include this module, instead, the idiom evaluates to false and the indented code is not executed.
"""

# Display the value and the type of the global variable `__nama__`
print(__name__, type(__name__))

if __name__ == "__main__":
    # Executes only if this module runs as a top level code.  
    print("namamain.py is running as top leval code.")
