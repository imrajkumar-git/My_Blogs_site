from django.shortcuts import redirect, render
from .models import Blog, BlogComment, Contact, Blog_category
from .forms import ContactForm, CreateBlogForm, UpdateBlogForm, CommentBlogForm
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from authors.models import UserProfuile
import math
import datetime
from django.db.models import Q


def blog_home(request):
    blogs = Blog.objects.all().order_by('-comment_date')

    blogs_category = Blog_category.objects.all()

    # week_ago = datetime.date.today() - datetime.timedelta(days=1)

    popular = Blog.objects.filter()

    # blogs.read+=1
    # blogs.save()

    no_of_posts = 10
    page = request.GET.get('page')

    if page is None:
        page = 1
    else:
        page = int(page)

    length = len(blogs)
    blogs = blogs[(page-1)*no_of_posts: page*no_of_posts]

    if page > 1:
        prev = page - 1
    else:
        prev = None
    if page < math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None

    CATID = request.GET.get('category')

    if CATID:
        blogs = Blog.objects.filter(Blog_category=CATID).order_by('-read')

    template_name = "main/blog_home.html"

    context = {
        'blogscat': blogs_category,
        'blogs': blogs,
        'prev': prev, 'nxt': nxt,
        'blogscategory': blogs_category,
        'pop': popular,


    }

    return render(request, template_name, context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    all_comments = BlogComment.objects.filter(blog=blog.id)
    all_blogs = Blog.objects.all().filter(Blog_category=blog.Blog_category)
    # week_ago = datetime.date.today() - datetime.timedelta(days = 7)
    blogs_category = Blog_category.objects.all()

    form = CommentBlogForm()

    if request.method == "POST":
        form = CommentBlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your comment on this blog has been posted")
            return redirect("/blog_detail/"+blog.slug)
    else:
        form = CommentBlogForm()

        blog.read += 1
        blog.save()

    context = {
        'blog': blog,
        'all_blogs': all_blogs,
        'form': form,
        'all_comments': all_comments,
        'blogscat': blogs_category,
    }
    return render(request, "main/blog_detail.html", context)


class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "main/contact_us.html"
    success_url = "/"
    success_message = "Your query has been submited successfully, we will contact you soon."

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "Please submit the form carefully")
        return redirect('home')


class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CreateBlogForm
    def createblog(request):
        if request.method == "POST":
            form = CreateBlogForm(request.POST)
            if form.is_verified():
                form.save()
                messages.success(
                request, "Your comment on this blog has been posted")
            else:
                form = CreateBlogForm()

    template_name = "main/create_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has not been  created now it is on pending"


class UpdateBlogView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Blog
    form_class = UpdateBlogForm
    template_name = "main/update_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has been updated sucessfully"


class DeleteBlogView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Blog
    template_name = "main/delete_blog.html"
    login_url = 'login'
    success_url = "/"
    success_message = "Your blog has been deleted"


def searchdata(request):
    q = request.GET.get('q')
    blogs = Blog.objects.filter(
        Q(name__icontains=q) |
        Q(mini_description__icontains=q)

    ).distinct()

    parms = {
        'blogs': blogs,
        'blogscategory': Blog_category.objects.filter(
            Q(name__icontains=q)

        ).distinct(),

        'title': f'Search Results for {q}',
    }

    return render(request, 'main/blog_home.html', parms)
