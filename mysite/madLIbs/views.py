from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.


def accept(request):
    if request.method == 'POST':
        noun_plural = request.POST.get('noun_plural', '')
        noun = request.POST.get('noun', '')
        animal = request.POST.get('animal', '')
        verb_base_form = request.POST.get('verb_base_form', '')
        noun_2 = request.POST.get('noun_2', '')
        verb_base_form_2 = request.POST.get('verb_base_form_2', '')
        noun_3 = request.POST.get('noun_3', '')
        noun_4 = request.POST.get('noun_4', '')
        adjective = request.POST.get('adjective', '')
        story_type = request.POST.get('story_type, ''')

        profile = Profile(noun_plural=noun_plural, noun=noun, animal=animal, verb_base_form=verb_base_form,
                          noun_2=noun_2, verb_base_form_2=verb_base_form_2,
                          adjective=adjective, noun_3=noun_3, noun_4=noun_4, story_type=story_type)
        profile.save()

        if story_type == "story1":
            return render(request, 'madLibs/story1.html')
    return render(request, 'madLibs/accept.html')


def story_list(request, id):
    profile = Profile.objects.get(pk=id)
    return render(request, 'madLibs/story_list.html')


def story1(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, 'madLibs/story1.html', {'user_profile': user_profile})
