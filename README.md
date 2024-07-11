# Fish Detector Tools

This is where I can place any refactored tools for ease of use.

1. [First Steps](#first-steps)
2. [Frame Extractor](#frame-extractor)
3. [Notes & Help](#notes--help)

## First steps

1. Clone this repsoitory (use one of the following commands)

```
git clone https://github.com/wj-jason/fish-detector.git
git clone git@github.com:wj-jason/fish-detector.git
```
2. Move into the repository
```
cd fish-detector
```

In order to use any of these tools, your current working directory (can be checked with either `pwd` or `cwd` based on your os) must be this repository. That is, running either `pwd` or `cwd` should return something along the lines of:
```
<OTHER_FILES>/fish-detector
```
## Frame Extractor

The frame extractor can either be run by specifying a certain `.mp4` file, or by specifying a directory containing multiple `.mp4` files.

To use the tool, run:
```
python3 -m utils.extract <ABSOLUTE_PATH> <FRAME_INTERVAL>
```
Note that you may have to run `python` instead of `python3` depending on your system.

For example, to extract the frames of only 1 file located in `/home/jason/videos/random_video.mp4`, taking every 10th frame:
```
python3 -m utils.extract /home/jason/videos/random_video.mp4 10
```
or to extract the frames from all the videos in the directory:
```
python3 -m utils.extract /home/jason/videos/ 10
```
Once extracted, you may view the contents of the file in `/home/jason/videos/random_video_FRAMES/`.

## Notes & Help

You may have to install some dependencies based on your system. If this is the case, the script will fail the first time you run it, specifying which dependencies are required. I have tried my best to ensure the dependencies work on most python versions, however please contact me (Jason) if any issues cannot be resolved.


