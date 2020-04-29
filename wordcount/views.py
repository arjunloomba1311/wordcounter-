from django.http import HttpResponse
from django.shortcuts import render
import operator

def Home(request):
     return render(request,'home.html')

def count(request):
     fulltext = request.GET['fulltext']
     worldlist = []
     wordlist = fulltext.split()
     word_dict = {}

     for word in wordlist:
         if word.lower() in word_dict:
             word_dict[word.lower()] += 1
         else:
            word_dict[word.lower()] = 1
     dict_list = word_dict.items()
     sorted_list = sorted(dict_list,key = operator.itemgetter(1), reverse = True)

     return render(request,'count.html',{"fulltext":fulltext,'wordcount':len(wordlist), 'sorted_list':sorted_list })

def about(request):
    return render(request,'about.html')
