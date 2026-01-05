from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Image
from reportlab.lib.units import cm
from io import BytesIO
from PIL import Image as PILImage
import tempfile

def generate_pdf(summary, audience, wordcloud_image=None):
    """
    summary: list of sentences
    audience: string
    wordcloud_image: optional, numpy array (WordCloud.to_array())
    """
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    # Use SimpleDocTemplate for automatic wrapping
    doc = SimpleDocTemplate(tmp.name, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)

    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph(f"<b>{audience.capitalize()} Summary</b>", styles['Title']))
    elements.append(Spacer(1, 12))

    # Add bullet points
    for s in summary:
        elements.append(Paragraph(f"• {s}", styles['Normal']))
        elements.append(Spacer(1, 6))

    # Add WordCloud if provided
    if wordcloud_image is not None:
        img = PILImage.fromarray(wordcloud_image)
        image_stream = BytesIO()
        img.save(image_stream, format='PNG')
        image_stream.seek(0)
        elements.append(Spacer(1, 12))
        elements.append(Image(image_stream, width=16*cm, height=12*cm))

    doc.build(elements)
    return tmp.name
