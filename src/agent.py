from ollama import Client
from pydantic import BaseModel

class LLMAgent:
    def __init__(self, model):
        if not model:
            raise ValueError("A model must be specified when creating a LLM Agent")
        self.model = model
        self.memory = []
        self.client = Client(host="http://localhost:11434")

    def add_to_memory(self, role, content):
        self.memory.append({"role": role, "content": content})

    def generate_response(self):
        try:
            response = self.client.chat(
                    model=self.model,
                    messages=self.memory,
                    stream=False,
                    )
                     
        except Exception as e:
            print(f"Error when generating response {e}")
            return -1

        content = response["message"]["content"]
        #print(f"At generate_response content={content}")
        self.add_to_memory("assistant", content)
        return 1

    def get_last_msg(self):
        if self.memory:
            return self.memory[-1]
        return None

    #def format_memmory(self):
    #formatted = []
    #for entry in self.memmory:
    #    role = entry["role"]
    #    content = entry["content"]
    #    formatted.append(f"{role}:\n{content}\n{'-'*40}\n")
    #return "".join(formatted)
