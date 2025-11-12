# Legal templates and petition models for medical malpractice cases

def get_petition_templates():
    """
    Returns templates for legal petitions related to medical malpractice
    
    Returns:
        dict: Dictionary containing various petition templates
    """
    templates = {
        "initial_petition": {
            "title": "Petição Inicial - Ação de Indenização por Erro Médico",
            "content": """
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA ____ VARA CÍVEL DA COMARCA DE _____________.

[NOME COMPLETO], [nacionalidade], [estado civil], [profissão], portador(a) do RG nº [...], inscrito(a) no CPF sob nº [...], residente e domiciliado(a) na [endereço completo], por seu advogado que esta subscreve (procuração anexa), com escritório na [endereço completo], onde recebe intimações, vem, respeitosamente, à presença de Vossa Excelência, propor a presente

AÇÃO DE INDENIZAÇÃO POR DANOS MORAIS, MATERIAIS E ESTÉTICOS

em face de [NOME COMPLETO DO MÉDICO], [nacionalidade], [profissão], inscrito(a) no CRM-[UF] sob nº [...], com endereço profissional na [endereço completo], e [HOSPITAL/CLÍNICA], pessoa jurídica de direito privado, inscrita no CNPJ sob nº [...], com sede na [endereço completo], pelos fatos e fundamentos que passa a expor:

I - DOS FATOS
1. O(A) Autor(a) foi submetido(a) a procedimento [especificar], realizado pelo primeiro Réu nas dependências do segundo Réu, em [data].

2. [Descrever detalhadamente como ocorreu o erro médico, mencionando os sintomas apresentados pelo paciente, o diagnóstico realizado, o procedimento adotado e quais foram as falhas cometidas pelo profissional].

3. Em razão do erro médico, o(a) Autor(a) sofreu as seguintes lesões e danos: [descrever detalhadamente as consequências físicas, estéticas, psicológicas e financeiras decorrentes do erro].

4. A falha na prestação do serviço está documentalmente comprovada pelo laudo do Dr. [nome do médico], especialista em [especialidade], que atesta que o procedimento realizado pelo Réu não observou as técnicas adequadas e a boa prática médica (doc. anexo).

II - DO DIREITO
5. A responsabilidade civil do médico está fundamentada no art. 951 do Código Civil, que estabelece a obrigação de indenizar quando, no exercício da profissão, por negligência, imprudência ou imperícia, causar dano ao paciente.

6. No presente caso, restou caracterizada a [negligência/imprudência/imperícia] do primeiro Réu, que [explicar qual foi a conduta inadequada].

7. Quanto ao segundo Réu, sua responsabilidade é objetiva, nos termos do art. 14 do Código de Defesa do Consumidor, respondendo solidariamente pelos danos causados ao paciente.

8. Os danos morais são evidentes diante do sofrimento físico e psicológico experimentado pelo(a) Autor(a), que [descrever o abalo psicológico].

9. Os danos estéticos decorrem de [descrever as sequelas estéticas], que causam constrangimento permanente ao(à) Autor(a) e afetam suas relações sociais e profissionais.

10. Os danos materiais compreendem todas as despesas médicas e hospitalares necessárias para [descrever o tratamento], conforme comprovantes anexos, totalizando R$ [valor].

11. Além disso, o(a) Autor(a) ficou impossibilitado(a) de exercer suas atividades profissionais por [período], deixando de auferir renda mensal de R$ [valor], o que totaliza R$ [valor] a título de lucros cessantes.

III - DOS PEDIDOS
Diante do exposto, requer:

a) A citação dos Réus para, querendo, contestarem a presente ação, sob pena de revelia;

b) A condenação solidária dos Réus ao pagamento de indenização por danos morais no valor de R$ [valor], ou outro valor a ser arbitrado por Vossa Excelência;

c) A condenação solidária dos Réus ao pagamento de indenização por danos estéticos no valor de R$ [valor], ou outro valor a ser arbitrado por Vossa Excelência;

d) A condenação solidária dos Réus ao pagamento de indenização por danos materiais no valor de R$ [valor], referente às despesas médicas e hospitalares já realizadas, conforme documentos anexos;

e) A condenação solidária dos Réus ao pagamento de indenização por lucros cessantes no valor de R$ [valor], correspondente ao período em que o(a) Autor(a) ficou impossibilitado(a) de exercer suas atividades profissionais;

f) A condenação dos Réus ao pagamento das despesas processuais e honorários advocatícios, estes fixados em 20% sobre o valor da condenação;

g) A produção de todas as provas em direito admitidas, especialmente pericial, documental e testemunhal.

Dá-se à causa o valor de R$ [valor].

Termos em que pede deferimento.
[Local], [data].

[Nome do Advogado]
OAB/[UF] [número]
            """
        },
        "extrajudicial_notification": {
            "title": "Notificação Extrajudicial",
            "content": """
NOTIFICAÇÃO EXTRAJUDICIAL

Notificante: [NOME COMPLETO], [nacionalidade], [estado civil], [profissão], portador(a) do RG nº [...], inscrito(a) no CPF sob nº [...], residente e domiciliado(a) na [endereço completo].

Notificado: [NOME DO MÉDICO/HOSPITAL], [dados de identificação], com endereço na [endereço completo].

Prezado(a) Senhor(a),

Venho, por meio desta, NOTIFICAR formalmente V.Sa. sobre [descrever resumidamente o erro médico ocorrido], em [data], que resultou em [descrever os danos sofridos pelo paciente].

Conforme documentação médica em meu poder e parecer técnico elaborado pelo Dr. [nome do médico], o procedimento realizado não seguiu os protocolos técnicos adequados, caracterizando [negligência/imprudência/imperícia] médica.

Diante disso, SOLICITO formalmente:

1. Acesso integral ao prontuário médico, incluindo todos os exames, laudos e anotações referentes ao atendimento prestado;

2. Ressarcimento integral das despesas médicas e hospitalares suportadas até o momento, no valor de R$ [valor], conforme comprovantes que podem ser apresentados;

3. Cobertura dos tratamentos necessários para a recuperação completa das lesões sofridas;

4. Indenização pelos danos morais e estéticos sofridos, sugerindo-se o valor de R$ [valor].

Estou aberto(a) a uma solução amigável para a presente questão e me coloco à disposição para agendamento de reunião com este objetivo, através do telefone [número] ou e-mail [endereço eletrônico].

Solicito manifestação no prazo de 15 (quinze) dias, a contar do recebimento desta notificação, sob pena de serem tomadas as medidas judiciais cabíveis.

[Local], [data].

[Nome do Notificante ou de seu Advogado]
[OAB/UF, se aplicável]
            """
        },
        "expert_examination_request": {
            "title": "Requerimento de Perícia Médica",
            "content": """
EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA ____ VARA CÍVEL DA COMARCA DE _____________.

Processo nº [número do processo]

[NOME COMPLETO], já qualificado nos autos do processo em epígrafe, que move em face de [NOME DO RÉU], por seu advogado, vem, respeitosamente, à presença de Vossa Excelência, requerer a PRODUÇÃO DE PROVA PERICIAL MÉDICA, pelos seguintes fundamentos:

1. Conforme narrado na petição inicial, o autor foi vítima de erro médico durante [procedimento], realizado pelo réu em [data], que resultou em [descrever as lesões].

2. Para a adequada apuração da existência de negligência, imprudência ou imperícia na conduta do réu, bem como para a quantificação precisa dos danos sofridos, é imprescindível a realização de perícia médica especializada.

3. Requer-se que a perícia seja realizada por profissional com especialização em [especialidade médica relacionada ao caso], dado o caráter técnico específico das questões envolvidas.

4. Para tanto, sugere os seguintes quesitos a serem respondidos pelo expert:

a) O procedimento realizado pelo réu seguiu os protocolos técnicos e diretrizes médicas aplicáveis ao caso?

b) Houve falha técnica na execução do procedimento? Qual?

c) O paciente foi devidamente informado sobre os riscos do procedimento?

d) As complicações apresentadas pelo autor são decorrentes de erro na conduta médica ou são riscos inerentes ao procedimento?

e) Quais as sequelas permanentes resultantes do procedimento?

f) As sequelas apresentadas pelo autor causam incapacidade laboral? Em que grau?

g) Quais tratamentos são necessários para a recuperação do autor e qual o custo estimado?

h) As sequelas apresentadas pelo autor causam dano estético? Em que grau (leve, moderado, grave ou gravíssimo)?

Desde já, indica como assistente técnico o Dr. [nome completo], [especialidade], com endereço na [endereço completo], telefone [número] e e-mail [endereço eletrônico].

Termos em que pede deferimento.
[Local], [data].

[Nome do Advogado]
OAB/[UF] [número]
            """
        },
        "settlement_agreement": {
            "title": "Termo de Acordo Extrajudicial",
            "content": """
TERMO DE ACORDO EXTRAJUDICIAL

Pelo presente instrumento particular,

De um lado,

[NOME COMPLETO], [nacionalidade], [estado civil], [profissão], portador(a) do RG nº [...], inscrito(a) no CPF sob nº [...], residente e domiciliado(a) na [endereço completo], doravante denominado(a) PRIMEIRO ACORDANTE;

E de outro lado,

[NOME DO MÉDICO/HOSPITAL], [dados de identificação], com endereço na [endereço completo], doravante denominado SEGUNDO ACORDANTE;

Têm entre si justo e acordado o que segue:

CLÁUSULA PRIMEIRA - DO OBJETO
O presente acordo tem por objeto pôr fim à controvérsia existente entre as partes, relativa ao alegado erro médico ocorrido em [data], durante [procedimento], que resultou em [descrever os danos].

CLÁUSULA SEGUNDA - DAS OBRIGAÇÕES DO SEGUNDO ACORDANTE
O SEGUNDO ACORDANTE se compromete a:

2.1. Pagar ao PRIMEIRO ACORDANTE o valor de R$ [valor] (valor por extenso), a título de indenização por danos morais, materiais e estéticos, mediante [forma de pagamento e prazo];

2.2. Custear o tratamento médico necessário para a recuperação do PRIMEIRO ACORDANTE, conforme prescrição médica, pelo período de [prazo], limitado ao valor máximo de R$ [valor];

2.3. [Outras obrigações específicas conforme o caso].

CLÁUSULA TERCEIRA - DAS OBRIGAÇÕES DO PRIMEIRO ACORDANTE
Em contrapartida, o PRIMEIRO ACORDANTE se compromete a:

3.1. Dar plena, geral, irrevogável e irretratável quitação quanto aos danos decorrentes do evento descrito na Cláusula Primeira, para nada mais reclamar, seja a que título for;

3.2. Desistir de eventual ação judicial já proposta, arcando com os honorários de seu advogado;

3.3. [Outras obrigações específicas conforme o caso].

CLÁUSULA QUARTA - DA CONFIDENCIALIDADE
As partes se comprometem a manter em sigilo os termos do presente acordo, não o divulgando a terceiros, exceto por exigência legal ou para fins de execução do mesmo.

CLÁUSULA QUINTA - DO DESCUMPRIMENTO
O descumprimento de qualquer das cláusulas deste acordo implicará no pagamento de multa no valor de [valor ou percentual] em favor da parte prejudicada, sem prejuízo do cumprimento da obrigação principal e de eventuais perdas e danos suplementares.

CLÁUSULA SEXTA - DISPOSIÇÕES FINAIS
6.1. O presente acordo não implica em reconhecimento de culpa ou responsabilidade por parte do SEGUNDO ACORDANTE.

6.2. As partes declaram que o presente acordo foi celebrado de forma livre e consciente, sem qualquer vício de consentimento.

E, por estarem justos e acordados, assinam o presente instrumento em 2 (duas) vias de igual teor e forma, na presença das testemunhas abaixo.

[Local], [data].

________________________________
[NOME DO PRIMEIRO ACORDANTE]

________________________________
[NOME DO SEGUNDO ACORDANTE]

Testemunhas:

1. ________________________________
Nome:
CPF:

2. ________________________________
Nome:
CPF:
            """
        },
        "medical_records_request": {
            "title": "Requerimento de Prontuário Médico",
            "content": """
REQUERIMENTO DE PRONTUÁRIO MÉDICO

À [Nome do Hospital/Clínica]
A/C: Diretor Clínico / Setor de Prontuários

Eu, [NOME COMPLETO], [nacionalidade], [estado civil], [profissão], portador(a) do RG nº [...], inscrito(a) no CPF sob nº [...], residente e domiciliado(a) na [endereço completo], venho, respeitosamente, REQUERER o fornecimento de CÓPIA INTEGRAL DE MEU PRONTUÁRIO MÉDICO, incluindo:

1. Todas as fichas de atendimento, consultas e internações;
2. Relatórios médicos completos;
3. Resultados de exames realizados;
4. Prescrições médicas;
5. Descrições cirúrgicas;
6. Registros de enfermagem;
7. Relatórios de anestesia;
8. Imagens de exames (tomografias, radiografias, ultrassonografias, etc.);
9. Evolução clínica diária;
10. Outros documentos relacionados ao meu atendimento.

O referido prontuário se refere ao período de [data inicial] a [data final], quando fui atendido pelo(a) Dr(a). [nome do médico].

Fundamento este pedido no direito garantido pela Lei nº 13.787/2018, pela Resolução CFM nº 1.821/2007 e pelo art. 5º, inciso XXXIV, alínea "b" da Constituição Federal, além do disposto no Código de Ética Médica.

Para tanto, apresento em anexo:
- Cópia do documento de identidade;
- [Outros documentos que comprovem a condição de paciente, se necessário].

Solicito que o prontuário seja disponibilizado no prazo legal de até 15 (quinze) dias, conforme disposto na Lei nº 12.527/2011 (Lei de Acesso à Informação).

[Local], [data].

________________________________
[NOME DO REQUERENTE]

Contatos:
Telefone: [número]
E-mail: [endereço eletrônico]
            """
        }
    }
    
    return templates
