import os
import sys
from PIL import Image, ImageFilter

def display_menu():
    """Displays the filter options to the user."""
    print("Filter Options:")
    print("1. Outline")
    print("2. Negative")
    print("3. Binary")
    print("4. Gray")
    print("5. Exit")
    print()

def get_filter_choice():
    """Prompts the user to select a filter option and returns the corresponding string."""
    while True:
        try:
            choice = int(input("Select a filter (1-5): "))
            if choice == 1:
                return 'outline'
            elif choice == 2:
                return 'negative'
            elif choice == 3:
                return 'binary'
            elif choice == 4:
                return 'gray'
            elif choice == 5:
                print("Exiting the application.")
                sys.exit()
            else:
                print("Invalid choice. Please select a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

class ImageFilterApp:
    def __init__(self, image_path):
        """
        Initializes the ImageFilterApp with the path to the image.
        
        :param image_path: Path to the input image file.
        :type image_path: str
        """
        self.image_path = image_path
        self.image = self._load_image()
        
    def _load_image(self):
        """Loads the image from the specified image path."""
        if not os.path.isfile(self.image_path):
            raise FileNotFoundError(f"Image file '{self.image_path}' not found.")
        return Image.open(self.image_path)

    def apply_filter(self, filter_type):
        """Applies the specified filter to the image and saves the result."""
        filter_methods = {
            'outline': self._outline_filter,
            'negative': self._negative_filter,
            'binary': self._binary_filter,
            'gray': self._gray_filter,
        }

        if filter_type not in filter_methods:
            raise ValueError(f"Filter type '{filter_type}' is not recognized. Choose from {list(filter_methods.keys())}.")

        filtered_image = filter_methods[filter_type]()
        self._save_image(filtered_image, filter_type)

    def _outline_filter(self):
        """Applies an outline filter to the image."""
        return self.image.filter(ImageFilter.FIND_EDGES)

    def _negative_filter(self):
        """Applies a negative filter to the image."""
        return Image.eval(self.image, lambda x: 255 - x)

    def _binary_filter(self):
        """Applies a binary filter to the image, converting it to black and white."""
        gray_image = self.image.convert("L")
        return gray_image.point(lambda x: 255 if x > 128 else 0)

    def _gray_filter(self):
        """Converts the image to grayscale."""
        return self.image.convert("L")

    def _save_image(self, filtered_image, filter_type):
        """Saves the filtered image in the same directory as the original image."""
        directory, original_filename = os.path.split(self.image_path)
        new_filename = f"{os.path.splitext(original_filename)[0]}_{filter_type}.png"
        new_image_path = os.path.join(directory, new_filename)
        filtered_image.save(new_image_path)
        print(f"Filtered image saved as '{new_image_path}'.")

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    
    try:
        app = ImageFilterApp(image_path)
        while True:
            display_menu()
            filter_choice = get_filter_choice()
            app.apply_filter(filter_choice)
    except Exception as e:
        print(f"An error occurred: {e}")
