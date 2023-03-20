import os
import json
import openai

class ChatGPTHandler:
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def get_text_from_input(self, user_query, action='continue'):
        prompts = self.__fetch_prompts(user_query, action)
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompts,
            n = 1,
            max_tokens = 512
        )
        
        return self.__prepare_output(response)

    def __fetch_prompts(self, user_query, action):
        conv_list = json.load(open(f'prompts/{action}.json', 'r'))
        conv_list.append({"role": "user", "content": user_query})
        return conv_list

    def __prepare_output(self, response):
        return response['choices'][0]['message']['content']