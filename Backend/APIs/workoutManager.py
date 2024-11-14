# workoutManager.py
class WorkoutManager:
    @staticmethod
    def add_workout(data):
        # Simulate adding a workout recommendation
        # Here, you would typically save this to a database or generate a workout recommendation
        workout = {
            "id": 1,
            "name": data.get("name", "General Workout"),
            "type": data.get("type", "Cardio"),
            "duration": data.get("duration", 30),
            "notes": data.get("notes", "Recommended workout based on fitness level.")
        }
        return {"status": "Workout added", "workout": workout}

    @staticmethod
    def get_all_workouts():
        # Simulate retrieving workouts
        workouts = [
            {"id": 1, "name": "Cardio Blast", "type": "Cardio", "duration": 30},
            {"id": 2, "name": "Strength Training", "type": "Strength", "duration": 45}
        ]
        return workouts
