import os
import openai

class ChatGPTHandler:
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def get_text_from_input(self, prompt, action='continue'):
        if action == 'summarize':
            return self.__summarize(prompt)
        elif action == 'simplify':
            return self.__simplify(prompt)
        elif action == 'continue':
            return self.__continue(prompt)
        elif action == 'proxy_write':
            return self.__proxy_write(prompt)
        elif action == 'rewrite':
            return self.__rewrite(prompt)
        elif action == 'correction':
            return self.__correction(prompt)

    def __summarize(self, prompt):
        pass

    def __simplify(self, prompt):
        pass

    def __continue(self, prompt):
        pass

    def __proxy_write(self, prompt):
        pass

    def __rewrite(self, prompt):
        pass

    def __correction(self, prompt):
        pass

    def __prepare_output(self, respon):
        pass