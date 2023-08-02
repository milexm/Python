
import openai

def simple_question():

    secret_key = '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'
    openai.api_key = secret_key

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

