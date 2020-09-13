
from django.shortcuts import render

from account.models import Account
# Create your views here.

def home_screen_view(request):
	
	context = {}
	accounts = Account.objects.all()
	context['accounts'] = accounts
	#context['some_string'] = "This is some string that i am passing to the view"
	#context['some_number'] = 210584
	#context = {
			#'some_string': "This is some string that i am passing to the view",
			#'some_number': 210584,
	#}

	#list_of_values = []
	#list_of_values.append("first entry")
	#list_of_values.append("second entry")
	#list_of_values.append("third entry")
	#list_of_values.append("forth entry")
	#context['list_of_values'] = list_of_values

	#questions = Question.objects.all()
	#context['questions'] = questions

	return render(request, "personal/home.html", context)	