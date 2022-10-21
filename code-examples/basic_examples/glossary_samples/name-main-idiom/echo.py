"""
File name: echp.py.
It shows the behavior of the if __name__ == "__main__" idiom and executes the relevant code. 
1) If you execute this module as the top level code the idiom evaluates to true and the indented code is executed, as in this example:
> python echo.py
> Yell something at a mountain: hello world
rld
ld
d
.
2) If you include this module, instead, the idiom evaluates to false and the indented code is not executed, as in this example:
> python
>>> from echo import echo
>>> echo("not top level code")            
'ode\nde\ne\n.'
"""


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."


if __name__ == "__main__":
    # Executes only if this module runs as a top level code.  
    text = input("Yell something at a mountain: ")
    print(echo(text))
