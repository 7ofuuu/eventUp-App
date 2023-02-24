from datetime import date

from django.contrib import messages
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from registration.models import RegistrationRecord
from .forms import EventForm
from .models import EventRecord


# Create your views here.
class EventListView(TemplateView):
    template_name = 'event-list.html'

    def get(self, request, *args, **kwargs):
        try:
            tema = 'All'
            if kwargs.get('tema_event'):
                tema = kwargs['tema_event']
                event_list = EventRecord.objects.filter(tema_event=kwargs['tema_event']).order_by('-tanggal_event')
                print('aa')
            else:
                event_list = EventRecord.objects.all().order_by('-tanggal_event')
            return render(request, self.template_name, {'event_list': event_list, 'now': date.today(), 'tema':tema})

        except ObjectDoesNotExist:
            messages.error(request, 'Record Not Found')
            return redirect('home')


# noinspection PyBroadException
class EventDetail(TemplateView):
    template_name = 'event_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            owner = False
            registered = True
            obj = EventRecord.objects.get(slug=kwargs['slug'])
            if obj.user == request.user or request.user.is_superuser:
                owner = True
            else:
                try:
                    RegistrationRecord.objects.get(user=request.user, event=obj)
                except Exception:
                    registered = False
            return render(request, self.template_name,
                          {'obj': obj, 'owner': owner, 'registered': registered, 'now': date.today()})
        except ObjectDoesNotExist:
            messages.error(request, 'Event Tidak Ditemukan')
            return redirect('home')


# noinspection PyBroadException
class AddEvent(TemplateView):
    template_name = 'add_update_event.html'

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_staff:
                form = EventForm()
            else:
                raise PermissionDenied
            return render(request, self.template_name, {'form': form})
        except PermissionDenied:
            messages.error(request, 'Permission Denied')
            return redirect('home')

    def post(self, request):
        if True:
            if request.user.is_staff:
                form = EventForm(request.POST, request.FILES)
                if form.is_valid():
                    temp = form.save(commit=False)
                    temp.user = request.user
                    form.save()
                    messages.success(request, 'Event Sukses Ditambahkan')
                    return redirect('event:event_detail', slug=temp.slug)
                else:
                    messages.error(request, 'Invalid Input')
            else:
                raise PermissionDenied
            return render(request, self.template_name, {'form': form})
        # except Exception:
        #     messages.error(request, 'Permission Denied')
        #     return redirect('home')


# noinspection PyBroadException
class UpdateEvent(TemplateView):
    template_name = 'add_update_event.html'

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_staff or request.user.is_superuser:
                obj = EventRecord.objects.get(slug=kwargs['slug'])
                if obj.user == request.user or request.user.is_superuser:
                    form = EventForm(instance=obj)
                else:
                    raise PermissionDenied
            else:
                raise PermissionDenied
            return render(request, self.template_name, {'form': form})
        except Exception:
            messages.error(request, 'Permission Denied')
            return redirect('home')

    def post(self, request, **kwargs):
        try:
            obj = EventRecord.objects.get(slug=kwargs['slug'])
            f = obj.biaya
            if obj.user == request.user or request.user.is_superuser:
                form = EventForm(request.POST, request.FILES, instance=obj)
                if form.is_valid():
                    fee = form.cleaned_data['biaya']
                    diff = fee - f
                    if diff != 0:
                        student_list = RegistrationRecord.objects.filter(event=obj)
                        for student in student_list:
                            student.balance += diff
                            student.save(update_fields=['balance'])
                    form.save()
                    messages.success(request, 'Event Sukses Diupdate')
                    return redirect('event:event_detail', kwargs['slug'])
                else:
                    messages.error(request, 'Invalid Input')
                return render(request, self.template_name, {'form': form})
            else:
                raise PermissionDenied
        except Exception:
            messages.error(request, 'Permission Denied')
            return redirect('home')


class DeleteEvent(TemplateView):

    def get(self, request, *args, **kwargs):
        try:
            obj = EventRecord.objects.get(slug=kwargs['slug'])
            if str(obj.timestamp) == kwargs['timestamp'] and (obj.user == request.user or request.user.is_superuser):
                if obj.registered_student > 0:
                    raise PermissionDenied('Siswa telah terdaftar, Anda tidak bisa menghapus event ini.')
                obj.delete()
                messages.success(request, 'Event Sukses Dihapus')
            else:
                raise PermissionDenied('Permission Denied')
        except ObjectDoesNotExist:
            messages.error(request, 'Event tidak ditemukan')
            return redirect('home')
        except PermissionDenied as msg:
            messages.warning(request, msg)
            return redirect('account:consolidated_view_all')
