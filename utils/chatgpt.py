import os
import json
import openai

class ChatGPTHandler:
    def __init__(self) -> None:
        openai.api_key = "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"
    
    def get_text_from_input(self, user_query, action='continue'):
        prompts = self.__fetch_prompts(user_query, action)
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompts,
            n = 1,
            max_tokens = 512
        )
        
        return self.__prepare_output(user_query, response, action="continue")

    def __fetch_prompts(self, user_query, action):
        conv_list = json.load(open(f'utils/prompts/{action}.json', 'r'))
        conv_list.append({"role": "user", "content": user_query})
        return conv_list

    def __prepare_output(self, user_query, response, action):
        if action == 'continue':
            return user_query.strip() + " " + response['choices'][0]['message']['content']
        return response['choices'][0]['message']['content']