from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password   
from django.db.models import Q
from protoDigital.models import Usuario, Usafa
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
# import requests

# def obter_coordenadas_do_cep(cep):
#     # Substitua com sua chave de API do Google Maps
#     api_key = 'SUA_CHAVE_DE_API_AQUI'
#     url = f'https://maps.googleapis.com/maps/api/geocode/json?address={cep}&key={api_key}'
    
#     response = requests.get(url)
#     data = response.json()
    
#     if data['status'] == 'OK':
#         # Extrai a latitude e longitude do primeiro resultado
#         latitude = data['results'][0]['geometry']['location']['lat']
#         longitude = data['results'][0]['geometry']['location']['lng']
#         return latitude, longitude
#     else:
#         raise ValueError(f"Não foi possível obter as coordenadas para o CEP {cep}.")

# # Função para calcular a distância entre dois pontos (latitude/longitude) em quilômetros ou metros
# def calcular_distancia(lat1, lon1, lat2, lon2, em_km=True):
#     from math import radians, sin, cos, sqrt, atan2
    
#     # Converter as coordenadas de graus para radianos
#     lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
#     # Diferença das latitudes e longitudes
#     dlat = lat2 - lat1
#     dlon = lon2 - lon1
    
#     # Fórmula de Haversine
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
#     # Raio da Terra: 6371 km ou 6371000 metros
#     raio = 6371 if em_km else 6371000  # Raio em metros ou quilômetros
    
#     # Distância
#     distancia = raio * c
#     return distancia

# # Função para buscar a Usafa mais próxima, baseada no CEP do usuário
# def buscar_usafa_mais_proxima(usuario_cep, em_km=True):
#     # Aqui, suponha que você tenha uma função para obter as coordenadas de latitude/longitude a partir do CEP
#     usuario_lat, usuario_lon = obter_coordenadas_do_cep(usuario_cep)  # Supondo que você tenha essa função
    
#     # Inicializa a distância mínima com um valor muito alto (em metros ou km, depende do que você escolher)
#     distancia_minima = float('300')  # Valor inicial muito alto
#     usafa_mais_proxima = None  # Usafa mais próxima, inicialmente sem valor
    
#     # Busca todas as Usafas e calcula a distância
#     for usafa in Usafa.objects.all():
#         distancia = calcular_distancia(usuario_lat, usuario_lon, usafa.latitude, usafa.longitude, em_km)
        
#         # Verifica se a Usafa atual está mais próxima
#         if distancia < distancia_minima:
#             distancia_minima = distancia
#             usafa_mais_proxima = usafa
    
#     # Retorna a Usafa mais próxima e a distância (em km ou metros)
#     return usafa_mais_proxima



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

    usafas = [
        {
            'nome': 'USAFA Aloha',
            'endereco': 'Rua Zenji Sasaki, nº 269 - Nova Mirim',
            'telefone': '3496-5158'
        },
        {
            'nome': 'USAFA Anhanguera',
            'endereco': 'Rua Josefa Alves de Siqueira, nº 648 - Anhanguera',
            'telefone': '3496-5216'
        },
        {
            'nome': 'USAFA Antártica',
            'endereco': 'Av. dos Trabalhadores, nº 3801 - Antártica',
            'telefone': '3496-5246'
        },
        {
            'nome': 'USAFA Aviação',
            'endereco': 'Av. Dr. Roberto de Almeida Vinhas, nº 2929 - Aviação',
            'telefone': '3496-5202'
        },
        {
            'nome': 'USAFA Boqueirão',
            'endereco': 'Av. Pres. Kennedy, nº 918 - Boqueirão',
            'telefone': '3496-5201'
        },
        {
            'nome': 'USAFA Caiçara',
            'endereco': 'Rua Mathilde de Azevedo Setubal, nº 530 - Caiçara',
            'telefone': '3496-5204'
        },
        {
            'nome': 'USAFA Esmeralda',
            'endereco': 'Rua Menotti Del Picchia, altura do nº 179',
            'telefone': '3496-5232'
        },
        {
            'nome': 'USAFA Forte',
            'endereco': 'Av. Rio Branco, nº 562 - Forte',
            'telefone': '3496-5221'
        },
        {
            'nome': 'USAFA Guaramar',
            'endereco': 'Av. dos Trabalhadores, nº 1717 - Glória',
            'telefone': '3496-5210'
        },
        {
            'nome': 'USAFA Guilhermina',
            'endereco': 'Av. Presidente Kennedy, nº 2100 - Guilhermina',
            'telefone': '3496-5200'
        },
        {
            'nome': 'USAFA Melvi',
            'endereco': 'Rua João Caetano, nº 101 - Melvi',
            'telefone': '3496-5264'
        },
        {
            'nome': 'USAFA Mirim I',
            'endereco': 'Av. dos Sindicatos, nº 635 - Mirim',
            'telefone': '3496-5203'
        },
        {
            'nome': 'USAFA Mirim II',
            'endereco': 'Rua Nossa Senhora da Conceição, nº 400 - Mirim',
            'telefone': '3496-5212'
        },
        {
            'nome': 'USAFA Noêmia',
            'endereco': 'Av. Presidente Kennedy, nº 4960 - Tupy',
            'telefone': '3496-5199'
        },
        {
            'nome': 'USAFA Ocian',
            'endereco': 'Rua José Jorge, nº 521 - Ocian',
            'telefone': '3496-5245'
        },
        {
            'nome': 'USAFA Princesa',
            'endereco': 'Rua Vergilio Gabriel de Siqueira, nº 20 - Princesa',
            'telefone': '3496-5166'
        },
        {
            'nome': 'USAFA Quietude',
            'endereco': 'Rua Rui Manoel Sampaio Seabra Pereira, nº 500 - Quietude',
            'telefone': '3496-5208'
        },
        {
            'nome': 'USAFA Real',
            'endereco': 'Rua das Begônias, nº 453 - Real',
            'telefone': '3496-5219'
        },
        {
            'nome': 'USAFA Ribeirópolis',
            'endereco': 'Rua Esmeraldo Tarquínio, nº 471 - Ribeirópolis',
            'telefone': '3496-5265'
        },
        {
            'nome': 'USAFA Rio Branco',
            'endereco': 'Av. Hugo de Carvalho Ramos, nº 1521 - Esmeralda',
            'telefone': '3496-5278'
        },
        {
            'nome': 'USAFA Samambaia',
            'endereco': 'Av. das Araucárias, nº 181 - Samambaia',
            'telefone': '3496-5215'
        },
        {
            'nome': 'USAFA Santa Marina',
            'endereco': 'Rua Clóvis Batista dos Santos, nº 598 - Bairro Anhanguera',
            'telefone': '3496-5159'
        },
        {
            'nome': 'USAFA São Jorge',
            'endereco': 'Av. dos Trabalhadores, nº 4242 - Antártica',
            'telefone': '3496-5211'
        },
        {
            'nome': 'USAFA Solemar',
            'endereco': 'Av. Pres. Kennedy, nº 19726 - Solemar',
            'telefone': '3496-5220'
        },
        {
            'nome': 'USAFA Tude Bastos',
            'endereco': 'Rua Maria Luiza Lavalle, nº 68 - Sítio do Campo',
            'telefone': '3496-5206'
        },
        {
            'nome': 'USAFA Tupi',
            'endereco': 'Rua Meinacós, nº 95 - Tupi',
            'telefone': '3496-5205'
        },
        {
            'nome': 'USAFA Tupiry',
            'endereco': 'Rua Idelfonso Galeano, nº 368 - Tupiry',
            'telefone': '3496-5209'
        },
        {
            'nome': 'USAFA Vila Alice',
            'endereco': 'Rua Renata Câmara Agondi, nº 46 - Anhanguera',
            'telefone': '3496-5217'
        },
        {
            'nome': 'USAFA Vila Sônia',
            'endereco': 'Rua Antônio Cândido da Silva, nº 1075 - Vila Sônia',
            'telefone': '3496-5207'
        }
    ]

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

        # Usa o backend personalizado para autenticação
        user = authenticate(request, cpf=cpf, password=senha)

        if user is not None:
            # Realiza o login se as credenciais forem válidas
            auth_login(request, user)
            return redirect('home')  # Redireciona para a página inicial ou outra página desejada
        else:
            # Caso as credenciais sejam inválidas
            return render(request, 'login/index.html', {'error': 'Credenciais inválidas'})

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
    return render(request, 'Perfil_do_Usuario/index.html')

def Cartao_Virtual(request):
    return render(request,'Cartao_Virtual/index.html')

def Marcar_Consulta(request):
    return render(request,'Marcar_Consulta/index.html')

def Endereco_das_USAFAs(request):
    return render(request,'Endereco_das_USAFAs/index.html')

def Configuracoes(request):
    return render(request,'Configuracoes/index.html')


