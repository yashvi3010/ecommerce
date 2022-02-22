from dataclasses import fields
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Ticket
# Create your views here.

class CreateTicket(CreateView):
    model = Ticket
    template_name = "ticket/create_ticket.html"
    fields = ['ticket_title', 'ticket_description']
    success_url = '/ticket/view/'


