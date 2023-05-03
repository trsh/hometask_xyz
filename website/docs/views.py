from django.shortcuts import render


def index(request):
    return render(request, "docs/index.html")

def doc_edit(request, doc_id):
    return render(request, "docs/doc_edit.html", {"doc_id": doc_id})

def doc_view(request, doc_id):
    return render(request, "docs/doc_view.html", {"doc_id": doc_id})