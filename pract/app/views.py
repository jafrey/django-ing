from django.shortcuts import render, render_to_response

# Create your views here.

def listarPersona(request):

	if request.GET.get('id'):

		idPersona = request.GET.get('id')

		p = Termo.objects.filter(id=idPersona)


	else:

		t = Persona.objects.all()

	return render_to_response('persona.html', { 'personas' : t })
