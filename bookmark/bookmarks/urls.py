from django.urls import path
from bookmarks import views

app_name = 'bookmarks'

urlpatterns  = [  
  # path('', views.bookmark_list, name='list'),
  # path('<int:pk>/', views.bookmark_detail, name='detail'),
  # path('create/', views.bookmark_create, name='create'),
  # path('update/<int:pk>/', views.bookmark_update, name='update'),
  # path('delete/<int:pk>/', views.bookmark_delete, name='delete')

  path('new/',views.BookmarkListView.as_view(), name='list'),
  path('new/<int:pk>/',views.BookmarkDetailView.as_view(), name='detail'),
  path('new/create/',views.BookmarkCreateView.as_view(), name='create'),
  path('new/update/<int:pk>/',views.BookmarkUpdateView.as_view(), name='update'),
  path('new/delete/<int:pk>/',views.BookmarkDeleteView.as_view(), name='delete')

]


