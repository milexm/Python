"""
Module echo.py 

Remarks
-------
This example shows the behavior of the <i>if __name__ == "__main__"</i> idiom.

If you execute this module as the top level code, for example by executing it directly from the command line, the idiom evaluates to true and the `main()` function is called.

If you include this module, instead, the idiom evaluates to false and the 
`main()` function is not called.

"""

def echo(text: str, repetitions: int = 3) -> str:
    """
    Imitate real-world echo.
    
    Parameters:
        text(str) : The text to echo. 
        repetitions(int) : The number of echoes. 

    Returns: 
        echoed_text(str) : The text echoed.
    """
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."


def main():
    """ 
        Executes only if this module runs as a top level code. 
        It is called when  __name__ == "__main__"
    """
    
    text = input("Yell something at a mountain: ")
    print(echo(text))

if __name__ == "__main__":
    main()
   
