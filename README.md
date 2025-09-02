# Utweet

# Mini Twitter Clone (Django)

This is a simple **Twitter-like app** built with Django.  
It allows users to register, log in, create tweets, edit/delete their tweets, and view tweets from other users.  

---

## 🚀 Features
- ✅ User registration & authentication (login/logout)  
- ✅ Create, edit, and delete tweets  
- ✅ View other users' tweets  
- ✅ CSRF-protected forms  
- ✅ Bootstrap UI for clean design  

---

## 🛠️ Tech Stack
- **Backend**: Django (Python)  
- **Frontend**: HTML, Bootstrap  
- **Database**: SQLite (default, can be swapped)  

---

## 📂 Project Structure

Views
Key views include:

tweet_list - Display all tweets

view_tweet - Show individual tweet with full content

create_tweet - Handle tweet creation

edit_tweet - Handle tweet editing

delete_tweet - Handle tweet deletio

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create_tweet/', views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>edit/', views.edit_tweet, name='edit_tweet'),
    path('<int:tweet_id>delete/', views.delete_tweet, name='delete_tweet'),
    path('register/', views.register, name='register'),
    path('<int:tweet_id>view_tweet/', views.view_tweet, name='view_tweet'),

]



