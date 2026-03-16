# Import required modules
import os                     # Used for filesystem operations (paths, directories, etc.)
import sys                    # Used to read command-line arguments (for drag-and-drop support)
from rembg import remove     # Core AI background removal function
from PIL import Image        # Pillow image library (not directly used here but included for compatibility)
from tkinter import filedialog, Tk   # Used to open a folder selection dialog

# Toggle variable used to determine if the program is processing
# an entire folder or just a single file
togglevar = True


def rembg_folder(input_folder, togglevar):
    """
    Processes either a folder of images OR a single image file
    and removes the background from each image using rembg.

    Parameters
    ----------
    input_folder : str
        Path to the input folder OR image file.

    togglevar : bool
        True  = process entire folder
        False = process single file
    """

    try:
        # Clear the console for cleaner output (Windows)
        os.system('cls')

        # Display the folder currently being processed
        print(f"Processing folder: {input_folder}")

        # Supported image formats that rembg can process
        supported_exts = ('.png', '.jpg', '.jpeg', '.webp')

        def iterate(filename):
            """
            Processes a single image file and removes the background.
            """

            try:
                # Determine the correct input and output paths
                if togglevar == True:
                    # Processing a folder
                    input_path = os.path.join(input_folder, filename)

                    # Output will always be a PNG with transparency
                    output_path = os.path.join(
                        output_folder,
                        os.path.splitext(filename)[0] + '.png'
                    )

                else:
                    # Processing a single file
                    input_path = input_folder

                    output_path = os.path.join(
                        output_folder,
                        os.path.splitext(os.path.basename(filename))[0] + '.png'
                    )

                # Open the image file in binary mode
                # This allows the raw image bytes to be passed to rembg
                with open(input_path, 'rb') as i:
                    input_data = i.read()

                    # Perform AI background removal
                    output_data = remove(input_data)

                # Write the processed image to disk
                with open(output_path, 'wb') as o:
                    o.write(output_data)

                # Clear console and show progress
                os.system('cls')
                print(f"Processed: {filename}")

            except Exception as e:
                # Catch any error during processing of a single file
                os.system('cls')
                print(f"Failed to process {filename}: {e}")

        # If togglevar is True we are processing an entire folder
        if togglevar == True:

            try:
                # Create output folder inside the input directory
                output_folder = os.path.join(input_folder, "RemBG'dImgs")

                # exist_ok=True prevents errors if folder already exists
                os.makedirs(output_folder, exist_ok=True)

            except Exception as e:
                print(f"Error creating output folder: {e}")
                return

            try:
                # Collect all supported image files from the directory
                files = [
                    f for f in os.listdir(input_folder)
                    if f.lower().endswith(supported_exts)
                ]
            except Exception as e:
                print(f"Error reading directory contents: {e}")
                return

            # Process each file found
            for filename in files:
                iterate(filename)

        else:
            # Processing a single file
            try:
                files = input_folder

                # Determine directory of the file
                directory = os.path.dirname(files)

                # Create output directory next to the original file
                output_folder = os.path.join(directory, "RemBG'dImgs")

                os.makedirs(output_folder, exist_ok=True)

                # Process the single file
                iterate(files)

            except Exception as e:
                print(f"Error processing single file: {e}")
                return

        # If no supported files were found
        if not files:
            print("No supported image files found in the folder.")
            return

        # Completion message
        print(f"Background removal completed. Results saved in: {output_folder}")

    except Exception as e:
        # Catch any unexpected error in the main folder processing
        os.system('cls')
        print(f"Error processing folder: {e}")


def get_folder_path():
    """
    Opens a folder selection dialog so the user can
    choose which folder to process.
    """

    try:
        # Clear console
        os.system('cls')

        print("Opening folder selection dialog...")

        # Create hidden Tkinter root window
        root = Tk()
        root.withdraw()

        # Open folder selection dialog
        folder_path = filedialog.askdirectory(
            title="Select a folder to clean"
        )

        # If user cancels dialog
        if not folder_path:
            print("No folder selected.")
            return None

        print(f"Selected folder: {folder_path}")

        return folder_path

    except Exception as e:
        os.system('cls')
        print(f"Error selecting folder: {e}")
        return None


# Entry point of the script
if __name__ == "__main__":

    try:
        # Message displayed after processing completes
        output_message = ""

        # If a command-line argument is provided
        # this usually means the user drag-and-dropped
        # a file or folder onto the executable
        if len(sys.argv) > 1:

            os.system('cls')

            input_path = sys.argv[1]

            # Check if the provided path is a folder
            if os.path.isdir(input_path):

                print(f"Drag-and-drop folder detected: {input_path}")

                # Process folder
                rembg_folder(input_path, True)

                output_message = (
                    f"Image backgrounds for directory: {input_path} are cleaned."
                )

            # Check if the provided path is a file
            elif os.path.isfile(input_path):

                print(f"A file was provided: {input_path}")

                # Process single file
                rembg_folder(input_path, False)

                output_message = (
                    f"Image background for file: {input_path} is cleaned."
                )

            else:
                print(f"Invalid path: {input_path}")

        else:
            # If no argument was provided, open folder selection dialog
            folder_path = get_folder_path()

            if folder_path:

                rembg_folder(folder_path, True)

                output_message = (
                    f"Image backgrounds for directory: {folder_path} are cleaned."
                )

            else:
                output_message = "No folder selected. Try again!"

        # Clear console and show final message
        os.system('cls')
        print(output_message)

    except Exception as e:
        # Catch unexpected fatal errors
        os.system('cls')
        print(f"Unexpected error: {e}")