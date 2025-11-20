import subprocess
import os
import time
import argparse

# --- Main compression function (unchanged core logic) ---

def compress_video(input_path, output_path, crf):
    """
    Compresses a video file using the H.265 (HEVC) codec with real-time FFmpeg output.
    """
    
    # --- Check for FFmpeg ---
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("🚨 Error: FFmpeg not found. Please install it and ensure it's in your system PATH.")
        return

    # --- Start Timer ---
    start_time = time.time()
    
    # --- Define FFmpeg Command ---
    command = [
        'ffmpeg',
        '-y', 
        '-i', input_path,
        '-c:v', 'libx265',
        '-crf', str(crf),
        '-c:a', 'aac',
        '-b:a', '128k',
        '-preset', 'medium', 
        '-loglevel', 'info', 
        output_path
    ]

    print(f"\n🎬 Starting compression for: {input_path}")
    print(f"   Output file: {output_path}")
    print(f"   CRF value: {crf} (Lower = higher quality/larger size)")
    print("---------------------------------------------------------")

    # --- Execute Command with Real-Time Output ---
    try:
        process = subprocess.Popen(command, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.STDOUT, 
                                   text=True)
        
        print("--- Real-time Progress ---")
        for line in process.stdout:
            print(f"   {line.strip()}")
            
        process.wait()
        
        # --- End Timer and Calculate Elapsed Time -----
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        if process.returncode == 0:
            print("\n✅ Compression completed successfully!")
            print(f"**Total time taken: {elapsed_time:.2f} seconds**")
            
            # Get and print file sizes
            if os.path.exists(input_path) and os.path.exists(output_path):
                original_size = os.path.getsize(input_path) / (1024*1024)
                compressed_size = os.path.getsize(output_path) / (1024*1024)
                print(f"Original size: **{original_size:.2f} MB**")
                print(f"Compressed size: **{compressed_size:.2f} MB**")
            else:
                 print("File sizes unavailable.")
        else:
            print(f"\n❌ Compression failed with return code **{process.returncode}**")

    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# ----------------------------------------------------------------------
# --- Main Execution Function ---

def main():
    parser = argparse.ArgumentParser(
        description="MUSAFFAR INDUSTRIES Video Compressor (HEVC/H.265).",
        epilog="If INPUT_FILE is omitted, the script will prompt the user."
    )
    
    # Optional arguments for command-line use
    parser.add_argument(
        '-i', '--input', 
        type=str, 
        help='Path to the input video file.'
    )
    parser.add_argument(
        '-c', '--crf', 
        type=int, 
        default=28, 
        help='Constant Rate Factor (CRF). Lower value = higher quality (18-28 recommended). Default is 28.'
    )
    
    args = parser.parse_args()

    COMPANY_NAME = "MUSAFFAR INDUSTRIES"
    
    print(f"\n*** WELCOME to {COMPANY_NAME} Video Compression Utility ***")
    print("---------------------------------------------------------")

    # 1. Get input file name (either from argument or prompt)
    if args.input:
        input_file_name = args.input
    else:
        # Prompt user if no argument was provided
        input_file_name = input("▶️ Enter the video file name (e.g., my_video.mp4) or full path: ")

    # 2. Check file existence
    if not os.path.exists(input_file_name):
        print(f"\n⚠️ Error: File not found at '{input_file_name}'.")
        return

    # 3. Generate the output file name
    base_name, ext = os.path.splitext(input_file_name)
    output_file_name = f"{base_name}_compressed{ext}"
    
    # 4. Run the compression
    compress_video(input_file_name, output_file_name, crf=args.crf)

# --- Standard Python Entry Point ---
if __name__ == "__main__":
    main()