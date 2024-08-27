# Text Summarization Tool

This project is a **Text Summarization Tool** built using the BART model (`facebook-bart-large-cnn`) and Streamlit for an interactive web interface. The tool allows users to input text and choose from three summarization styles: **Normal**, **Precise**, and **Accurate**. The tool generates concise summaries of the input text by adjusting length and other parameters based on the selected style.

## Features

- **Interactive Web Interface**: Built with Streamlit, providing an easy-to-use platform for text summarization.
- **Customizable Summarization Styles**: Select from Normal, Precise, and Accurate styles to tailor the summary to your needs.
- **Real-time Summarization**: Generates summaries quickly using the pre-trained BART model.

## How It Works

1. **Input Text**: Enter the text you want to summarize in the provided text area.
2. **Choose Style**: Select a summarization style from the dropdown menu: Normal, Precise, or Accurate.
3. **Generate Summary**: Click the "Summarize" button to generate a concise summary of your input text.

## Installation

Follow these steps to run the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/text-summarization-tool.git
    cd text-summarization-tool
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Dependencies

- Python 3.7+
- Transformers (`transformers`)
- TensorFlow (`tensorflow`)
- Streamlit (`streamlit`)

## Example Usage

1. Run the application using `streamlit run app.py`.
2. Open your web browser and navigate to `http://localhost:8501`.
3. Enter your text, choose the summarization style, and click "Summarize" to see the result.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

---

Feel free to customize this template further to fit your project's needs.
