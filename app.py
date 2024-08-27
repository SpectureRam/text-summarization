import os
import streamlit as st
from transformers import BartTokenizer, TFBartForConditionalGeneration

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model_name = 'facebook-bart-large-cnn'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = TFBartForConditionalGeneration.from_pretrained(model_name)

def summarize(text, style):
    input_length = len(tokenizer.encode(text, return_tensors='tf', max_length=1024, truncation=True)[0])

    if style == 'Normal':
        max_length = int(input_length * 0.6)
        min_length = int(input_length * 0.5)
        length_penalty = 1.5
    elif style == 'Precise':
        max_length = int(input_length * 0.45)
        min_length = int(input_length * 0.35)
        length_penalty = 1.2
    else:
        max_length = int(input_length * 0.4)
        min_length = int(input_length * 0.3)
        length_penalty = 1.0

    inputs = tokenizer.encode(text, return_tensors='tf', max_length=1024, truncation=True)
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=length_penalty,
        num_beams=4,
        no_repeat_ngram_size=3,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

    if not summary.endswith(('.', '!', '?')):
        summary += '.'
    return summary

st.title('Text Summarizer')
user_input = st.text_area("Enter text to summarize:", "")
summary_style = st.selectbox(
    'Choose summarization style:',
    ('Normal', 'Precise', 'Accurate')
)

if st.button('Summarize'):
    if user_input:
        summary = summarize(user_input, summary_style)
        st.write("Summary:")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")

# End of program 2.0