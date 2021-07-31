from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import MemberBlogForm
from .models import MemberBlog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from fitness_for_all.decorators import full_membership_check

# Create your views here.

@login_required
@full_membership_check
def member_blog(request):
    """ Add a blog  """

    member_blogs = MemberBlog.objects.all()

    template = 'member_blog/member_blog.html'
    context = {
        'member_blogs': member_blogs,
    }

    return render(request, template, context)


@login_required
@full_membership_check
def add_blog(request):
    """ Add a blog  """

    if request.method == 'POST':
        form = MemberBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added blog!')
            return redirect(reverse('member_blog'))
        else:
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
    else:
                # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            user = request.user
            form = MemberBlogForm(initial={
                'user': user,
            })
        else:
            form = MemberBlogForm()             

    member_blogs = MemberBlog.objects.all()
        
    template = 'member_blog/add_blog.html'
    context = {
        'form': form,
        'member_blogs': member_blogs,
    }

    return render(request, template, context)