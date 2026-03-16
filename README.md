# RemBG-Utility-Tool
**RemBG Batch Background Remover** is a lightweight desktop utility that automatically removes backgrounds from **images or entire folders of images** using AI. Built with **Python**, **rembg**, and **Tkinter**, it provides a simple workflow for quickly generating transparent PNG images with backgrounds removed.

The tool supports **drag-and-drop files or folders**, folder selection dialogs, and automatic batch processing.

---

## Key Features

- **AI Background Removal** – Uses the `rembg` library to automatically remove backgrounds from images.
- **Batch Processing** – Process an entire folder of images in one run.
- **Single Image Support** – Drag-and-drop or select individual images for background removal.
- **Automatic Output Folder** – Processed images are saved to a generated `RemBG'dImgs` folder.
- **Transparent PNG Output** – All processed images are exported as PNG files with transparency.
- **Drag-and-Drop Support** – Drop files or folders directly onto the executable.
- **Automatic File Detection** – Detects whether a file or folder was provided.
- **Console Progress Output** – Displays processing status for each image.
- **Error Handling** – Failed files are reported without stopping the batch process.

---

## Supported Image Formats

- `png`
- `jpg`
- `jpeg`
- `webp`

All processed files are exported as **PNG images with transparent backgrounds**.

---

## Built With

- **Python**
- **rembg** – AI-powered background removal
- **Pillow (PIL)** – Image handling
- **Tkinter** – File/folder selection dialog
- **ONNX Runtime** – Model inference used internally by rembg

---

## Usage

1. Launch the executable.
2. Choose one of the following methods:

**Option 1 – Drag and Drop**
- Drag a **file** or **folder** onto the executable.

**Option 2 – Folder Selection**
- Run the program normally.
- Select a folder when the file dialog appears.

3. The program processes all supported images.
4. Results are saved in a folder named:

`RemBG'dImgs`

inside the selected directory.

---

## Output Structure

Example:


---

## Notes

- Supports both **single-image processing** and **full folder batch processing**.
- Output files always use **PNG format** to preserve transparency.
- The executable and the original Python source code are available in the repository and the **Releases** tab.

---

## License

This project is open source under the **MIT License**.
