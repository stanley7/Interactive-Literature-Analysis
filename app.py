import gradio as gr
from data_preprocessing import list_papers, get_paper_text
from llm_experts import summarize_paper, extract_contributions, answer_question

# Path to  papers folder
PAPER_DIR = "Datasets/papers"
PREVIEW_CHARS = 600 

# List all available papers
paper_files = list_papers(PAPER_DIR)

def show_paper_preview(filename):    
    text = get_paper_text(PAPER_DIR, filename)
    return text[:PREVIEW_CHARS] + ("..." if len(text) > PREVIEW_CHARS else "")

def summarizer_interface(filename):    
    text = get_paper_text(PAPER_DIR, filename)
    return summarize_paper(text)

def contributions_interface(filename):   
    text = get_paper_text(PAPER_DIR, filename)
    return extract_contributions(text)

def qa_interface(filename, question):   
    text = get_paper_text(PAPER_DIR, filename)
    return answer_question(text, question)

with gr.Blocks() as demo:
    gr.Markdown("# Mixture of Experts: Research Paper Assistant")
    with gr.Row():
        selected_paper = gr.Dropdown(choices=paper_files, label="Select a Paper", value=paper_files[0] if paper_files else None)
        preview = gr.Textbox(label="Preview of Paper", lines=8, interactive=False)

    
    selected_paper.change(fn=show_paper_preview, inputs=selected_paper, outputs=preview)

    with gr.Tabs():
        with gr.TabItem("Summarize"):
            gr.Markdown("### Summarization Expert")
            sum_output = gr.Textbox(label="Summary", lines=8)
            sum_btn = gr.Button("Generate Summary")
            sum_btn.click(fn=summarizer_interface, inputs=selected_paper, outputs=sum_output)
        with gr.TabItem("Extract Contributions"):
            gr.Markdown("### Contribution Extraction Expert")
            contrib_output = gr.Textbox(label="Contributions", lines=8)
            contrib_btn = gr.Button("Extract Contributions")
            contrib_btn.click(fn=contributions_interface, inputs=selected_paper, outputs=contrib_output)
        with gr.TabItem("Q&A"):
            gr.Markdown("### Q&A Expert")
            qa_question = gr.Textbox(label="Enter your question", lines=2)
            qa_output = gr.Textbox(label="Answer", lines=8)
            qa_btn = gr.Button("Ask")
            qa_btn.click(fn=qa_interface, inputs=[selected_paper, qa_question], outputs=qa_output)

demo.launch()

