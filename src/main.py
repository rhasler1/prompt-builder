from dotenv import load_dotenv
import os
import argparse
from agent import LLMAgent

load_dotenv()
USER_PREFIX = os.getenv("USER_PREFIX")

def parse_cmdline_args():
    parser = argparse.ArgumentParser(description="Prompt-Builder")
    
    parser.add_argument("--model", type=str, default="gemma3", help="This is the model to be used.")
    parser.add_argument("--system", type=str, default="You are a mathematician", help="Who you want the llm to be.")
    parser.add_argument("--instruction", type=str, default="Find the square root.", help="This is what you want the llm to do.")
    parser.add_argument("--context", type=str, default="4", help="This is what the instruction will be applied to.")

    args = parser.parse_args()
    return args

def read_file(path):
    with open(path, "r") as file:
        content = file.read()
    return content

def main():
    args = parse_cmdline_args()
    system = args.system
    model = args.model
    instruction = args.instruction
    context = args.context

    # overwriting defaults
    instruction = read_file(f"{USER_PREFIX}/files/instruction.txt")
    context = read_file(f"{USER_PREFIX}/files/context.txt")

    agent = LLMAgent(model)
    agent.add_to_memory(role="System", content=system)
    agent.add_to_memory(role="User", content=instruction)
    agent.add_to_memory(role="User", content=context)

    agent.generate_response()
    msg = agent.get_last_msg()

    print(f"Message:\n{msg}")

if __name__ == "__main__":
    main()
