from django.shortcuts import render, HttpResponse, redirect,  get_object_or_404
from blog.forms import TODOForm, PostForm
from blog.models import TODO, Post
from django.contrib.auth.decorators import login_required
import datetime



# General

def home(request):
    print("Here")
    return render(request, 'blog/home.html', )

def about(request):
    return render(request, 'blog/about.html',{'title': 'About | TOLOG'})

# Blog Related
@login_required(login_url='loginPage')
def blog(request):
    currentUser = request.user

    post = Post.objects.filter(author= currentUser)
    # postForm = PostForm(request.POST)
    context = {
        'title': 'Blogs | TOLOG',
        'posts': post,
        # 'form': PostForm
    }
    return render(request, 'blog/blogs.html', context=context)

@login_required(login_url='loginPage')
def addNewBlog(request):
    
    postForm = PostForm(request.POST)
    context = {
        'title': 'New Blog | TOLOG',
        'form': postForm,
    }
    if postForm.is_valid():
            print("=> Adding New Blog")
            currentUser = request.user
            print('=> New Blog Submitted!!')
            post = postForm.save(commit=False)
            post.author = currentUser
            post.save()
            return redirect('blogPage')
    else:
        print("== Add new Blog Form Requested ==")
        return render(request, 'blog/saveblog.html', context=context)
    
def update_blog(request, id):
    post = Post.objects.get(pk = id)

    if request.method == 'POST':
        postForm = PostForm(request.POST, instance=post)
        if postForm.is_valid():
            postForm.save()
            return redirect('blogPage')
    else:
        postForm = PostForm(instance=post)

    context = {
        'title': 'Update Blog | TOLOG',
        'form': postForm,
    }
    return render(request, 'blog/updateblog.html', context=context)

def delete_blog(request , id ):
    print(f'\n=> Deleting Blog with the id: {id}\n')
    Post.objects.get(pk = id).delete()
    return redirect('blogPage')    

# Todo Related
@login_required(login_url='loginPage')
def addTodo(request):
    # user authenticated?
    if request.user.is_authenticated:
        user = request.user

        form = TODOForm(request.POST)
        # Form posted?
        if form.is_valid():
            print("=> Todo Form Submitted!!")
            # print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            # print(todo)
            return redirect("addTodoPage")

        else : 
            search = request.GET.get('search-area') or ''
            if search:
                print("== Search Query ==")
                todos = TODO.objects.filter(user=user, title__icontains=search)
                if todos:
                    context = {
                        'form': form,
                        'todos': todos,
                        'title': 'Todos | TOLOG',
                    }
                else:
                    context = {
                        'form': form,
                        'todos': todos,
                        'title': 'Todos | TOLOG',
                    }

            # Just Requested form
            else:
                print("\n== Todo Form Requested!! ==\n")
                todos = TODO.objects.filter(user = user).order_by('priority')
                context = {
                    'form': form,
                    'todos': todos,
                    'title': 'Todos | TOLOG',
                }
            return render(request , 'blog/addtodo.html' , context=context)

def delete_todo(request , id ):
    print(f'\n=> Deleting todo with the id: {id}\n')
    TODO.objects.get(pk = id).delete()
    return redirect('addTodoPage')

def change_todo(request , id  , status):
    print(f'\n=> Updating todo status with the id: {id}\n')
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('addTodoPage')



# Create your views here.
# posts = [
#     {
#         'title': 'First Blog Post',
#         'author': 'Umer Ishtiaq',
#         'date': '17 August 2023',
#         'content': 'This is the first blog post by Umer.'
#     },
#     {
#         'title': 'Second Blog Post',
#         'author': 'Poyo Oil',
#         'date': '17 September 2023',
#         'content': 'This is the second blog post by Poyo.'
#     },

# ]
