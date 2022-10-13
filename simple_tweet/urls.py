from django.urls import path

from simple_tweet.views import TextApiView, TextView

app_name = "simple_tweet"
urlpatterns = [
  path("", TextView.as_view(), name="index"),
  path("api/texts/", TextApiView.as_view(), name="texts")
]