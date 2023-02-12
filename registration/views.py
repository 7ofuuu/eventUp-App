from datetime import date
from io import BytesIO

import xlwt
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template, render_to_string
from django.utils import timezone
from django.views.generic import TemplateView
from xhtml2pdf import pisa

from event.models import EventRecord
from student.models import StudentRecord
from .forms import TransactionForm
from .models import RegistrationRecord


# Create your views here.
# noinspection PyBroadException
class RegisterEvent(TemplateView):

    def get(self, request, *args, **kwargs):
        try:
            if not request.user.is_staff and not request.user.is_superuser:
                obj = EventRecord.objects.get(slug=kwargs['slug'])
                t = date.today()
                if obj.membutuhkan_pendaftaran and (obj.tanggal_awal_pendaftaran <= t) and (t <= obj.tanggal_akhir_pendaftaran):
                    try:
                        student = StudentRecord.objects.get(user=request.user)
                    except ObjectDoesNotExist:
                        messages.info(request, 'Fill your personal information before registration')
                        return redirect('home')
                    try:
                        RegistrationRecord.objects.get(student=student, event=obj)
                        msg = str('Already Register in ' + obj.nama_event)
                        messages.warning(request, msg)
                    except ObjectDoesNotExist:
                        obj.registered_student += 1
                        RegistrationRecord.objects.create(student=student, user=request.user, event=obj,
                                                          tema_event=obj.tema_event, tipe_event=obj.tipe_event, balance=obj.biaya)
                        obj.save(update_fields=['registered_student'])
                        msg = str('Successfully Register for ' + obj.nama_event)
                        messages.success(request, msg)
                        current_site = get_current_site(request)
                        mail_subject = 'Anda telah terdaftar di: ' + obj.nama_event
                        message = render_to_string('registration_email.txt', {
                            'user': request.user,
                            'domain': current_site.domain,
                            'event': obj,
                            'email': settings.EMAIL_HOST_USER,
                        })
                        email = EmailMessage(mail_subject, message, to=[request.user.email])
                        email.send()
                        return redirect("account:consolidated_view_all")
                else:
                    messages.info(request, 'Registration Closed/Does not Start/no Registration Required')
            else:
                raise PermissionDenied
            return redirect('event:event_detail', kwargs['slug'])
        except ObjectDoesNotExist:
            messages.error(request, 'Record Not Found')
            return redirect('home')
        except PermissionDenied:
            messages.warning(request, 'You have not Permission to Register')
        except Exception as e:
            messages.error(request, 'Try After Some Time')
            return redirect('home')


# noinspection PyBroadException
class RegistrationDetail(TemplateView):
    template_name = 'registration_detail.html'

    def get(self, request, *args, **kwargs):
        try:
            obj = RegistrationRecord.objects.get(registration_id=kwargs['registration_id'])
            if request.user.is_superuser or request.user == obj.event.user:
                form = TransactionForm()
                return render(request, self.template_name, {'obj': obj, 'form': form, 'staff': True})
            student = StudentRecord.objects.get(user=request.user)
            if student == obj.student:
                return render(request, self.template_name, {'obj': obj, 'staff': False})
            raise PermissionDenied
        except Exception:
            messages.error(request, 'You Does not Permission')
            return redirect('home')

    def post(self, request, **kwargs):
        try:
            obj = RegistrationRecord.objects.get(registration_id=kwargs['registration_id'])
            if request.user.is_superuser or request.user == obj.event.user:
                form = TransactionForm(request.POST)
                if form.is_valid():
                    temp = form.save(commit=False)
                    temp.registration_id = obj.registration_id
                    temp.user = request.user
                    obj.jumlah_pembayaran += temp.jumlah_pembayaran
                    obj.balance -= temp.jumlah_pembayaran
                    temp.save()
                    obj.save(update_fields=['jumlah_pembayaran', 'balance'])
                    obj.transaction_id.add(temp)
                    messages.success(request, 'Successfully Update')
                    return redirect('registration:registration_detail', kwargs['registration_id'])
                else:
                    messages.error(request, 'Invalid Inputs')
                    return render(request, self.template_name, {'obj': obj, 'form': form, 'staff': True})
            else:
                raise PermissionDenied
        except PermissionDenied:
            messages.error(request, 'You Does not Permission')
            return redirect('home')
        except Exception:
            messages.error(request, 'Error, Contact to US')
            return redirect('home')


# noinspection PyBroadException
class RegisterStudentList(TemplateView):
    template_name = 'register_student_list.html'

    def get(self, request, *args, **kwargs):
        try:
            event = EventRecord.objects.get(slug=kwargs['slug'])
            if request.user.is_superuser or request.user == event.user:
                obj = RegistrationRecord.objects.filter(event=event)
                return render(request, self.template_name, {'obj': obj})
            raise PermissionDenied
        except Exception:
            messages.error(request, 'You Does not Permission')
            return redirect('home')


# noinspection PyBroadException
class RegistrationReport(TemplateView):
    template_name = 'report.html'

    def get(self, request, *args, **kwargs):
        try:
            event = EventRecord.objects.get(slug=kwargs['slug'])
            if request.user.is_superuser or request.user == event.user:
                student_list = RegistrationRecord.objects.filter(event=event)
                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = "attachment; filename=Registration Report %s.xls" % event
                wb = xlwt.Workbook(encoding='utf-8')
                ws = wb.add_sheet(event.slug)

                # Sheet header, first row
                font_style_bold = xlwt.XFStyle()
                font_style_bold.font.bold = True

                ws.write_merge(0, 0, 2, 4, 'EventUp SMK Negeri 4 Bandung', font_style_bold)
                ws.write_merge(1, 1, 1, 5, 'Jl. Kliningan No.6, Turangga, Kec. Lengkong, Kota Bandung, Jawa Barat 40264, INDONESIA.')

                ws.write(3, 0, 'Kode Event')
                ws.write(3, 1, event.slug, font_style_bold)
                ws.write(3, 2, 'Nama Event')
                ws.write_merge(3, 3, 3, 4, event.nama_event, font_style_bold)
                ws.write(3, 5, 'Tanggal Event')
                ws.write(3, 6, event.tanggal_event.strftime('%b %d, %Y'), font_style_bold)

                ws.write(4, 0, 'Tema Event')
                ws.write(4, 1, event.tema_event, font_style_bold)
                ws.write(4, 2, 'Nama Kontak Person')
                ws.write_merge(4, 4, 3, 4, event.narahubung, font_style_bold)
                ws.write(4, 5, 'Biaya Event')
                ws.write(4, 6, event.biaya, font_style_bold)

                row_num = 6
                columns = ['No.', 'Id Registrasi', 'Nama Siswa', 'Nomor Induk Siswa', 'Jumlah Pembayaran', 'Sisa Pembayaran', 'Tanggal']
                for col_num in range(len(columns)):
                    ws.write(row_num, col_num, columns[col_num])

                # Sheet body, remaining rows
                for student in student_list:
                    row_num += 1
                    ws.write(row_num, 0, row_num - 6)
                    ws.write(row_num, 1, student.registration_id)
                    ws.write(row_num, 2, student.student.user.first_name + ' ' + student.student.user.last_name)
                    ws.write(row_num, 3, student.student.nis)
                    ws.write(row_num, 4, student.jumlah_pembayaran)
                    ws.write(row_num, 5, student.balance)
                    ws.write(row_num, 6, student.timestamp.strftime('%b %d, %Y'))

                ws.write_merge(row_num + 2, row_num + 2, 0, 3, 'Dicetak pada ' + str(timezone.now()) + ' (GMT)')
                wb.save(response)
                return response
            raise PermissionDenied
        except PermissionDenied:
            messages.error(request, 'You Does not Permission')
            return redirect('home')
        except Exception:
            messages.error(request, 'Something went wrong')
            return redirect('home')


# noinspection PyBroadException
class TransactionReport(TemplateView):
    template_name = 'report.html'

    def get(self, request, *args, **kwargs):
        try:
            event = EventRecord.objects.get(slug=kwargs['slug'])
            if request.user.is_superuser or request.user == event.user:
                student_list = RegistrationRecord.objects.filter(event=event)
                response = HttpResponse(content_type='application/ms-excel')
                response['Content-Disposition'] = "attachment; filename=Transaction Report_%s.xls" % event
                wb = xlwt.Workbook(encoding='utf-8')
                ws = wb.add_sheet(event.slug)

                # Sheet header, first row
                font_style_bold = xlwt.XFStyle()
                font_style_bold.font.bold = True

                ws.write_merge(0, 0, 2, 4, 'EventUp SMK Negeri 4 Bandung', font_style_bold)
                ws.write_merge(1, 1, 1, 5, 'Jl. Kliningan No.6, Turangga, Kec. Lengkong, Kota Bandung, Jawa Barat 40264, INDONESIA.')

                ws.write(3, 0, 'Kode Event')
                ws.write(3, 1, event.slug, font_style_bold)
                ws.write(3, 2, 'Nama Event')
                ws.write_merge(3, 3, 3, 4, event.nama_event, font_style_bold)
                ws.write(3, 5, 'Tanggal Event')
                ws.write(3, 6, event.tanggal_event.strftime('%b %d, %Y'), font_style_bold)

                ws.write(4, 0, 'Tema Event')
                ws.write(4, 1, event.tema_event, font_style_bold)
                ws.write(4, 2, 'Nama Kontak Person')
                ws.write_merge(4, 4, 3, 4, event.narahubung, font_style_bold)
                ws.write(4, 5, 'Biaya Event')
                ws.write(4, 6, event.biaya, font_style_bold)

                row_num = 6
                columns = ['No.', 'No. Kwitansi', 'Nama Siswa', 'Nomor Induk Siswa', 'Jumlah Pembayaran', 'Date', 'User']
                for col_num in range(len(columns)):
                    ws.write(row_num, col_num, columns[col_num], font_style_bold)

                # Sheet body, remaining rows
                for student in student_list:
                    for s in student.transaction_id.all():
                        row_num += 1
                        ws.write(row_num, 0, row_num - 6)
                        ws.write(row_num, 1, student.registration_id)
                        ws.write(row_num, 2, student.student.user.first_name + ' ' + student.student.user.last_name)
                        ws.write(row_num, 3, student.student.nis)
                        ws.write(row_num, 4, s.jumlah_pembayaran)
                        ws.write(row_num, 5, s.timestamp.strftime('%b %d, %Y'))
                        ws.write(row_num, 6, s.user.username)

                ws.write_merge(row_num + 2, row_num + 2, 0, 3, 'Dicetak pada ' + str(timezone.now()) + ' (GMT)')
                wb.save(response)
                return response
            raise PermissionDenied
        except PermissionDenied:
            messages.error(request, 'You Does not Permission')
            return redirect('home')
        except Exception:
            messages.error(request, 'Something went wrong')
            return redirect('home')


# noinspection PyBroadException
class EnrollmentReport(TemplateView):
    template_name = 'report.html'

    def get(self, request, *args, **kwargs):
        try:
            event = EventRecord.objects.get(slug=kwargs['slug'])
            if request.user.is_superuser or request.user == event.user:
                # if event.biaya == 0:
                #     student_list = RegistrationRecord.objects.filter(event=event)
                # else:           
                #     student_list = RegistrationRecord.objects.filter(event=event, balance=event.biaya)
                student_list = RegistrationRecord.objects.filter(event=event)

                template = get_template('report.html')
                html = template.render({'event': event, 'student_list': student_list, 'now': timezone.now()})

                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

                if not pdf.err:
                    response = HttpResponse(result.getvalue(), content_type='application/pdf')
                    # content = "inline; filename='Enrollment Report %s.pdf'" % event
                    content = "attachment; filename=Enrollment Report %s.pdf" % event
                    response['Content-Disposition'] = content
                    return response

                return HttpResponse("Not found")
            raise PermissionDenied
        except PermissionDenied:
            messages.error(request, 'You Does not Permission')
            return redirect('home')
        except Exception:
            messages.error(request, 'Something went wrong')
            return redirect('home')
