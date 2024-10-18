from django.http import HttpResponse
from django.shortcuts import render


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
    return render(request, 'login/index.html')
