from django.shortcuts import render, render_to_response

from models import Persona, Producto, Compra

# Create your views here.

def listarPersona(request):

	if request.GET.get('id'):

		idPersona = request.GET.get('id')

		p = Persona.objects.filter(id=idPersona)


	else:

	  p = Persona.objects.all()

	return render_to_response('persona.html', { 'personas' : p })

def listarProducto(request):

    if request.GET.get('id'):

    	idProducto = request.GET.get('id')

    	p = Producto.objects.filter(id=idProducto)


    	else:

    	  p = Producto.objects.all()

    return render_to_response('producto.html', { 'producto' : p })
