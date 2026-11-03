from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db import transaction, DatabaseError
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Restrict all views to staff members only
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class UserListView(StaffRequiredMixin, ListView):
    model = User
    template_name = 'accounts/users/list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-date_joined')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(username__icontains=q) | queryset.filter(email__icontains=q)
        return queryset


class UserCreateView(StaffRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/users/create.html'
    success_url = reverse_lazy('accounts:user_list')

    def form_valid(self, form):
        try:
            # Transactional Save
            with transaction.atomic():
                response = super().form_valid(form)

            messages.success(self.request, f"User '{self.object.username}' was successfully created.")
            return response
        except DatabaseError as e:
            messages.error(self.request, f"Database Error: Could not save user. Rolled back. Details: {e}")
            return self.form_invalid(form)
        except Exception as e:
            messages.warning(self.request, f"Warning: An error occurred. Rolled back. Details: {e}")
            return self.form_invalid(form)


class UserUpdateView(StaffRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'accounts/users/edit.html'

    def get_success_url(self):
        return reverse_lazy('accounts:user_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        try:
            # Transactional Save
            with transaction.atomic():
                response = super().form_valid(form)

            messages.success(self.request, f"User '{self.object.username}' was successfully updated.")
            return response
        except DatabaseError as e:
            messages.error(self.request, f"Database Error: Could not update user. Rolled back. Details: {e}")
            return self.form_invalid(form)
        except Exception as e:
            messages.warning(self.request, f"Warning: An error occurred. Rolled back. Details: {e}")
            return self.form_invalid(form)


class UserDetailView(StaffRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/users/detail.html'
    context_object_name = 'user_obj'