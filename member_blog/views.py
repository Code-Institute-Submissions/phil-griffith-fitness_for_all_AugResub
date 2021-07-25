from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import MemberBlogForm
from django.contrib import messages

# Create your views here.

def member_blog(request):
    """ Add a blog  """

    return render(request, 'member_blog/member_blog.html')


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
        
    template = 'member_blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)