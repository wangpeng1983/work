# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def count(request):
    user_text = request.GET["text"]
    total_count = (len(user_text))

    word_dirt = {}

    for word in user_text:
        if word not in word_dirt:
            word_dirt[word] = 1
        else:
            word_dirt[word] += 1
    # sorted_dict = (word_dirt.items(), key=lambda w: w[1], reverse=True)

    return render(request, "count.html",
                  {"count": total_count, "text": user_text, "word": word_dirt})
