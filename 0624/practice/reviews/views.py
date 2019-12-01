from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from .models import Review

# Create your views here.
# 리뷰 생성하기(C:create)
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('/reviews/detail/' + str(review.id))
    elif request.method == 'GET':
        form = ReviewForm()
        return render(request, 'review_new.html', {'form': form})


# 모든 리뷰 리스트 보기(R:read)
def review_list(request):
    reviews = Review.objects.all()      #review의 form을 따르는 모든 오브젝트
    return render(request, 'review_list.html', {'reviews': reviews})

# 한 개의 리뷰 보기(R:read)
def review_detail(request, review_id):
    review_detail = get_object_or_404(Review, id=review_id)     #id: 모든 인스턴스는 각각의 오브젝트들을 구분하는 고유 아이디 필요 ->고유 아이디 갖는 데이터 가져오기
    return render(request, 'review_detail.html', {'review': review_detail})

# 리뷰 수정하기(U:update)
def review_update(request, review_id):      #선택한 리뷰에 대한 수정하기 위해 리뷰에 대한 아이디 넘겨주기
    review = get_object_or_404(Review, id=review_id)    #db에서 id로 조회한다음에 있는지?
    if request.method == 'GET':     
        form = ReviewForm(instance=review)
        return render(request,'review_update.html',{'form':form})
    elif request.method == "POST":      #
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('/reviews/detail/' + str(review.id))

# 리뷰 삭제하기(D:delete)
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('/reviews/')



