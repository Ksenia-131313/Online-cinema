from django.urls import path


from . import views



urlpatterns = [
    path('subscription', views.SubscriptionView.as_view(), name='subscription'),

    path("<slug:slug>", views.SubscroptionDetailView.as_view(), name="subscriptions_detail"),
    path("add/", views.add_paysubs_view, name="add_pay"),  # СДЕЛАТЬ ФОРМУ ПОДПИСОК НА ОСНОВЕ ОТЗЫВОВ!
]
# path('subscription', views.SubsDetail.as_view(), name='subscription'), 
# path('subscription', views.subscription_all, name='subscription'),
