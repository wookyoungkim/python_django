from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request,'about.html')

def result(request):
    full_text=request.GET['fulltext']   #textarea에서 전송된 정보(fulltext)를 변수에 담기
    word_list=full_text.split()
    word_dictionary={}
    
    for word in word_list:
        if word in word_dictionary: #기존에 찾은 단어면
            word_dictionary[word]+=1
        else:   #word dictionary에 추가하기
            word_dictionary[word]=1
    
    return render(request,'result.html', {'fulltext':full_text, 'total':len(word_list), 'dictionary': word_dictionary.items()}) 
#데이터도 같이 result.html에 넘겨주기+result.html에서 full_text를 fulltext로 사용하기 