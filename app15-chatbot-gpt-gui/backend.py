import openai


class ChatBot:
    def __int__(self):
        openai.api_key = " "

    def generate_response(self, user_input):
        response = (
            openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=3000,
                temperature=0.5,
            )
            .choices[0]
            .text()
        )
        return response
