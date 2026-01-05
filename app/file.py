import PyPDF2
import docx

def extract_text(uploaded_file):
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        return " ".join(
            page.extract_text()
            for page in reader.pages
            if page.extract_text()
        )

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        return " ".join(p.text for p in doc.paragraphs)

    return ""
