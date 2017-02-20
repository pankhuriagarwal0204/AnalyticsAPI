from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import models
from widget_reports import Widgets


class MorchaDayView(viewsets.ViewSet):
    def retrieve(self, request, pk=None, date=None):
        self.widgets = Widgets(date=date, pk=pk, level='morcha', timespan='day')
        error, message = self.widgets.check_object_exists()
        if error:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = self.widgets.get_unit_report()
            return Response(data)


class MorchaWeekView(viewsets.ViewSet):
    def retrieve(self, request, pk=None, date=None):
        self.widgets = Widgets(date=date, pk=pk, level='morcha', timespan='week')
        error, message = self.widgets.check_object_exists()
        if error:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'weaksignal': self.widgets.get_weaksignal_count(object=True),
                'offline': self.widgets.get_offline_count_and_duration(object=True),
                'backup': self.widgets.get_backup_count_and_duration(object=True),
                'report': self.widgets.get_unit_report()
            })


class MorchaMonthView(viewsets.ViewSet):
    def retrieve(self, request, pk=None, date=None):
        self.widgets = Widgets(date=date, pk=pk, level='morcha', timespan='month')
        error, message = self.widgets.check_object_exists()
        if error:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'weaksignal': self.widgets.get_weaksignal_count(object=True),
                'offline': self.widgets.get_offline_count_and_duration(object=True),
                'backup': self.widgets.get_backup_count_and_duration(object=True),
                'report': self.widgets.get_unit_report()
            })


class PostDayView(viewsets.ViewSet):
    def retrieve(self, request, pk=None, date=None):
        self.widgets = Widgets(date=date, pk=pk, level='post', timespan='day')
        error, message = self.widgets.check_object_exists()
        if error:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = self.widgets.get_unit_report()
            return Response(data)


class PostWeekView(viewsets.ViewSet):
    def retrieve(self, request, pk=None, date=None):
        self.widgets = Widgets(date=date, pk=pk, level='post', timespan='week')
        error, message = self.widgets.check_object_exists()
        if error:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = self.widgets.get_unit_report()
            return Response(data)


class PostMonthView(viewsets.ViewSet):
    def retrieve(self, request, pk=None, date=None):
        self.widgets = Widgets(date=date, pk=pk, level='post', timespan='month')
        error, message = self.widgets.check_object_exists()
        if error:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = self.widgets.get_unit_report()
        return Response(data)


class BattalionLiveView(viewsets.ViewSet):
    def retrieve(self, request, pk=None, date=None):
        self.widgets = Widgets(date=date, pk=pk, level='battalion', timespan='live')
        error, message = self.widgets.check_object_exists()
        if error:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
           return Response('found')


class PostLiveView(viewsets.ViewSet):
    def retrieve(self, request, pk=None, date=None):
        self.widgets = Widgets(date=date, pk=pk, level='post', timespan='live')
        error, message = self.widgets.check_object_exists()
        if error:
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        else:
            #self.widgets.get_total_devices()
            return Response('found')

