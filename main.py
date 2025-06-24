from utils import read_video, save_video
from trackers import Tracker

def main():
    # Read video
    video_frames = read_video('input/08fd33_4.mp4')
    if not video_frames:
        print("No frames read from the video.")
        return

    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stub.pkl')

    # Draw output
    ## Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save video
    save_video(output_video_frames, 'output/output_video.avi')

if __name__ == '__main__':
    main()