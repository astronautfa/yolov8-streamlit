from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
RTSP = 'RTSP'
YOUTUBE = 'YouTube'

SOURCES_LIST = [VIDEO, WEBCAM, RTSP, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'office_4.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'office_4_detected.jpg'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'video_1': VIDEO_DIR / 'video1.mp4',
    'video_2': VIDEO_DIR / 'video2.mp4',
    'video_3': VIDEO_DIR / 'video3.mp4',
    'video_4': VIDEO_DIR / 'video4.mp4',
    'video_5': VIDEO_DIR / 'video5.mp4',
    'video_6': VIDEO_DIR / 'video6.mp4',
    'video_7': VIDEO_DIR / 'video7.mp4',
    'video_8': VIDEO_DIR / 'video8.mp4',
    'video_9': VIDEO_DIR / 'video9.mp4',
    'video_10': VIDEO_DIR / 'video10.mp4',
    'video_11': VIDEO_DIR / 'video11.mp4',
    'video_12': VIDEO_DIR / 'video12.mp4',
    'video_13': VIDEO_DIR / 'video13.mp4',
    'video_14': VIDEO_DIR / 'video14.mp4',
    'video_15': VIDEO_DIR / 'video15.mp4',
    'video_16': VIDEO_DIR / 'video16.mp4',
    'video_17': VIDEO_DIR / 'video17.mp4',
    'video_18': VIDEO_DIR / 'video18.mp4',
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolov8m.pt'
# In case of your custome model comment out the line above and
# Place your custom model pt file name at the line below 
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'

SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'

# Webcam
WEBCAM_PATH = 0
