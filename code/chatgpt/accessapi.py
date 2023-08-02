""" 
Module accessapi.py
"""

import openai

def simple_question():
    """
        Aask a simple question to ChatGPT. 

        Remarks
        -------
        This simple function tests the enviroment settings to 
        determine if the infrastructure is in place to communicate
        with ChatGPT via the OpenAI API.  
     """


    secret_key = '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'
    openai.api_key = secret_key

    # Simple prompt or question to ask. 
    my_prompt = 'Tell me a short ad for a homme security company'


    output = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = my_prompt,
        max_tokens = 200,
        temperature = 0
    )

    print(output)


if __name__ == '__main__':
    # Ask simple question.
    simple_question()

