import cv2
import glob
import os
from tqdm import tqdm
import warnings
import sys
import argparse

def extract_frames(
	video_path: str,
	output_dir: str,
	interval: int
):
    print(f"Processing: {video_path}")
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) 
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        warnings.warn(f"Directory {output_dir} already exists.")
    
    frame_count = 0
    extracted_count = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    with tqdm(total=total_frames, desc=os.path.basename(video_path), unit='frames') as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                break
            
            if frame_count % interval == 0:
                frame_filename = os.path.join(output_dir, f'frame_{extracted_count:04d}.jpg')
                cv2.imwrite(frame_filename, frame)
                extracted_count += 1
            
            frame_count += 1
            pbar.update(1)
    
    cap.release()

def main(input_path, interval):
    if os.path.isdir(input_path):
        # Input path is a directory
        video_files = [f for f in os.listdir(input_path) if f.endswith('.mp4')]
        print("Files found:")
        for f in video_files:
            print(f)
        for video_file in video_files:
            video_path = os.path.join(input_path, video_file)
            output_dir = os.path.join(input_path, video_file.replace('.mp4', '_FRAMES'))
            
            extract_frames(video_path, output_dir, interval)
    
    elif os.path.isfile(input_path) and input_path.endswith('.mp4'):
        # Input path is a single .mp4 file
        video_path = input_path
        output_dir = os.path.splitext(video_path)[0] + '_FRAMES'
        
        extract_frames(video_path, output_dir, interval)
    
    else:
        print(f"Error: {input_path} is not a valid directory or .mp4 file.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_frames.py <input_dir> <interval>")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Extract frames from .mp4 files at a given interval.')
    parser.add_argument('input_dir', type=str, help='Path to the directory holding .mp4 files')
    parser.add_argument('interval', type=int, help='Extraction interval in seconds')
    
    args = parser.parse_args()
    
    main(args.input_dir, args.interval)

