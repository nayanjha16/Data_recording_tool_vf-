from django.shortcuts import render, HttpResponseRedirect
from . import forms
from . import models


def dashboard(request):
    if request.user.is_authenticated:
        try:
            user_prompts = models.audio_files.objects.filter(user=request.user)
            last_prompt = user_prompts.last()
            if last_prompt.audio.name[-5]=="i":
                new_prompt_id = last_prompt.sentence.id
                new_prompt = models.sentences.objects.get(id=new_prompt_id)
                
            elif last_prompt.sentence.id < models.sentences.objects.count():
                new_prompt_id = last_prompt.sentence.id + 1
                new_prompt = models.sentences.objects.get(id=new_prompt_id)
            else:
                return HttpResponseRedirect("/user/thankyou")
            context = {'prompt': new_prompt.sentence,
                       'id': new_prompt.id}
        except BaseException as e:
            first_prompt = models.sentences.objects.get(id=1)
            context = {'prompt': first_prompt.sentence,
                       'id': first_prompt.id}
        return render(request, 'collector/recorder.html', context)
    else:
        return HttpResponseRedirect('/')
    return render(request, 'collector/recorder.html', {})


def upload_audio(request):
    if request.method == 'POST':
        audio_upload = forms.audio_upload_form(request.POST, request.FILES)
        num= int(request.POST['num'])
        if 'save_all' in request.POST:
            if audio_upload.is_valid():
                audio = audio_upload.save(commit=False)
                prompt = models.sentences.objects.get(id=request.POST['pid'])
                
                audio.sentence = prompt
                audio.user = request.user
                audio.audio.name = str(audio.user.id) + "_" + str(audio.sentence.id)+"_"+ +num+ "i.wav"
                audio.save()
        else:
            if audio_upload.is_valid():
                audio = audio_upload.save(commit=False)
                prompt = models.sentences.objects.get(id=request.POST['pid'])
                audio.sentence = prompt
                audio.user = request.user
                audio.audio.name = str(audio.user.id) + "_" + str(audio.sentence.id) +"_"+num+ ".wav"
                audio.save()



    return HttpResponseRedirect('/user/dashboard')

def thankyou(request):
    return render(request, 'collector/thankyou.html', {})
