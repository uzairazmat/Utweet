from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.


def mytweet(request):
    return render(request, "websites/mytweet.html")


def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "websites/tweet_list.html", {'tweets': tweets})


@login_required
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form. is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")

    else:
        form = TweetForm()
    return render(request, "websites/tweet_form.html", {'form': form})


@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            redirect("tweet_list")

    else:
        form = TweetForm(instance=tweet)
    return render(request, "websites/tweet_form.html", {"form": form})


@login_required
def delete_tweet(request, tweet_id):

    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, "websites/tweet_confirm_delete.html")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create user but don't save to DB yet
            user = form.save(commit=False)

            # Hash password properly
            user.set_password(form.cleaned_data["password1"])
            user.save()

            # Log the user in
            login(request, user)
            return redirect("tweet_list")
    else:
        form = UserRegistrationForm()

    return render(request, "registration/register.html", {"form": form})


def view_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, "websites/view_tweet.html", {"tweet": tweet})
