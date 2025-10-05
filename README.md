# Mixture of Experts for Interactive Literature Analysis

An interactive research paper analysis system that leverages the Mixture of Experts (MoE) paradigm with large language models to provide on-demand analytical capabilities for research papers.

## Overview

This system offers three specialized LLM-powered experts:
- **Summarization Expert**: Generates concise 3-5 sentence summaries of paper abstracts
- **Contribution Extraction Expert**: Identifies and lists novel contributions as bullet points
- **Question Answering Expert**: Answers specific questions about paper content

Unlike traditional MoE systems with learned routing mechanisms, this system adopts a human-in-the-loop design where users select which expert to consult based on their analytical needs.

## Features

- PDF paper processing and text extraction
- Three specialized LLM experts powered by Google Gemini 2.0 Flash
- Human-guided expert routing for transparency and control
- Interactive web interface built with Gradio
- Automatic abstract detection and extraction

## System Architecture

```
PDF Input → Data Preprocessing → Extracted Text
                                      ↓
                    ┌─────────────────┼─────────────────┐
                    ↓                 ↓                 ↓
            Summarization      Contribution         Q&A
               Expert            Expert            Expert
                    ↓                 ↓                 ↓
                    └─────────────────┼─────────────────┘
                                      ↓
                        Interactive Interface (Gradio)
                                      ↓
                              Analysis Output
```

## Installation

### Prerequisites
- Python 3.10 or higher
- Google Gemini API key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/stanley7/Interactive-Literature-Analysis.git
cd Interactive-Literature-Analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
GEMINI_API_KEY=your-api-key-here
```

## Usage

1. Place your PDF research papers in the `Datasets/papers/` directory

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to the local URL provided (typically `http://127.0.0.1:7860`)

4. Select a paper from the dropdown menu and choose an expert:
   - **Summarize tab**: Get a concise summary
   - **Extract Contributions tab**: Identify novel contributions
   - **Q&A tab**: Ask specific questions about the paper

## Project Structure

```
Interactive-Literature-Analysis/
├── app.py                      # Gradio interface
├── llm_experts.py             # Expert module implementations
├── data_preprocessing.py      # PDF processing and text extraction
├── requirements.txt           # Python dependencies
├── Mixture of Experts for Interactive Literature Analysis.pdf   # Term paper    
├── Datasets/
│   └── papers/               # PDF papers 
└── README.md
```

## Requirements

```
gradio>=4.0
google-genai
PyMuPDF
python-dotenv
```

## How It Works

### Data Preprocessing
- Extracts text from PDF files using PyMuPDF
- Identifies abstract sections using pattern matching
- Falls back to first 1,500 characters if abstract detection fails

### Expert Design
Each expert uses task-specific prompts optimized for:
- **Summarization**: 3-5 sentence overviews focusing on main findings
- **Contribution Extraction**: Structured bullet-point lists of novel ideas
- **Q&A**: Targeted responses to user-specified questions

### Human-in-the-Loop Routing
Users act as the routing mechanism, selecting experts based on their information needs. This provides:
- Greater transparency in analytical functions
- User control over exploration workflow
- Iterative refinement through multiple expert consultations
- Clear relationship between user intent and system output

## Ethical Considerations

Users should be aware of:
- **Hallucinations**: LLMs may generate plausible but incorrect information
- **Oversimplification**: Automated summaries may omit important nuances
- **Verification Required**: Always verify critical details against original papers
- **Bias Propagation**: Underlying LLM biases may affect outputs

## Limitations

- Analyzes abstracts only (not full paper text)
- Supports PDF format only
- English language papers only
- Requires internet connection for API calls

## Future Work

- Full-text analysis support
- Multi-language support
- User study evaluation

## License

MIT License - See LICENSE file for details

## Author

Stanley Joel Gona  
University of Potsdam  
Email: gona@uni-potsdam.de

## Acknowledgments

- Built with [Gradio](https://gradio.app)
- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)
- PDF processing with [PyMuPDF](https://pymupdf.readthedocs.io)
