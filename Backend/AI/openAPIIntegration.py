import openai
import time

max_retries = 2

def MessageChatBot(message):
    MessageChatBot_(message, ())

def MessageChatBot_(message, context):
    messages_ = [{"role": "system", "content": "You are an enthusiastic fitness assistant, dedicated to empowering individuals on their journey to health and wellness. Your mission is to provide personalized workout plans, nutritional advice, and motivational support to help people achieve their fitness goals."},]
    for x in context:
        messages_.append({"role": "system", "content": context})
    messages_.append({ "role": "user","content": message})
    #print(messages)
    retries = 0
    while retries < max_retries:
        try:
            # Attempt to get the completion
            completion = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=messages_
            )
            return completion
        except openai.error.APIConnectionError as e:
            print(f"Connection error: {e}. Retrying in a few seconds...")
            time.sleep(2 ** retries)  # Exponential backoff
            retries += 1
    raise Exception("Failed to connect after multiple attempts.")

    return completion.choices[0].message.content

def GetWorkoutRecommendation(workoutType, exercises):
    input = f"Create a workout plan for the user with workout type: {workoutType} and including {exercises} and others like it."
    return MessageChatBot(input)