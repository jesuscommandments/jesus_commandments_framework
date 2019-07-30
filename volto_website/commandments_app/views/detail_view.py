from django.shortcuts import render, get_object_or_404
from django.views import View

from commandments_app.models import Commandment


class DetailView(View):
    def get(self, request, commandment_id):
        commandment = get_object_or_404(Commandment, pk=commandment_id)

        primary_bible_references = commandment.primary_bible_references()
        for bible_reference in primary_bible_references:
            bible_reference.load_text()
            secondary_bible_references = commandment.primary_bible_references()
        for bible_reference in secondary_bible_references:
            bible_reference.load_text()

        images = commandment.images()
        return render(request, 'commandments/detail.html', {'commandment': commandment,
                                                            'primary_bible_references': primary_bible_references,
                                                            'secondary_bible_references': secondary_bible_references,
                                                            'images': images})
