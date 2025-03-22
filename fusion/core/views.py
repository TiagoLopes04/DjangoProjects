from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Servico,Colaborador
from .forms import ContatoForm
from django.contrib import messages

class indexView(FormView):
    template_name = 'index.html'

    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context= super(indexView,self).get_context_data(**kwargs)
        context['servicos']=Servico.objects.order_by('servico').all()
        context['colaboradores']=Colaborador.objects.order_by('nome').all()
        return context

    def form_valid(self, form,*args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super(indexView,self).form_valid(form,*args,**kwargs)

    def form_invalid(self,form,*args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o email!')
        return super(indexView,self.request).form_invalid(form,*args,**kwargs)
