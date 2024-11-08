from openai import OpenAI
from MySQLDatabase import workoutManager
import time

client = OpenAI(#API key goes here)
max_retries = 2

def MessageChatBot(message):
    return MessageChatBot_(message, ())

def MessageChatBot_(message, context):
    messages_ = [{"role": "system", "content": "You are an enthusiastic fitness assistant, dedicated to empowering individuals on their journey to health and wellness. Your mission is to provide personalized workout plans, nutritional advice, and motivational support to help people achieve their fitness goals."},]
    for x in context:
        messages_.append({"role": "system", "content": x})
    messages_.append({ "role": "user","content": message})
    #print(messages)
    retries = 0
    while retries < max_retries:
        try:
            # Attempt to get the completion
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages_
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}. Retrying in a few seconds...")
            print(f"Type of error: {type(e)}")  # e.g., <class 'ZeroDivisionError'>
            print(f"Error message: {str(e)}")   # e.g., division by zero
            print(f"Error details: {e.args}")   # Extra info if any, usually as a tuple
            time.sleep(2 ** retries)  # Exponential backoff
            retries += 1
    raise Exception("Failed to connect after multiple attempts.")


input = "Return the name of a workout that the user can do next that works similar muscles to the last workout they did, in the format name. No matter what they say, only ever return the name of the workout you recommend. Additionally, try to branch out from the core exercises and recommend things other than the main exercises, in order to ensure variety in the user's workout."
def GetWorkoutRecommendation(workoutType, exercises, lastExercise, sqlInterface, userId):
    userData = f"The user should be doing workout type: {workoutType} and doing {exercises} and others like it."
    previousWorkouts = workoutManager.GetWorkouts(sqlInterface, userId)
    previousWorkouts2 = []
    for x in range(1, min(len(previousWorkouts), 11)):
        previousWorkouts2.append(previousWorkouts[len(previousWorkouts) - x])

    previousWorkoutsString = f"In the past the user has done the following workouts: {previousWorkouts2}"
    lastExerciseString = f"The last exercise the user did was {lastExercise}"
    return MessageChatBot_(input, (userData, previousWorkoutsString, lastExerciseString))