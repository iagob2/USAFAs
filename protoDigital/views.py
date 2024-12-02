from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password   
from protoDigital.models import Usuario, Usafa
from django.contrib.auth import authenticate, login
from datetime import timedelta

def home(request):

    # Atendimentos que as USAFAS podem realizar
    atendimentos = [
        {
            'icon': 'assets/icons/Medical team.svg',
            'alt': 'icone medico familia',
            'title': 'Médico da Família e Comunidade:',
            'description': 'Cuidando de você e da sua família com atenção integral à saúde.'
        },
        {
            'icon': 'assets/icons/Stethoscope.svg',
            'alt': 'icone Enfermagem',
            'title': 'Enfermagem:',
            'description': 'Comprometidos com o cuidado, a segurança e o bem-estar do paciente.'
        },
        {
            'icon': 'assets/icons/Newborn.svg',
            'alt': 'icone pré-natal',
            'title': 'Pré-Natal e Puerpério:',
            'description': 'Acompanhando e apoiando você em cada etapa da gravidez e além.'
        },
        {
            'icon': 'assets/icons/Children.svg',
            'alt': 'icone Puericultura',
            'title': 'Puericultura:',
            'description': 'Cuidando da saúde e do desenvolvimento das crianças, desde o nascimento.'
        },
        {
            'icon': 'assets/icons/Tooth.svg',
            'alt': 'icone Ondologia',
            'title': 'Odontologia:',
            'description': 'Cuidando do seu sorriso e da sua saúde bucal com excelência.'
        },
        {
            'icon': 'assets/icons/Doctor.svg',
            'alt': 'icone Hiperdia',
            'title': 'Hiperdia:',
            'description': 'Controle e acompanhamento para hipertensos e diabéticos, promovendo saúde e bem-estar.'
        },
        {
            'icon': 'assets/icons/Baby head with a small heart outline.svg',
            'alt': 'icone Teste de gravidez',
            'title': 'Teste de gravidez:',
            'description': 'Oferecendo resultados rápidos e confiáveis para o início de uma nova jornada.'
        },
        {
            'icon': 'assets/icons/Family.svg',
            'alt': 'icone Planejamento familiar',
            'title': 'Planejamento familiar:',
            'description': 'Apoio e orientação para decisões conscientes sobre o futuro da sua família.'
        },
        {
            'icon': 'assets/icons/Medical sign.svg',
            'alt': 'icone Preventivo',
            'title': 'Preventivo:',
            'description': 'Prevenção é o primeiro passo para uma vida mais saudável.'
        },
        {
            'icon': 'assets/icons/Protection.svg',
            'alt': 'icone Curativo',
            'title': 'Curativo:',
            'description': 'Cuidando de você, com segurança e atenção em cada etapa da recuperação.'
        },
        {
            'icon': 'assets/icons/Medical.svg',
            'alt': 'icone Vacinação',
            'title': 'Vacinação:',
            'description': 'Proteção para você e sua família através da imunização.'
        }
    ]

    usafas = Usafa.objects.all()
    
    context = {
        'atendimentos': atendimentos,
        'usafas': usafas
    }

    return render(request, 'home/index.html', context)


def login(request):
    if request.method == 'POST':
        # Pega os dados do formulário
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        
        try:
            # Busca o usuário pelo CPF
            user = Usuario.objects.get(CPF=cpf)
            if check_password(senha, user.senha):

                request.session['user_id'] = user.id_usuario
                request.session.set_expiry(timedelta(minutes=30))
                # Realiza o login se as credenciais forem válidas
                return redirect('perfil_do_usuario')  # Redireciona para a página inicial ou outra página desejada
            else:
                # Caso as credenciais sejam inválidas
                print("Credenciais inválidas")
                return render(request, 'login/index.html')
        except Usuario.DoesNotExist:
            # Caso o usuário não seja encontrado
            return render(request, 'login/index.html')

    return render(request, 'login/index.html')


def Registro(request):
    if request.method == "POST":
        try:
            # usafa = buscar_usafa_por_cep_proximo(request.POST.get("cep"))
            usafa_instance = Usafa.objects.get(id_usafa=1)
            # Captura dos dados enviados pelo formulário
            cpf = request.POST.get("cpf")
            rg = request.POST.get("rg")
            senha = request.POST.get("password")
            nome_usuario = request.POST.get("full_name")
            email = request.POST.get("email")
            data_nascimento = request.POST.get("birth_date")
            telefone = request.POST.get("phone")
            cep = request.POST.get("cep")
            rua = request.POST.get("street")
            numero = request.POST.get("number")
            complemento = request.POST.get("complement")
            bairro = request.POST.get("neighborhood")
            cidade = request.POST.get("city")
            estado = request.POST.get("state")
            status = "ativo"

            

            # Validar as senhas
            if senha != request.POST.get("confirm_password"):
                messages.error(request, "As senhas não coincidem!")
                return render(request, "Registro/index.html")

            # Criptografar a senha
            senha_criptografada = make_password(senha)

            # Criar e salvar o usuário
            usuario = Usuario.objects.create(
                CPF=cpf,
                RG=rg,
                senha=senha_criptografada,
                nome_usuario = nome_usuario,
                email=email,
                telefone=telefone,
                data_nascimento=data_nascimento,
                CEP=cep,
                endereco_usuario_rua=rua,
                endereco_usuario_numero=numero,
                endereco_usuario_complemento=complemento,
                endereco_usuario_bairro=bairro,
                endereco_usuario_cidade=cidade,
                endereco_usuario_estado=estado,
                status=status,
                usafa=usafa_instance

            )
            usuario.save()

            # Mensagem de sucesso e redirecionamento
            messages.success(request, "Registro realizado com sucesso! Faça login.")
            return redirect("login")

        except Exception as e:
            # Exibir o erro no terminal e mostrar mensagem genérica ao usuário
            print("Erro ao registrar o usuário:", e)
            messages.error(request, "Ocorreu um erro ao tentar registrar. Tente novamente.")

    # Renderizar a página de registro para método GET
    return render(request, "Registro/index.html")


def Perfil_do_Usuario(request):
    user_id = request.session.get('user_id')
    if user_id:
        return render(request, 'Perfil_do_Usuario/index.html')
    else:
        return redirect('login')

def Cartao_Virtual(request):
    user_id = request.session.get('user_id')
    if user_id:
        return render(request,'Cartao_Virtual/index.html')
    else:
        return redirect('login')

def Marcar_Consulta(request):
    user_id = request.session.get('user_id')
    if user_id:
        return render(request,'Marcar_Consulta/index.html')
    else:
        return redirect('login')

def Endereco_das_USAFAs(request):
    user_id = request.session.get('user_id')
    if user_id:
        return render(request,'Endereco_das_USAFAs/index.html')
    else:
        return redirect('login')
def Configuracoes(request):
    user_id = request.session.get('user_id')
    if user_id:
        return render(request,'Configuracoes/index.html')
    else:
        return redirect('login')


