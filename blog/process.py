from .models import transcript
pk=1
text=transcript.objects.all()[pk]


def grammar(transcribed_text):
    
    
    from gingerit.gingerit import GingerIt

    #text = 'The smelt of fliwers bring back memories.'

    parser = GingerIt()
    correct=parser.parse(transcribed_text) 
    return correct
new_text=grammar(text)
print(new_text)
