import os
import json

# Function to log the maze environment information and parameters in JSON 
def log_environment_details(env, args, file_path, file_name):
    env_details = {
        "Environment Name": env.env_name,
        "Scaling Factor": env.base_env.MAZE_SIZE_SCALING,
        "Maze Structure": env.base_env.MAZE_STRUCTURE,
        "Arguments": vars(args)  
    }
    full_path = os.path.join(file_path, file_name + ".json")
    with open(full_path, "w") as file:
        json.dump(env_details, file, indent=4)  
