import cv2
import glob
import os
from tqdm import tqdm

# move to directory with videos
CWD = '/mnt/noaa_poc2/NOAA-POC/inference/'
os.chdir(CWD)
VIDS = sorted([vid for vid in glob.glob('*.MP4')])

# create directories to hold extraced frames
for vid in VIDS:
    name = vid[:-4]
    directory = name + '_FRAMES'
    os.mkdir(directory) if not os.path.exists(directory) else None

FRAMES = sorted([fol for fol in glob.glob('*_FRAMES')])

INTERVAL = 1 # extracts every 10th frame

# extract
for video, folder in zip(VIDS, FRAMES):
    if not os.listdir(folder):  # Check if the directory is empty
        print(f'Extracting frames from {video}')
        video = cv2.VideoCapture(video)
        curr_frame = 0
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # Get total frame count
        progress_bar = tqdm(total=total_frames, unit='frame', desc='Progress')  # Create tqdm progress bar
        
        while True:
            success, frame = video.read()
            if success:
                if curr_frame % INTERVAL == 0:
                    cv2.imwrite(f'{CWD}{folder}/frame_{curr_frame}.jpg', frame)
                curr_frame += 1
                progress_bar.update(1)  # Update progress bar
                continue
            else:
                break
        
        progress_bar.close()
