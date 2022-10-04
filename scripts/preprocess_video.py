"""Preprocess video"""

import argparse
import os
import cv2

def main(video_path, output_path, n):
    """Preprocess video"""
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_rate = cap.get(cv2.CAP_PROP_FPS)

    os.makedirs(output_path, exist_ok=True)

    frame_count = 0
    frame_index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % int(frame_rate * n) == 0:
            cv2.imwrite(os.path.join(output_path, f"{frame_index:04d}.jpg"), frame)
            frame_index += 1
        frame_count += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", type=str, default="data/cawang.mp4")
    parser.add_argument("--output_path", type=str, default="data/images")
    parser.add_argument("--n", type=int, default=1)
    args = parser.parse_args()

    main(args.video_path, args.output_path, args.n)