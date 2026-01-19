# Video Transcriber

A simple Python script to transcribe MP4 video files to text using OpenAI's Whisper model.

## Features

- Transcribe MP4 video files to text
- Multiple model sizes for accuracy/speed tradeoffs
- Automatic output file naming
- Preview of transcription results

## Requirements

- Python 3.10+
- FFmpeg
- openai-whisper

## Installation

### 1. Install FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

### 2. Install Python Dependencies

```bash
pip install openai-whisper
```

Or using a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install openai-whisper
```

## Usage

### Basic Usage

```bash
python transcribe_video.py video.mp4
```

This will create `video.txt` in the same directory as the video.

### Specify Output File

```bash
python transcribe_video.py video.mp4 transcript.txt
```

### Choose Model Size

```bash
python transcribe_video.py -m medium video.mp4
```

## Model Options

| Model | Size | Speed | Accuracy | Use Case |
|-------|------|-------|----------|----------|
| `tiny` | 39M | Fastest | Lower | Quick drafts, testing |
| `base` | 74M | Fast | Good | Default, general use |
| `small` | 244M | Medium | Better | Improved accuracy |
| `medium` | 769M | Slow | High | Professional use |
| `large` | 1550M | Slowest | Highest | Maximum accuracy |

**Note:** Larger models require more RAM and processing time but produce more accurate transcriptions.

## Examples

```bash
# Transcribe with default settings (base model)
python transcribe_video.py meeting_recording.mp4

# Transcribe with high accuracy
python transcribe_video.py -m large lecture.mp4 lecture_transcript.txt

# Quick transcription for testing
python transcribe_video.py -m tiny test_video.mp4
```

## Output

The script outputs:
1. A text file containing the full transcription
2. A preview of the first 500 characters in the terminal

## Limitations

- Designed for MP4 files (other formats may work but are not officially supported)
- Requires significant processing time for long videos
- Large models require substantial RAM (8GB+ recommended for medium/large)

## License

MIT License

## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - The underlying speech recognition model
