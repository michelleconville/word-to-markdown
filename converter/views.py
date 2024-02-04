from io import BytesIO
from django.shortcuts import render, redirect
from .forms import DocumentForm
from markdown import markdown
from docx import Document as DocxDocument
from .models import Document
 
def convert_to_markdown(docx_content):
    # Ensure the content is read as binary data
    docx_io = BytesIO(docx_content)
    doc = DocxDocument(docx_io)
    markdown_content = ""
    for paragraph in doc.paragraphs:
        markdown_content += paragraph.text + "\n"
    return markdown(markdown_content)
 
def convert_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            docx_content = document.file.read()
            markdown_content = convert_to_markdown(docx_content)
            document.markdown_content = markdown_content
            document.save()
            return redirect('document_detail', pk=document.pk)
    else:
        form = DocumentForm()
    return render(request, 'converter/convert_document.html', {'form': form})
 
def document_detail(request, pk):
    document = Document.objects.get(pk=pk)
    return render(request, 'converter/document_detail.html', {'document': document})