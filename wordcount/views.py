from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = [x.lower() for x in fulltext.split(" ")]
    totalwords = len(words)
    print(totalwords)
    counter = {}
    for word in words:
        if word.isalpha():
            c = counter.get(word)
            if c is None:
                counter[word] = 1
            else:
                counter[word] = c+1
    sorted_dict = sorted(counter.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html', {'originaltext': fulltext,
                                          'totalwords': totalwords,
                                          'counted':sorted_dict ,
                                          })

def about(request):
    return render(request,'about.html')