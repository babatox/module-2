from groq import generate_response
def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    vague = input("Enter a vague prompt: ")
    print("\nAI's response to vague prompt:")
    print(generate_response(vague))
    specific = input("\nNow, make it more specific: ")
    print("\nAI's response to specific prompt:")
    print(generate_response(specific))
