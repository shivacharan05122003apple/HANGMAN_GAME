from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.conf.urls import url
from .models import game
from gtts import gTTS
import random
g1=game()
def home(request):
    return render(request,'home.html')

def add(request):
    
    
    g1.name=request.POST["n"]
    words_to_guess =  [ 'account','air','amount','animal','answer','approval','art','attack','attention','back','base','behaviour','belief', 'birth','blood','blow','body',
    'bread','breath','brother','building','burn','business','butter','care','cause','chance','change','cloth','color','comfort','company',
    'comparison','competition','connection','cook','country','cover','credit','cry','current','damage','danger','daughter','day','death', 'decision',
    'detail','development','direction']
    data=[ 'an arrangement with a bank to keep your money there and allow you to take it out when you need to.'
    , 'the mixture of gases that surrounds the Earth and that we breathe.'
    , 'a collection or mass especially of something that cannot be counted.'
    , 'something that lives and moves, but is not a human, bird, insect, or fish.'
    , 'the receipt and response to a letter, question, or phone call.'
    , 'the feeling of having a positive opinion of someone or something.'
    ,'the activity of making objects, drawings, music, paintings, sculptures, etc that are beautiful or that express feeling.'
    , ' to try to hurt or defeat (mainly referred to as physical violence but can also be used to describe verbal or emotional outbursts).'
    , 'notice, thought or interest.'
    , '(adverb) in return, into, towards a previous place or condition, or an earlier time; (noun) the part of your body that is opposite to the front, from your shoulder to your bottom.'
    , 'the bottom part of an object, on which it rests, or the lowest part of something.'
    , 'the way that someone behaves.'
    , 'the feeling of being certain that something exists or is true, something that you believe.'
    , 'the time when a young baby or young animal comes out of its mother’s body.'
    , 'the red liquid that is sent around the body by the heart.'
     ,'to move and make currents of air, or to make a sound by forcing air out of your mouth.'
    ,'the whole physical structure that forms a person or animal.'
    , 'a food made from flour, water, and usually yeast, mixed together and baked.'
    , 'the air that goes into and out of your lungs.'
    , 'a man or boy with the same parents as another person.'
    , 'a structure with walls and a roof, such as a house or a factory.'
    , 'to be hurt, damaged, or destroyed by fire or extreme heat, or to cause this to happen.'
    ,  'the activity of buying and selling goods and services.'
    , 'a pale yellow food containing a lot of fat that is made from cream, usually spread on bread or used in cooking.'
    , 'the process of protecting someone or something, and providing what they need.'
    , 'the reason why something, especially something bad, happens.'
    , ' an occasion that allows something to be done.'
    , 'to exchange one thing for another thing, or to make or become different.'
    ,' a type of woven material, usually used in cleaning to remove dirt, dust, or liquid.'
    , 'red, blue, green, yellow, red, orange, etc.'
    , 'a pleasant feeling of being relaxed and free from pain.'
    , ' organization that sells goods or services in order to make money.'
    , 'the act of comparing two or more people or things.'
    , 'a situation in which someone is trying to win something or be more successful than someone else.'
    , 'the state of being related to someone or something.'
    , '(verb) when you prepare food to be eaten by heating it until it is ready, or (noun) a person who prepares and cooks food.'
    , 'An area of land that has its own government, army, etc.'
    , 'to put or spread something over something, or to lie on the surface of something.'
    , 'praise, approval, or honor.'
     ,'to produce tears as the result of strong emotion, such as sadness, fear, happiness, or pain.'
    , ' the present time.'
    , 'to harm or spoil something.'
    , 'the possibility of harm or death to someone.'
    , 'your female child.'
    , 'a period of 24 hours.'
    , 'the end of life.'
    ,  'a choice that you make about something after thinking about all the possible options.'
    , 'a single piece of information or fact about something.'
    , 'the process in which someone or something grows or changes and becomes more advanced.'
    , 'the position towards which someone or something moves or faces.' ]
    data2=dict(zip(words_to_guess,data))
    g1.word = random.choice(words_to_guess)
    g1.clue=data2[g1.word]
    g1.answer=g1.word
    g1.error=False
    g1.length = len(g1.word)
    image="/images/hang0.gif"
    g1.count = 0
    
    g1.limit=6
    g1.display = '_'' '* g1.length
    g1.already_guessed = []
    g1.play_game = ""
    return render(request,"gamehome.html",{'g1':g1})

def pickword(request):
    words_to_guess =  [ 'account','air','amount','animal','answer','approval','art','attack','attention','back','base','behaviour','belief', 'birth','blood','blow','body',
    'bread','breath','brother','building','burn','business','butter','care','cause','chance','change','cloth','color','comfort','company',
    'comparison','competition','connection','cook','country','cover','credit','cry','current','damage','danger','daughter','day','death', 'decision',
    'detail','development','direction']
    data=[ 'an arrangement with a bank to keep your money there and allow you to take it out when you need to.'
    , 'the mixture of gases that surrounds the Earth and that we breathe.'
    , 'a collection or mass especially of something that cannot be counted.'
    , 'something that lives and moves, but is not a human, bird, insect, or fish.'
    , 'the receipt and response to a letter, question, or phone call.'
    , 'the feeling of having a positive opinion of someone or something.'
    ,'the activity of making objects, drawings, music, paintings, sculptures, etc that are beautiful or that express feeling.'
    , ' to try to hurt or defeat (mainly referred to as physical violence but can also be used to describe verbal or emotional outbursts).'
    , 'notice, thought or interest.'
    , '(adverb) in return, into, towards a previous place or condition, or an earlier time; (noun) the part of your body that is opposite to the front, from your shoulder to your bottom.'
    , 'the bottom part of an object, on which it rests, or the lowest part of something.'
    , 'the way that someone behaves.'
    , 'the feeling of being certain that something exists or is true, something that you believe.'
    , 'the time when a young baby or young animal comes out of its mother’s body.'
    , 'the red liquid that is sent around the body by the heart.'
     ,'to move and make currents of air, or to make a sound by forcing air out of your mouth.'
    ,'the whole physical structure that forms a person or animal.'
    , 'a food made from flour, water, and usually yeast, mixed together and baked.'
    , 'the air that goes into and out of your lungs.'
    , 'a man or boy with the same parents as another person.'
    , 'a structure with walls and a roof, such as a house or a factory.'
    , 'to be hurt, damaged, or destroyed by fire or extreme heat, or to cause this to happen.'
    ,  'the activity of buying and selling goods and services.'
    , 'a pale yellow food containing a lot of fat that is made from cream, usually spread on bread or used in cooking.'
    , 'the process of protecting someone or something, and providing what they need.'
    , 'the reason why something, especially something bad, happens.'
    , ' an occasion that allows something to be done.'
    , 'to exchange one thing for another thing, or to make or become different.'
    ,' a type of woven material, usually used in cleaning to remove dirt, dust, or liquid.'
    , 'red, blue, green, yellow, red, orange, etc.'
    , 'a pleasant feeling of being relaxed and free from pain.'
    , ' organization that sells goods or services in order to make money.'
    , 'the act of comparing two or more people or things.'
    , 'a situation in which someone is trying to win something or be more successful than someone else.'
    , 'the state of being related to someone or something.'
    , '(verb) when you prepare food to be eaten by heating it until it is ready, or (noun) a person who prepares and cooks food.'
    , 'An area of land that has its own government, army, etc.'
    , 'to put or spread something over something, or to lie on the surface of something.'
    , 'praise, approval, or honor.'
     ,'to produce tears as the result of strong emotion, such as sadness, fear, happiness, or pain.'
    , ' the present time.'
    , 'to harm or spoil something.'
    , 'the possibility of harm or death to someone.'
    , 'your female child.'
    , 'a period of 24 hours.'
    , 'the end of life.'
    ,  'a choice that you make about something after thinking about all the possible options.'
    , 'a single piece of information or fact about something.'
    , 'the process in which someone or something grows or changes and becomes more advanced.'
    , 'the position towards which someone or something moves or faces.' ]
    data2=dict(zip(words_to_guess,data))
    g1.word = random.choice(words_to_guess)
    g1.clue=data2[g1.word]
    print(g1.word)
    print(g1.clue)
    g1.answer=g1.word
    g1.error=False
    g1.length = len(g1.word)
    g1.count = 0
    g1.win=False
    g1.limit=6
    g1.display = '_'' '* g1.length
    g1.already_guessed = []
    g1.play_game = ""
    return render(request,"gamehome.html",{'g1':g1})

def check(request):
    
      g1.guess=request.POST["guess"]  
      g1.error=False   
      g1.guess = g1.guess.strip()
      if len(g1.guess.strip()) == 0 or len(g1.guess.strip()) >= 2 or g1.guess <= "9":
         return render (request,'gamehome.html',{'g1':g1, 'error':"invalid input" } )
      elif g1.guess in g1.word:
         g1.already_guessed.extend([g1.guess])
         index = g1.word.find(g1.guess)
         g1.word = g1.word[:index] + "_" + g1.word[index + 1:]
         g1.display = g1.display[:index*2]+ g1.guess + g1.display[index*2 + 1:]
        
         if g1.word=='_' * g1.length and g1.count<g1.limit:
             g1.win=True
             return render(request,"gamehome.html",{'g1':g1})
         else: 
          return render(request,"gamehome.html",{'g1':g1})
      
      elif g1.guess in g1.already_guessed:
          error="Try another letter"
          
          return render (request,'gamehome.html',{'g1':g1, 'error':error} )
    
      else:
          if g1.limit - g1.count > 0:
              g1.error=True
              g1.count += 1
              error="Wrong guess. " + str(g1.limit - g1.count) + " guesses remaining\n"
              audio(error)
              return render (request,'gamehome.html',{'g1':g1, 'error':error })
          else:
              g1.count += 1
              return render (request,'gamehome.html',{'g1':g1})

def play_loop():
    g1.play_game = request.POST['playgame']
    if g1.play_game == "y":
        pickword(request)

def clue(request):
    msg=g1.clue
    return render(request,'gamehome.html', {'g1':g1, 'msg':msg})

def audio(str):
    if g1.limit -g1.count == 5 :
      audio=gTTS(str)
      audio.save('static/audio5.mp3')  
    elif  g1.limit -g1.count == 4 :
      audio=gTTS(str)
      audio.save('static/audio4.mp3')
    elif  g1.limit -g1.count == 3 :
      audio=gTTS(str)
      audio.save('static/audio3.mp3')
    elif  g1.limit -g1.count == 2 :
      audio=gTTS(str)
      audio.save('static/audio2.mp3')
    else:
      audio=gTTS(str)
      audio.save('static/audio1.mp3')             

    
        

        