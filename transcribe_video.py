#!/usr/bin/env python3
"""
Transcribe an MP4 video file to text using OpenAI's Whisper model.

Usage:
    python transcribe_video.py <video_file.mp4> [output_file.txt]

Requirements:
    pip install openai-whisper

    FFmpeg must be installed:
    - macOS: brew install ffmpeg
    - Ubuntu: sudo apt install ffmpeg
"""

import argparse
import sys
from pathlib import Path

try:
    import whisper
except ImportError:
    print("Error: openai-whisper not installed.")
    print("Install with: pip install openai-whisper")
    sys.exit(1)


def transcribe_video(video_path: str, output_path: str | None = None, model_name: str = "base") -> str:
    """
    Transcribe a video file to text.

    Args:
        video_path: Path to the MP4 video file
        output_path: Optional path for the output text file
        model_name: Whisper model to use (tiny, base, small, medium, large)

    Returns:
        The transcribed text
    """
    video_file = Path(video_path)

    if not video_file.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    if not video_file.suffix.lower() == ".mp4":
        print(f"Warning: File extension is {video_file.suffix}, expected .mp4")

    print(f"Loading Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)

    print(f"Transcribing {video_file.name}...")
    result = model.transcribe(str(video_file))

    transcription = result["text"].strip()

    # Determine output path
    if output_path is None:
        output_path = video_file.with_suffix(".txt")
    else:
        output_path = Path(output_path)

    # Write transcription to file
    output_path.write_text(transcription, encoding="utf-8")
    print(f"Transcription saved to: {output_path}")

    return transcription


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe an MP4 video file to text using Whisper"
    )
    parser.add_argument("video", help="Path to the MP4 video file")
    parser.add_argument("output", nargs="?", help="Output text file path (optional)")
    parser.add_argument(
        "-m", "--model",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size (default: base). Larger models are more accurate but slower."
    )

    args = parser.parse_args()

    try:
        transcription = transcribe_video(args.video, args.output, args.model)
        print("\n--- Transcription Preview ---")
        preview = transcription[:500] + "..." if len(transcription) > 500 else transcription
        print(preview)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error during transcription: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()