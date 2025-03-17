from PIL import Image, ImageFilter
import os

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
        """
        Loads the image from the specified image path.
        
        :return: PIL Image object.
        :rtype: Image.Image
        :raises FileNotFoundError: If the image file does not exist.
        """
        if not os.path.isfile(self.image_path):
            raise FileNotFoundError(f"Image file '{self.image_path}' not found.")
        return Image.open(self.image_path)

    def apply_filter(self, filter_type):
        """
        Applies the specified filter to the image and saves the result.
        
        :param filter_type: The type of filter to apply. Accepts 'outline', 'negative', 'binary', or 'gray'.
        :type filter_type: str
        :raises ValueError: If the filter type is not recognized.
        """
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
        """
        Saves the filtered image in the same directory as the original image.
        
        :param filtered_image: The filtered PIL Image object.
        :type filtered_image: Image.Image
        :param filter_type: The filter type used for naming the output file.
        :type filter_type: str
        """
        directory, original_filename = os.path.split(self.image_path)
        new_filename = f"{os.path.splitext(original_filename)[0]}_{filter_type}.png"
        new_image_path = os.path.join(directory, new_filename)
        filtered_image.save(new_image_path)
        print(f"Filtered image saved as '{new_image_path}'.")

# Example of how to use the ImageFilterApp
if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"  # Specify the path to your image here
    filter_type = "gray"  # Specify your desired filter
    app = ImageFilterApp(image_path)
    app.apply_filter(filter_type)
