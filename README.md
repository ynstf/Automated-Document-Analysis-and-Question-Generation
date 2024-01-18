# OCR-QA Project

Automate document analysis and question generation using Optical Character Recognition (OCR) techniques and OpenAI's GPT-3.5-turbo model.

## Overview

This project utilizes PyPDFium, EasyOCR, Tesseract, and OpenAI's GPT-3.5-turbo to extract text from images and generate insightful questions and answers based on the content. Enhance your document analysis workflow with this versatile Python project.

## Features

- **OCR Techniques:** Utilize PyPDFium, EasyOCR, and Tesseract for efficient text extraction from images.
- **Question Generation:** Leverage GPT-3.5-turbo to automatically generate questions based on extracted text.
- **Versatile Usage:** Easily adapt the project for various document types and languages.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/ynstf/Automated-Document-Analysis-and-Question-Generation.git
    cd OCR-QA-Project
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:

    ```bash
    # Add your OpenAI GPT-3.5-turbo API key to the .env file
    echo "chatgpt_token=your-api-key" > .env
    ```

4. Run the script:

    ```bash
    python main.py
    ```


