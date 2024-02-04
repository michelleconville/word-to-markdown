import subprocess
from io import BytesIO
from django.shortcuts import render, redirect
from .forms import DocumentForm
from markdown import markdown
from docx import Document as DocxDocument
from .models import Document
import os


def convert_to_markdown(docx_content):
    # Write the docx content to a temporary file
    temp_docx_file = 'temp.docx'
    with open(temp_docx_file, 'wb') as f:
        f.write(docx_content)

    # Convert the docx file to Markdown using Pandoc
    output = subprocess.run(['pandoc', temp_docx_file, '--to=markdown'], capture_output=True, text=True)

    # Delete the temporary docx file
    os.remove(temp_docx_file)


    return output.stdout


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