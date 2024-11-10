# OpenAI Image Generator

![AI-IMAGE-GENERATOR](readme_media/banner.png)

OpenAI Image Generator is a Python program that uses the OpenAI API for generating images. It utilizes OpenAI's DALL-E model to create images based on user prompts. This image generator does not have a graphical user interface (GUI); instead, you can input prompts directly into the console. The generator then creates an image and automatically downloads it.

## Features

- **Prompt-based Image Generation**: Generate images by entering text prompts.
- **Configurable Settings**: Set parameters such as image format, model version, and download path through a YAML configuration file.
- **Automatic Image Download**: Saves generated images in a specified directory with timestamped filenames for easy organization.
- **Error Handling**: Detects and handles errors related to missing API keys, configuration issues, and HTTP errors during image download.

## Requirements

- Python 3.7+
- OpenAI Python SDK
- PyYAML
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Michael-Schaeffer/openai-image-generator.git
   cd openai-image-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install openai pyyaml requests
   ```

3. Set up the OpenAI API key as an environment variable:

   In Windows Command Prompt
   ```bash
   setx OPENAI_API_KEY "your_openai_api_key"
   ```
   In a Linux or macOS terminal
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

4. (Optional) Edit the `config.yaml` file to customize settings.

## Configuration

The program reads configuration options from a `config.yaml` file. Below is an example configuration file:

```yaml
api:
  key_env_var: "OPENAI_API_KEY"

image_generation:
  format: "1024x1024"
  model: "dall-e-3"

storage:
  save_path: "downloads/images"
```

- `key_env_var`: Environment variable name that stores your OpenAI API key.
- `format`: Desired image resolution. Supported options include `1024x1024`, `512x512`, etc.
- `model`: Specify the OpenAI image model to use (e.g., `dall-e-3`).
- `save_path`: Directory path where generated images will be saved.

## Usage

1. Run the program:
   ```bash
   python openai-image-generator.py
   ```

2. When prompted, enter a text prompt for the image you want to generate:
   ```plaintext
   Enter your prompt (or type 'exit' to quit):
   A futuristic cityscape at sunset
   ```

3. The program will generate an image based on your prompt and download it to the specified directory with a timestamped filename.

4. To exit the program, type `exit`.

## Example

```plaintext
IMAGE GENERATOR started

Enter your prompt (or type 'exit' to quit):
A forest with magical creatures at dawn

Generating image...
Generated 1 image(s).
Image downloaded and saved as downloads/images/2023-11-01_12-45-30.png
```

## Error Handling

The program includes error handling for common issues:
- **Missing API Key**: Checks for the presence of the OpenAI API key in the environment.
- **Configuration Errors**: Alerts if the configuration file is missing or has errors.
- **HTTP Errors**: Handles HTTP errors when downloading images, with informative status messages.

## License

This project is licensed under the MIT License.

---

### Notes
Ensure that the `OPENAI_API_KEY` environment variable is set before running the program.