import pandas as pd
import matplotlib.pyplot as plt
import os

# Folder containing the CSV files
folder_path = 'Transfer/AntMaze/AntMaze-2/Transfer/STAR/Results'
output_folder_path = 'Transfer/AntMaze/AntMaze-2/Transfer/STAR/Plots'  # Folder where plots will be saved

# Create output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        # Load the CSV file
        df = pd.read_csv(file_path, usecols=['frames', 'reward'])

        # Calculate moving averages
        #df['MA3'] = df['reward'].rolling(window=3).mean()
        df['MA10'] = df['reward'].rolling(window=10).mean()

        # Plotting
        plt.figure(figsize=(14, 7))
        plt.plot(df['frames'], df['reward'], label='Reward', alpha=0.25)
        #plt.plot(df['frames'], df['MA3'], label='Moving Average (3)', linewidth=2)
        plt.plot(df['frames'], df['MA10'], label='Moving Average (10)', linewidth=2)
        plt.title(f'Reward and Moving Averages (10) for {filename}')
        plt.xlabel('Frames')
        plt.ylabel('Reward')
        plt.legend()
        
        # Save plot to the output folder
        output_file_path = os.path.join(output_folder_path, f'{filename[:-4]}_plot.png')
        plt.savefig(output_file_path)
        plt.close()  # Close the plot window
