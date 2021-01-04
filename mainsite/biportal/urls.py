from django.urls import path

from . import views

# this is for the app to figure out the namespace of this app when constructing the links
app_name = 'biportal'

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     # the 'name' value as called by the {% url %} template tag
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.home, name='home2'),
    # path('', views.HomeListView.as_view(), name='home2'),

    # # path('<int:pk>', views.board_topics, name='board_topics'),
    # path('<int:pk>', views.TopicsListView.as_view(), name='board_topics'),


    # path('<int:pk>/new/', views.new_topic, name='new_topic'),

    # # path('<int:pk>/topics/<int:topic_pk>/', views.topic_posts, name='topic_posts'),
    # path('<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),


    # path('<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),

    # path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit', views.PostUpdateView.as_view(), name='edit_post'),

    # path('new_post/', views.NewPostView02.as_view(), name='new_post'),

]