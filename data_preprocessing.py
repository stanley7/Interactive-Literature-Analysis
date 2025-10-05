import os
import fitz  

def list_papers(paper_dir):
    return sorted([f for f in os.listdir(paper_dir) if f.lower().endswith('.pdf')])

def get_paper_text(paper_dir, filename):
  
    file_path = os.path.join(paper_dir, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist!")
    doc = fitz.open(file_path)
    text = "".join([page.get_text() for page in doc])
    return text.strip()


if __name__ == "__main__":

    paper_dir = "Datasets/papers"
    papers = list_papers(paper_dir)
    print(f"Found {len(papers)} papers.")
    if papers:
        print(f"First paper: {papers[0]}")
        content = get_paper_text(paper_dir, papers[0])
        print(f"First 500 characters:\n{content[:500]}")
