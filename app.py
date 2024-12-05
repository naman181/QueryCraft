import streamlit as st
import os
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate

def generate_questions(input_text, subject, no_que, que_type):
    llm = CTransformers(model='model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.1})

    template = """
        Generate {no_que} {que_type} questions and four options including correct answer on 
        subject/topic {subject} for the given passage: {input_text} in format
        question: Question?
        option a: ...
        option b: ...
        option c: ...
        option d: ...
        correct Answer: ...
        """

    prompt = PromptTemplate(input_variables=["no_que", "que_type", "subject", "input_text"],
                            template=template)

    # Split input text into chunks
    max_token_length = 512
    chunks = [input_text[i:i+max_token_length] for i in range(0, len(input_text), max_token_length)]

    responses = []
    for chunk in chunks:
        response = llm(prompt.format(no_que=no_que, que_type=que_type, subject=subject, input_text=chunk))
        responses.append(response)

    output_file = 'generated_questions.txt'
    with open(output_file, 'w') as file:
        for response in responses:
            file.write(response + '\n\n')

    return output_file

def main():
    st.title('Generate Questions')

    input_text = st.text_area('Enter the passage:')
    subject = st.text_input('Enter the subject/topic:')
    no_que = st.number_input('Number of questions:', min_value=1, step=1)
    que_type = st.selectbox('Question type:', ['MCQ', 'Short Answer'])

    if st.button('Generate'):
        questions_file_path = generate_questions(input_text, subject, no_que, que_type)
        st.markdown(f"Download your questions from [here](/{questions_file_path})", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
