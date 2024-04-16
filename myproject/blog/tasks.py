from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Post

@shared_task
def send_post_notification(email, title):
    subject = 'New post!'
    message = f'Check out this new post on our blog {title}'
    email_from = 'no-reply@gmail.com'
    recipent_list = [email,]
    send_mail(subject, message, email_from, recipent_list)


@shared_task
def daily_post_summary(email):
    now = timezone.now()
    start_time = now - timedelta(hours=24)
    recent_posts = Post.objects.filter(created_at__gte=start_time)

    if recent_posts.exists():
        subject = 'Daily Post Summary'
        message = 'Here is the summary of posts created in the last 24 hours:\n\n'
        message += '\n'.join(f"Title: {post.title}, Created at: {post.created_at.strftime('%Y-%m-%d %H:%M')}" for post in recent_posts)
        send_mail(subject, message, 'from@example.com', [email])
    else:
        print("No posts were created in the last 24 hours.")

@shared_task
def hourly_comment_summary(email):
    posts = Post.objects.annotate(comments_count=Count('comments')).filter(comments_count__gt=10)
    posts_titles = [post.title for post in posts]
    print("Posts with more than 10 comments:")
    for title in posts_titles:
        print(title)