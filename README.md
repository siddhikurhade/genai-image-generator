# AI Image Generator Using Flask

An AI-powered text-to-image generation web application that converts natural-language prompts into images using a pretrained generative AI model.

## Features

- Generate images from text prompts.
- Simple and user-friendly web interface.
- Flask backend for handling image-generation requests.
- Display and download generated images.
- Save generated images locally.
- Modular HTML, CSS, and Python structure.

## Technologies Used

- **Python**
- **Flask**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Stable Diffusion / Diffusers** or a configured image-generation API

## Project Structure

```text
genai-image-generator/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── generated/
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/siddhikurhade/genai-image-generator.git
cd genai-image-generator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the image-generation model

Configure the required model and credentials according to the backend implementation. If using an API, store credentials in a local `.env` file and never upload that file to GitHub.

If using local Stable Diffusion through Diffusers, ensure your computer has enough memory and storage to download and run the model.

### 5. Run the application

```bash
python app.py
```

Open the local URL displayed in the terminal, typically:

```text
http://127.0.0.1:5000/
```

## How It Works

1. The user enters a text prompt.
2. The frontend sends the prompt to the Flask backend.
3. The configured image-generation model processes the prompt.
4. The generated image is saved locally.
5. The application displays the generated image for the user.

## Security

- API keys and tokens must remain private.
- The `.env` file is excluded through `.gitignore`.
- Generated images and downloaded model files are not committed by default.

## Future Improvements

- Add more image-generation models.
- Provide image-size and style controls.
- Improve generation progress and error handling.
- Add a generation history and gallery.
- Deploy the application online.

## Author

**Siddhi Kurhade**

GitHub: [@siddhikurhade](https://github.com/siddhikurhade)

---

*This project was developed for learning and experimentation with generative AI and text-to-image generation.*
