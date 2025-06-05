from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mensaje
from .forms import MensajeForm
from django.db.models import Q, Max

@login_required
def inbox_view(request):
    # Obtener usuarios con los que el usuario actual ha tenido conversaciones
    # Se agrupa por el otro participante y se anota la fecha del último mensaje para ordenar
    conversaciones = Mensaje.objects.filter(
        Q(emisor=request.user) | Q(receptor=request.user)
    ).values(
        'emisor', 'receptor' # Agrupar por la combinación emisor-receptor
    ).annotate(
        ultimo_timestamp=Max('timestamp') # Obtener el timestamp del último mensaje en la "conversación"
    ).order_by('-ultimo_timestamp')

    # Procesar para obtener una lista única de 'otros usuarios' y el último mensaje
    otros_usuarios_con_ultimo_mensaje = []
    usuarios_procesados = set()

    for conv in conversaciones:
        otro_usuario_id = conv['emisor'] if conv['receptor'] == request.user.id else conv['receptor']
        
        if otro_usuario_id not in usuarios_procesados:
            try:
                otro_usuario = User.objects.get(id=otro_usuario_id)
                # Obtener el último mensaje real para mostrarlo (opcional)
                ultimo_mensaje = Mensaje.objects.filter(
                    (Q(emisor=request.user, receptor=otro_usuario) | Q(emisor=otro_usuario, receptor=request.user))
                ).latest('timestamp')

                no_leidos = Mensaje.objects.filter(emisor=otro_usuario, receptor=request.user, leido=False).count()

                otros_usuarios_con_ultimo_mensaje.append({
                    'usuario': otro_usuario,
                    'ultimo_mensaje': ultimo_mensaje,
                    'no_leidos': no_leidos,
                    'timestamp_orden': conv['ultimo_timestamp'] # Usar el timestamp anotado para el orden
                })
                usuarios_procesados.add(otro_usuario_id)
            except User.DoesNotExist:
                continue # El usuario pudo haber sido eliminado
    
    # Re-ordenar por el timestamp_orden que ya obtuvimos
    otros_usuarios_con_ultimo_mensaje.sort(key=lambda x: x['timestamp_orden'], reverse=True)


    return render(request, 'mensajes/inbox.html', {'conversaciones': otros_usuarios_con_ultimo_mensaje})

@login_required
def chat_view(request, username_receptor):
    receptor = get_object_or_404(User, username=username_receptor)
    mensajes = Mensaje.objects.filter(
        (Q(emisor=request.user) & Q(receptor=receptor)) |
        (Q(emisor=receptor) & Q(receptor=request.user))
    ).order_by('timestamp')

    # Marcar mensajes como leídos
    Mensaje.objects.filter(emisor=receptor, receptor=request.user, leido=False).update(leido=True)

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.receptor = receptor
            mensaje.save()
            return redirect('chat_view', username_receptor=receptor.username)
    else:
        form = MensajeForm()

    return render(request, 'mensajes/chat_view.html', {
        'receptor': receptor,
        'mensajes': mensajes,
        'form': form
    })

@login_required
def start_chat_view(request):
    users = User.objects.exclude(pk=request.user.pk).exclude(is_staff=True).order_by('username') # Excluir al propio usuario y staff
    return render(request, 'mensajes/start_chat.html', {'users': users})