from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path('', views.review_list, name='review_list'), # 리뷰 리스트
    path('review/', views.review_create, name='create_review'), # 리뷰 생성
    path('detail/<int:review_id>/', views.review_detail, name='review_detail'), # 리뷰 자세히 보기
    path('update/<int:review_id>/', views.review_update, name='update_review'), # 리뷰 업데이트
    path('delete/<int:review_id>/', views.review_delete, name='delete_review'), # 리뷰 삭제하기
]
