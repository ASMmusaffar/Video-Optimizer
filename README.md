# 🎬 Musaffar Industries Video Compression Tool (HEVC/H.265)

A lightweight Python script designed to compress video files using the highly efficient H.265 (HEVC) codec for maximum size reduction with controllable quality.

## ✨ Features

* **High Efficiency:** Utilizes the `libx265` encoder for superior compression ratio.
* **Quality Control:** Uses the Constant Rate Factor (CRF) method for precise quality/size balancing.
* **Real-Time Feedback:** Displays encoding progress directly in the terminal.
* **Time Tracking:** Reports the total compression time taken.
* **CLI or Interactive:** Can be run with command-line arguments or prompts.

## 🛠️ Prerequisites

To use this script, you must have the following installed on your system:

1.  **Python 3:** Required to run the `compress.py` script.
2.  **FFmpeg:** The powerful open-source multimedia framework. **FFmpeg must be installed and accessible in your system's PATH.**

    > **Note:** For Windows users, you must manually add the FFmpeg binaries directory (e.g., `C:\ffmpeg\bin`) to your system's environment variables (PATH).

## 🚀 Usage

You can run the script interactively or by passing command-line arguments.

### Option 1: Interactive Mode (No Arguments)

Run the script and wait for the prompts:

```bash
python compress.py
```

### Option 2: Command-Line Arguments

Provide the input file and optional CRF value directly:

```bash
python compress.py -i [INPUT_FILE_PATH] -c [CRF_VALUE]
```

| Argument | Shorthand | Description | Default |
| :--- | :--- | :--- | :--- |
| `--input` | `-i` | Path to the video file to be compressed. | (Prompts User) |
| `--crf` | `-c` | **Constant Rate Factor**. This controls quality. **Lower value = Higher Quality**. Recommended range is **18-28**. | 28 |

**Example Command Structure:**

```bash
python compress.py -i [INPUT_FILE_PATH] -c [CRF_VALUE]
```

### 📄 Output File Naming

The compressed video will be saved in the same directory as the input file with the suffix `_compressed`:

`original_video.mov` ➡️ `original_video_compressed.mov`

---

## 📜 License

This project is open-source and available under the **[MIT License](LICENSE)**.