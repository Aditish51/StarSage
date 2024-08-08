from django.shortcuts import render
from django.http import HttpResponse
from . models import basic_mcq, basic_tf, basic_fbl
import random

def home_quiz(request):
    return render(request, 'home_quiz.html')

def levels(request):
    return render(request, 'levels.html')

def basic_ques(request):
    first_ques = basic_mcq.objects.get(id= random.randint(1,10))
    return render(request, 'basic_ques.html', {'first_ques':first_ques})

def next_ques(request):
    mcq_ques = basic_mcq.objects.get(id= random.randint(1,10))
    tf_ques = basic_tf.objects.get(id= random.randint(1,15))
    fbl_ques = basic_fbl.objects.get(id= random.randint(1,5))
    main_ques= [mcq_ques, tf_ques, fbl_ques]
    sel_ques = random.choice(main_ques)
    return render(request, 'next_ques.html', {'sel_ques':sel_ques,'mcq_ques':mcq_ques,'tf_ques':tf_ques,'fbl_ques':fbl_ques})