import gradio as gr

def calculate_sum(a,b):
    return str(int(a)+int(b))

interface = gr.Interface(fn= calculate_sum, inputs=['text', 'text'], outputs= ['text'])
interface.launch()