import time
import winsound
import numpy as np
from PIL import Image
from datetime import datetime

img_path = input("Select image (path, only '/' slashes): ")
img = Image.open(img_path)

data = np.asarray(img)

max_freq = 15000
min_freq = 50
step_freq = (max_freq + min_freq) // 256



print(f"Step: {step_freq}")

start_time = time.time()
print(f"Start time: {datetime.now()}")
for row in data:
    for pixel in row:
        total = 0
        for channel in pixel:
            # total += channel  # Sum all 3 channel values to gget average
            channel_freq = int(channel * step_freq)
            winsound.Beep(channel_freq, 50)
        # average = total / 3  # Find average
        # channel_freq = int(average * step_freq)  # Get the equivalent frequency
        # winsound.Beep(channel_freq, 50)  # Just beep

end_time = time.time() - start_time
print(f"End time: {datetime.now()}")
print(f"Elapsed time: {end_time}")