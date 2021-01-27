from django.shortcuts import render
import requests 
from .models import Post, User


def index(request):
    
    if User.objects.exists() == False and Post.objects.exists() == False:

        reqUsers = requests.get('http://jsonplaceholder.typicode.com/users')
        users = reqUsers.json() 

        reqPosts = requests.get('http://jsonplaceholder.typicode.com/posts')
        posts = reqPosts.json()

        for item in users: 
            user = User.objects.create(
                id = item['id'],
                name = item['name'],
                username = item['username'],
                email = item['email'],
                address = item['address'],
                phone = item['phone'],
                website = item['website'],
                company = item['company']
            ) 
            user.save()
             
            for itemPost in posts:
                if  itemPost['userId'] == item['id']:
                    post = Post.objects.create(
                        id = itemPost['id'],
                        userId = user,
                        title = itemPost['title'],
                        body = itemPost['body'], 
                    ) 
                    post.save()
                    

    content = []
    posts = Post.objects.values('userId', 'title', 'body')
    users = User.objects.values('id', 'name')
    for post in posts:
        for user in users:
            if user['id'] == post['userId']:
                content.append({
                    'title': post['title'],
                    'body': post['body'],
                    'name': user['name'],
                })
    
    
    
    return render(request, 'main/index.html', {'content': content})
