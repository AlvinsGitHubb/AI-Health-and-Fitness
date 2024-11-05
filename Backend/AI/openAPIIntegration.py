from openai import OpenAI
client = OpenAI(api_key="")


def MessageChatBot(message):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an enthusiastic fitness assistant, dedicated to empowering individuals on their journey to health and wellness. Your mission is to provide personalized workout plans, nutritional advice, and motivational support to help people achieve their fitness goals."},#This is the system talking to the chat bot and telling it its role
            {
                "role": "user",
                "content": message
            }#This is the user's message to the chat bot, which it will repond to
        ]
    )

    return completion.choices[0].message

def GetWorkoutRecommendation(workoutType, exercises):
    input = f"Create a workout plan for the user with workout type: {workoutType} and including {exercises} and others like it."
    return MessageChatBot(input)