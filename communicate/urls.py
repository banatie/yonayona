from django.urls import path

from . import views


app_name = 'communicate'
urlpatterns = [
    # User Account
    path('', views.index, name='index'),
    #path('', views.index, name='user_top_page'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('report/user', views.report_user, name='report_user'),
    # Message
    path('message/send', views.add_message, name='add_message'),
    # Conversation
    path('conversation/<int:conversation_id>/view/', views.view_conversation, name='conversation_view'),
    path('conversation/<int:conversation_id>/delete/', views.delete_conversation, name='conversation_delete'),
]
