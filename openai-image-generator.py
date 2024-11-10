# OPENAI IMAGE GENERATOR

import os
import yaml
import requests  # For downloading generated images
from openai import OpenAI
from datetime import datetime
import sys

class ImageGenerator:
    def __init__(self, config_file="config.yaml"):
        # Load configuration from YAML
        self.config = self.load_config(config_file)

        # Get the environment variable name for the API key from the nested config
        api_key_env_var = self.config.get("api", {}).get("key_env_var", "OPENAI_API_KEY")
        self.api_key = os.environ.get(api_key_env_var)
        if not self.api_key:
            raise ValueError(f"API key must be provided in the environment variable '{api_key_env_var}'")

        # Set configurations for image format, model, and download path from nested fields
        self.image_format = self.config.get("image_generation", {}).get("format", "1024x1024")
        self.model = self.config.get("image_generation", {}).get("model", "dall-e-3")
        self.download_path = self.config.get("storage", {}).get("save_path", "downloads/images")

        # Initialize OpenAI client
        self.client = OpenAI(api_key=self.api_key)

        # Ensure the download directory exists
        os.makedirs(self.download_path, exist_ok=True)

    def load_config(self, config_file):
        """Load configuration from a YAML file."""
        try:
            with open(config_file, "r") as file:
                config = yaml.safe_load(file)
            return config
        except FileNotFoundError:
            print(f"Configuration file '{config_file}' not found. Using default values.")
            return {}
        except yaml.YAMLError as e:
            print(f"Error loading configuration file: {e}")
            return {}

    def create_image(self, prompt, n=1):
        """Generate an image based on the prompt and return URLs."""
        try:
            image_response = self.client.images.generate(
                prompt=prompt,
                n=n,
                size=self.image_format,
                model=self.model
            )

            # Extract URLs from the response
            image_urls = [image.url for image in image_response.data if image.url]

            if image_urls:
                print(f"Generated {len(image_urls)} image(s).")
                # Download and save the first image
                self.download_image(image_urls[0])
            else:
                print("No images generated.")
            return image_urls

        except Exception as e:
            print(f"Error generating image: {e}")
            return []

    def download_image(self, url):
        """Download an image from a URL and save it locally."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Generate a unique filename using timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f"{timestamp}.png"
                save_path = os.path.join(self.download_path, filename)

                # Save the image content
                with open(save_path, "wb") as file:
                    file.write(response.content)
                print(f"Image downloaded and saved as {save_path}")
            else:
                print("Failed to download image. Status code:", response.status_code)
        except Exception as e:
            print(f"Error downloading image: {e}")

if __name__ == "__main__":
    print("IMAGE GENERATOR started")

    # Create the ImageGenerator instance
    try:
        image_generator = ImageGenerator()
    except Exception as e:
        print(f"Error initializing ImageGenerator: {e}")
        sys.exit(1)

    # Main loop for generating images
    while True:
        prompt = input("\nEnter your prompt (or type 'exit' to quit):\n\n")
        
        if prompt.lower() == "exit":
            print("Exiting the program.")
            break

        print("\nGenerating image...")
        try:
            # Generate images based on prompt
            response_images = image_generator.create_image(prompt, n=1)
            if not response_images:
                print("No images were returned.")
        except Exception as e:
            print(f"Error interacting with OpenAI: {e}")
