import requests
from django.contrib.humanize.templatetags import humanize
from django.shortcuts import render

from discussion_forums.utils import load_profanity_words, contains_profanity
from resource_library.models import Resource

PROFANE_WORDS = load_profanity_words('profanity.txt')


# Create your views here.

def resources(request):
    all_resources = Resource.objects.all().order_by('-added_at')
    for resource in all_resources:
        resource.humanized_added_at = humanize.naturaltime(resource.added_at)
    return render(request, "resource_page.html", {'resources': all_resources})


def dictionary(request):
    meanings = []
    word = ""

    if request.method == "POST":
        word = request.POST.get('word', '')
        word = word.capitalize()
        print(word)

        if word == "Web" or word == ".net":
            meanings.append("Can I get a hundred from this subject, please? :3")
        if contains_profanity(word, PROFANE_WORDS):
            word = "..."
            meanings.append("You can't use this here.")

        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

        if response.status_code == 200:
            data = response.json()

            for entry in data:
                word_data = entry.get('word', '')

                if word_data:
                    for meaning in entry.get('meanings', []):
                        definitions = meaning.get('definitions', [])

                        for definition in definitions:
                            meanings.append(definition.get('definition', ''))
    return render(request, 'dictionary.html', {'meanings': meanings, 'word': word})
