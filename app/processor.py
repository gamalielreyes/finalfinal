from .models import respuesta, comentario, post

def user_respuesta(request):
	r = respuesta.objects.all().order_by('fecharespuesta')
	context = {'Resp':r}
	return context

def user_post(request):
	p = post.objects.all().order_by('-Fecha_post')
	ctx = {'Post':p}
	return ctx

def user_comment(request):
	p = comentario.objects.all().order_by('fechacomment')
	ctx = {'Comment':p}
	return ctx