from django.urls import path

from . import views


app_name = 'communicate'
urlpatterns = [
    # User Account
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('update/user/bgm/', views.update_user_settings, name='update_user_settings'),
    path('report/user/<int:conversation_id>/<str:explanation>/', views.report_user, name='report_user'),
    # Conversation
    path('conversation/start/', views.start_conversation, name='start_conversation'),
    path('conversation/<int:conversation_id>/cancel/', views.cancel_conversation, name='cancel_conversation'),
    path('conversation/<int:conversation_id>/end/', views.end_conversation, name='end_conversation'),
    path('conversation/<int:conversation_id>/view/', views.view_conversation, name='view_conversation'),
    path('conversation/<int:conversation_id>/delete/', views.delete_conversation, name='delete_conversation'),
]
