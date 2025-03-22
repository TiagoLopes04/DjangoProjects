from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome=forms.CharField(label='Nome',max_length=100)
    email=forms.EmailField(label='E-mail',max_length=100)
    assunto=forms.CharField(label='assunto',max_length=100)
    mensagem=forms.CharField(label='mensagem',max_length=300)

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo= f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail=EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@fusion.com.pt',
            to=['contato@fusion.com.pt',],
            headers={'Reply-To': email}
        )
        mail.send()

