from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from sesame.utils import get_query_string

from ..forms import EmailForm


class HomeView(generic.TemplateView):
    template_name = "app/home.html"


class EmailLoginView(generic.FormView):
    template_name = "registration/login.html"
    form_class = EmailForm

    def get_user(self, email: str):
        User = get_user_model()
        user = User.objects.filter(email__iexact=email).first()

        return user

    def create_link(self, user):
        link = reverse("login")
        link += get_query_string(user)

        return link

    def send_email(self, user, link):
        user.email_user(
            subject="[CRM] Log into our App",
            message=f"""\
            Hello,

            You requested that we send you a link to log into our app:

            {link}

            Thank you!
            """,
        )

    def email_submitted(self, email: str):
        user = self.get_user(email)
        if user is None:
            return
        link = self.create_link(user)
        self.send_email(user, link)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        self.email_submitted(email)

        return render(self.request, "registration/email_login_success.html")
