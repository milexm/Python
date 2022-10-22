"""
It shows the behavior of the if __name__ == "__main__" idiom.


1) If you execute this module as the top level code the idiom evaluates to true and the indented code is executed.
2) If you include this module, instead, the idiom evaluates to false and the indented code is not executed.

Functions:

echo 


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
