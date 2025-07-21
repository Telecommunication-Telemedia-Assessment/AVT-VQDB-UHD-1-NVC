import argparse
import subprocess
import platform
from pathlib import Path

def get_ffmpeg_command():
    if platform.system() == 'Windows':
        return 'ffmpeg.exe'
    return 'ffmpeg'

def upscale_video(input_file, output_file, codec, overwrite, ffmpeg_cmd):
    if output_file.exists() and not overwrite:
        print(f"Skipping (already exists): {output_file}")
        return

    scale_filter = 'scale=3840x2160:param0=5'
    sws_flags = 'lanczos+accurate_rnd+bitexact'
    overwrite_flag = ['-y'] if overwrite else []

    if codec.lower() == 'ffvhuff':
        cmd = [
            ffmpeg_cmd, *overwrite_flag,
            '-i', str(input_file),
            '-c:v', 'ffvhuff',
            '-vf', scale_filter,
            '-sws_flags', sws_flags,
            str(output_file)
        ]
    elif codec.lower() == 'h265':
        cmd = [
            ffmpeg_cmd, *overwrite_flag,
            '-i', str(input_file),
            '-c:v', 'libx265',
            '-x265-params', 'lossless=1',
            '-vf', scale_filter,
            '-sws_flags', sws_flags,
            str(output_file)
        ]
    else:
        raise ValueError("Unsupported codec. Use 'ffvhuff' or 'x265'.")

    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("Error: FFmpeg not found. Ensure it's installed and in your system PATH.")

def main():
    parser = argparse.ArgumentParser(description="Upscale MKV videos to 4K using FFmpeg.")
    parser.add_argument('--input_dir', '-i', type=Path, required=True, help='Input directory containing MKV files.')
    parser.add_argument('--output_dir', '-o', type=Path, required=True, help='Output directory for upscaled MKV files.')
    parser.add_argument('--overwrite', action='store_true', default=False, help='Overwrite output files if they already exist (default: False).')
    parser.add_argument('--codec', choices=['ffvhuff', 'h265'], default='ffvhuff', help='Lossless codec to use for encoding (default: ffvhuff).')

    args = parser.parse_args()

    ffmpeg_cmd = get_ffmpeg_command()

    input_dir = args.input_dir
    output_dir = args.output_dir
    if not input_dir.exists():
        print(f"Input directory does not exist: {input_dir}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    for input_file in sorted(input_dir.glob('*.mkv')):
        if input_file.name.startswith('.'):
            continue  # skip hidden
        
        output_file = output_dir / input_file.name.replace('.decoded.mkv', '.mkv')
        upscale_video(input_file, output_file, args.codec, args.overwrite, ffmpeg_cmd)

if __name__ == '__main__':
    main()