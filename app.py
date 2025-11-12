import streamlit as st
import base64
from io import BytesIO
from utils.pdf_generator import generate_pdf
from content.chapters_new import ebook_content
from content.templates import get_petition_templates
from assets.images import get_image_urls, get_cover_image, get_author_image
from content.sample_images import get_placeholder_image_dict
from assets.logo import get_medindeniz_logo_svg, get_medindeniz_about

# ========== CONFIGURAÇÃO PRINCIPAL ==========
st.set_page_config(
    page_title="E-book Premium: Indenização por Erro Médico",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="auto"
)

# ========== CSS SUPER FORÇADO PARA TEMA CLARO ==========
st.markdown("""
<style>
    /* RESET COMPLETO - FORÇAR TEMA CLARO */
    .stApp {
        background-color: white !important;
        color: black !important;
    }
    
    /* CORRIGIR TODOS OS TEXTOS */
    body, h1, h2, h3, h4, h5, h6, p, div, span, li, td, th, label {
        color: #000000 !important;
    }
    
    /* CORRIGIR BARRA LATERAL */
    section[data-testid="stSidebar"] {
        background-color: white !important;
        color: black !important;
    }
    
    .css-1d391kg, .sidebar .sidebar-content {
        background-color: white !important;
        color: black !important;
    }
    
    /* CORRIGIR CARDS E CONTAINERS */
    .card-container {
        background-color: #F8F9FA !important;
        color: black !important;
        border: 1px solid #dee2e6 !important;
        border-radius: 10px !important;
        padding: 1.5rem !important;
        margin-bottom: 1.5rem !important;
    }
    
    .blue-container {
        background-color: #E3F2FD !important;
        color: black !important;
        border-left: 5px solid #1E64C8 !important;
        padding: 1rem !important;
        margin-bottom: 1.5rem !important;
    }
    
    .yellow-container {
        background-color: #FFFDE7 !important;
        color: black !important;
        border-left: 5px solid #FFB200 !important;
        padding: 1rem !important;
        margin-bottom: 1.5rem !important;
    }
    
    /* CORRIGIR INPUTS */
    .stTextInput input, .stPassword input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ced4da !important;
    }
    
    /* CORRIGIR BOTÕES */
    .stButton button {
        background-color: #1E64C8 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
    }
    
    /* CORRIGIR SELECT BOX */
    .stSelectbox div[data-baseweb="select"] {
        background-color: white !important;
        color: black !important;
    }
    
    /* CORRIGIR RADIO BUTTONS */
    .stRadio div {
        background-color: white !important;
        color: black !important;
    }
    
    /* CORRIGIR TODOS OS ELEMENTOS STREAMLIT */
    .main .block-container {
        background-color: white !important;
        color: black !important;
    }
    
    /* GARANTIR QUE TUDO SEJA VISÍVEL */
    * {
        color: #000000 !important;
    }
    
    /* ESTILOS ESPECÍFICOS DO SEU EBOOK */
    .main-header {
        font-size: 2.5rem;
        color: #1E64C8 !important;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4A4A4A !important;
        text-align: center;
        margin-top: 0;
    }
    .chapter-title {
        font-size: 1.8rem;
        color: #1E64C8 !important;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .section-title {
        font-size: 1.4rem;
        color: #1E64C8 !important;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    .normal-text {
        font-size: 1rem;
        color: #333333 !important;
        text-align: justify;
        margin-bottom: 1rem;
    }
    .quote-text {
        font-size: 0.95rem;
        color: #555555 !important;
        padding-left: 1rem;
        border-left: 3px solid #1E64C8;
        margin-bottom: 1rem;
    }
    .footer {
        font-size: 0.8rem;
        color: #777777 !important;
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #EEEEEE;
    }
</style>
""", unsafe_allow_html=True)

# Resto do código original mantido igual...
st.markdown("""
<script type="text/javascript">
    function forceScrollToTop() {
        window.scrollTo(0, 0);
        document.documentElement.scrollTo(0, 0);
        document.body.scrollTo(0, 0);
        
        if (window.scrollY > 0) {
            setTimeout(forceScrollToTop, 100);
        }
    }
    
    forceScrollToTop();
    setTimeout(forceScrollToTop, 10);  
    setTimeout(forceScrollToTop, 100);
    setTimeout(forceScrollToTop, 200);
    setTimeout(forceScrollToTop, 500);
    setTimeout(forceScrollToTop, 1000);
    
    document.addEventListener('DOMContentLoaded', function() {
        var topButton = document.createElement('button');
        topButton.id = 'auto-top-button';
        topButton.style.position = 'fixed';
        topButton.style.top = '0';
        topButton.style.opacity = '0';
        topButton.style.pointerEvents = 'none';
        document.body.prepend(topButton);
        
        setTimeout(function() {
            document.getElementById('auto-top-button').click();
            forceScrollToTop();
        }, 100);
    });
</script>
""", unsafe_allow_html=True)

# Adicionar uma âncora no topo da página
st.markdown("""
<div id="topo"></div>
<button id="topoBtn" onclick="window.scrollTo(0,0)" 
    style="position: fixed; z-index: 9999; top: 0; left: 0; width: 1px; height: 1px; 
    opacity: 0.01; background: transparent; border: none;"></button>
""", unsafe_allow_html=True)

# Adicionar um número ao estado da sessão para forçar a reinicialização completa
if "page_load_count" not in st.session_state:
    st.session_state.page_load_count = 0
    
# Variável para controlar se precisamos rolar para o topo
if "scroll_to_top" not in st.session_state:
    st.session_state.scroll_to_top = False

# Sistema simples de senha para controle de acesso
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("<h1 class='main-header'>MedIndeniz</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Guia Completo: Indenização por Erro Médico</h2>", unsafe_allow_html=True)
    
    # Forçar centralização com HTML direto e margens auto
    balanca_url = get_medindeniz_logo_svg()
    st.markdown(f"""
    <div style="text-align: center; width: 100%;">
        <img src="{balanca_url}" width="200" style="display: block; margin: 0 auto;">
    </div>
    """, unsafe_allow_html=True)
    
    senha = st.text_input("Digite a senha de acesso fornecida na compra:", type="password")
    senha_correta = "medindeniz2025"  # Altere para a senha desejada
    
    if st.button("Acessar E-book"):
        if senha == senha_correta:
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Senha incorreta. Por favor, digite a senha fornecida na compra do e-book.")
    
    st.markdown("""
    <div style='text-align: center; margin-top: 20px; color: #666;'>
    Se você ainda não adquiriu o e-book, visite <a href='https://medindeniz.com.br' target='_blank'>nosso site</a>.
    </div>
    """, unsafe_allow_html=True)
    
    # Para a execução do app aqui até que a senha correta seja fornecida
    st.stop()

# Sidebar Navigation
st.sidebar.title("Navegação")
pages = ["Capa", "Visualizar E-book", "Baixar PDF"]

# Inicializa a escolha na sessão se necessário
if 'choice' not in st.session_state:
    st.session_state.choice = "Capa"

# Usa a variável da sessão para o estado do radio
choice = st.sidebar.radio("Ir para:", pages, index=pages.index(st.session_state.choice))

# MedIndeniz Company information in sidebar
st.sidebar.markdown("<hr style='margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: center;'>Sobre</h3>", unsafe_allow_html=True)

# Exibir a imagem da MedIndeniz
medindeniz_info = get_medindeniz_about()
medindeniz_logo_url = get_medindeniz_logo_svg()

# Mostrar imagem com texto grande 
st.sidebar.image(medindeniz_logo_url, width=250)
st.sidebar.markdown(f"""
<h2 style="font-weight: bold; color: #1E64C8; text-align: center; font-size: 26px;">{medindeniz_info['name']}</h2>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"""
<div style="text-align: center; margin-bottom: 15px; font-weight: bold; font-size: 20px;">
{medindeniz_info['title']}
</div>

<div style="text-align: center; margin-bottom: 10px;">
{medindeniz_info['description']}
</div>

{medindeniz_info['experience']}
""", unsafe_allow_html=True)

st.sidebar.markdown("<hr style='margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: center;'>Informações</h3>", unsafe_allow_html=True)
st.sidebar.markdown("""
<div style="text-align: center; margin-bottom: 10px;">
Este guia completo apresenta informações sobre indenização por erro médico no Brasil.
<br><br>
Todos os direitos reservados © 2025.
<br><br>
O conteúdo tem caráter informativo e não substitui a consulta a um advogado especializado.
</div>
""", unsafe_allow_html=True)

# Main content
if choice == "Capa":
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        # Usar URL da imagem de capa
        st.image(get_cover_image(), use_container_width=True)
        st.markdown("<h1 class='main-header'>Guia Completo: Indenização por Erro Médico</h1>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>Guia completo para profissionais e vítimas</h2>", unsafe_allow_html=True)
        
        st.markdown("<div class='blue-container'>", unsafe_allow_html=True)
        st.markdown("""
        ### O que você encontrará neste guia:
        
        - Identificação e documentação de erros médicos
        - Tipos de danos indenizáveis
        - Cálculo de indenizações com valores atualizados
        - Estratégias de negociação e acordo
        - Modelos de petições e documentos
        - Jurisprudência relevante e casos reais
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Visualizar Conteúdo", use_container_width=True):
                st.session_state.choice = "Visualizar E-book"
                st.query_params["page"] = "visualizar"
                st.rerun()
        with col_b:
            if st.button("Baixar PDF", use_container_width=True):
                st.session_state.choice = "Baixar PDF"
                st.query_params["page"] = "baixar"
                st.rerun()

elif choice == "Visualizar E-book":
    st.markdown("<h1 class='main-header'>Guia Completo: Indenização por Erro Médico</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>Guia completo para profissionais e vítimas</h2>", unsafe_allow_html=True)
    
    # Verificar se há parâmetro de capítulo na URL
    if "chapter" in st.query_params:
        try:
            url_chapter_index = int(st.query_params["chapter"])
            if 0 <= url_chapter_index < len(ebook_content["chapters"]):
                st.session_state.selected_chapter = ebook_content["chapters"][url_chapter_index]["title"]
                if st.session_state.scroll_to_top:
                    st.session_state.scroll_to_top = False
                    st.markdown("""
                    <script>
                        window.scrollTo(0, 0);
                    </script>
                    """, unsafe_allow_html=True)
        except:
            pass
    
    # Inicializar a seleção de capítulo se não existir na sessão
    if 'selected_chapter' not in st.session_state:
        st.session_state.selected_chapter = ebook_content["chapters"][0]["title"]
    
    # Seleção de capítulo em uma lista suspensa
    chapter_titles = [chapter["title"] for chapter in ebook_content["chapters"]]
    selected_chapter = st.selectbox("Selecione o capítulo:", chapter_titles, index=chapter_titles.index(st.session_state.selected_chapter))
    
    # Encontrar o índice do capítulo selecionado
    chapter_index = chapter_titles.index(selected_chapter)
    chapter = ebook_content["chapters"][chapter_index]
    
    # Atualizar a seleção de capítulo na sessão e o parâmetro na URL
    if st.session_state.selected_chapter != selected_chapter:
        st.session_state.selected_chapter = selected_chapter
        st.query_params["chapter"] = str(chapter_index)
    
    # Exibir imagem para o capítulo usando URLs
    images = get_image_urls()
    
    # Determinar qual imagem usar com base no índice do capítulo, com tamanho reduzido
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if chapter_index == 0:  # Introdução
            caption = "Documentos jurídicos relacionados a processos de erro médico"
            image_url = images["legal_documents"][0]
            st.image(image_url, use_container_width=True, caption=caption)
        elif chapter_index in [1, 2, 3]:  # Capítulos sobre erro médico
            caption = "Aspectos da relação médico-paciente e erros médicos"
            image_url = images["medical_error"][chapter_index % len(images["medical_error"])]
            st.image(image_url, use_container_width=True, caption=caption)
        elif chapter_index in [4, 5]:  # Capítulos sobre processos
            caption = "Relação entre médicos e pacientes no contexto jurídico"
            image_url = images["doctor_patient"][(chapter_index - 4) % len(images["doctor_patient"])]
            st.image(image_url, use_container_width=True, caption=caption)
        else:  # Outros capítulos
            caption = "Escritório de advocacia especializado em erro médico"
            image_url = images["law_office"][(chapter_index - 6) % len(images["law_office"])]
            st.image(image_url, use_container_width=True, caption=caption)
    
    # Mostrar título do capítulo como cabeçalho
    st.markdown(f"<h2 class='chapter-title'>{chapter['title']}</h2>", unsafe_allow_html=True)
    
    # Exibir navegação de capítulos (anterior/próximo)
    col1, col2 = st.columns(2)
    with col1:
        if chapter_index > 0:
            if st.button("← Capítulo Anterior", use_container_width=True, key="btn_anterior", 
                        help="Navegar para o capítulo anterior"):
                new_index = chapter_index - 1
                st.session_state.selected_chapter = chapter_titles[new_index]
                st.session_state.page_load_count += 1
                st.session_state.scroll_to_top = True
                st.query_params.clear()
                st.query_params["page"] = "visualizar"
                st.query_params["chapter"] = str(new_index)
                st.rerun()
    with col2:
        if chapter_index < len(chapter_titles) - 1:
            if st.button("Próximo Capítulo →", use_container_width=True, key="btn_proximo",
                        help="Navegar para o próximo capítulo"):
                new_index = chapter_index + 1
                st.session_state.selected_chapter = chapter_titles[new_index]
                st.session_state.page_load_count += 1
                st.session_state.scroll_to_top = True
                st.query_params.clear()
                st.query_params["page"] = "visualizar"
                st.query_params["chapter"] = str(new_index)
                st.rerun()
    
    # Botões de navegação no final do capítulo também
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Separador visual antes do conteúdo
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    # Exibir conteúdo do capítulo selecionado em formato card
    with st.container():
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        
        for element in chapter["content"]:
            if isinstance(element, dict):
                if element["type"] == "paragraph":
                    st.markdown(f"<p class='normal-text'>{element['text']}</p>", unsafe_allow_html=True)
                elif element["type"] == "subheading":
                    st.markdown(f"<h3 class='section-title'>{element['text']}</h3>", unsafe_allow_html=True)
                elif element["type"] == "bullet":
                    st.markdown(f"<ul><li>{element['text']}</li></ul>", unsafe_allow_html=True)
                elif element["type"] == "table" and "data" in element:
                    if "title" in element:
                        st.markdown(f"<h4>{element['title']}</h4>", unsafe_allow_html=True)
                    
                    headers = element["data"][0]
                    data = element["data"][1:]
                    st.table([dict(zip(headers, row)) for row in data])
                elif element["type"] == "quote":
                    st.markdown(
                        f"""<div class='quote-text'>
                        "{element['text']}"
                        {f"<p style='text-align: right; font-style: italic;'>— {element['source']}</p>" if "source" in element else ""}
                        </div>""", 
                        unsafe_allow_html=True
                    )
                elif element["type"] == "warning":
                    st.markdown(
                        f"""<div style='background-color: #FFF8E6; padding: 15px; border-left: 5px solid #FFB200; margin: 10px 0;'>
                        ⚠️ <strong>Atenção:</strong> {element['text']}
                        </div>""", 
                        unsafe_allow_html=True
                    )
                elif element["type"] == "tip":
                    st.markdown(
                        f"""<div style='background-color: #E8F0FE; padding: 15px; border-left: 5px solid #1E64C8; margin: 10px 0;'>
                        💡 <strong>Dica:</strong> {element['text']}
                        </div>""", 
                        unsafe_allow_html=True
                    )
                elif element["type"] == "jurisprudence":
                    st.markdown(
                        f"""<div style='background-color: #F8FAFD; padding: 15px; border: 1px solid #E0E9F5; border-radius: 5px; margin: 10px 0;'>
                        <p style='font-style: italic; color: #333;'>{element['text']}</p>
                        {f"<p style='text-align: right; font-size: 0.8em; color: #1E64C8;'>{element['source']}</p>" if "source" in element else ""}
                        </div>""", 
                        unsafe_allow_html=True
                    )
                elif element["type"] == "spacer":
                    st.write("")
            else:
                st.markdown(f"<p class='normal-text'>{element}</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Botões de navegação no final do capítulo
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if chapter_index > 0:
            if st.button("← Capítulo Anterior", use_container_width=True, key="btn_anterior_bottom", 
                        help="Navegar para o capítulo anterior"):
                new_index = chapter_index - 1
                st.session_state.selected_chapter = chapter_titles[new_index]
                st.session_state.page_load_count += 1
                st.session_state.scroll_to_top = True
                st.query_params.clear()
                st.query_params["page"] = "visualizar"
                st.query_params["chapter"] = str(new_index)
                st.rerun()
    with col2:
        if chapter_index < len(chapter_titles) - 1:
            if st.button("Próximo Capítulo →", use_container_width=True, key="btn_proximo_bottom",
                        help="Navegar para o próximo capítulo"):
                new_index = chapter_index + 1
                st.session_state.selected_chapter = chapter_titles[new_index]
                st.session_state.page_load_count += 1
                st.session_state.scroll_to_top = True
                st.query_params.clear()
                st.query_params["page"] = "visualizar"
                st.query_params["chapter"] = str(new_index)
                st.rerun()
                
    # Footer
    st.markdown("<div class='footer'>", unsafe_allow_html=True)
    st.markdown("""
    © 2025 - Todos os direitos reservados  
    Este material tem caráter informativo e não substitui a consulta a um advogado especializado.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif choice == "Baixar PDF":
    st.markdown("<h1 class='main-header'>Baixar E-book em PDF</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<div class='card-container'>", unsafe_allow_html=True)
        st.markdown("""
        ### E-book Premium: Indenização por Erro Médico
        
        Este documento em PDF contém o guia completo sobre indenização por erro médico, incluindo:
        
        - Todos os 8 capítulos do conteúdo
        - Modelos de petições e documentos
        - Parâmetros de cálculo atualizados
        - Jurisprudência relevante
        
        Pronto para download em alta qualidade.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("Gerar PDF para Download", use_container_width=True):
            with st.spinner("Gerando PDF, por favor aguarde..."):
                pdf_data = generate_pdf(
                    title=ebook_content["title"],
                    author=ebook_content["author_name"],
                    content=ebook_content
                )
                
                if pdf_data:
                    file_name = "Ebook_Indenizacao_Erro_Medico_Dr_Reginaldo_Oliveira.pdf"
                    
                    st.success("PDF gerado com sucesso!")
                    st.markdown(
                        f'<a href="data:application/pdf;base64,{pdf_data}" download="{file_name}" target="_blank">'
                        f'<button style="background-color: #1E64C8; color: white; padding: 12px 20px; '
                        f'border: none; border-radius: 4px; cursor: pointer; font-size: 16px; '
                        f'width: 100%; margin-top: 12px;">'
                        f'Baixar PDF</button></a>',
                        unsafe_allow_html=True
                    )
                else:
                    st.error("Ocorreu um erro ao gerar o PDF. Por favor, tente novamente.")

# Additional features - Template viewer (optional tab)
with st.sidebar.expander("Modelos de Documentos"):
    template_option = st.selectbox(
        "Selecione um modelo:",
        [
            "Petição Inicial",
            "Notificação Extrajudicial",
            "Requerimento de Perícia",
            "Acordo Extrajudicial",
            "Requerimento de Prontuário"
        ]
    )
    
    template_key = None
    if st.button("Visualizar Modelo"):
        templates = get_petition_templates()
        
        if template_option == "Petição Inicial":
            template_key = "initial_petition"
        elif template_option == "Notificação Extrajudicial":
            template_key = "extrajudicial_notification"
        elif template_option == "Requerimento de Perícia":
            template_key = "expert_examination_request"
        elif template_option == "Acordo Extrajudicial":
            template_key = "settlement_agreement"
        elif template_option == "Requerimento de Prontuário":
            template_key = "medical_records_request"
        
        if template_key:
            st.session_state.template_view = {
                "show": True,
                "title": templates[template_key]["title"],
                "content": templates[template_key]["content"]
            }

# Show template viewer if selected
if "template_view" in st.session_state and st.session_state.template_view["show"]:
    with st.sidebar:
        st.markdown("---")
        st.markdown(f"### {st.session_state.template_view['title']}")
        
        template_content = st.text_area(
            "Conteúdo do Modelo (copie e edite conforme necessário)",
            value=st.session_state.template_view["content"],
            height=300
        )
        
        if st.button("Fechar Visualização"):
            st.session_state.template_view["show"] = False
            st.rerun()
        
        template_filename = f"{st.session_state.template_view['title'].replace(' ', '_')}.txt"
        
        st.download_button(
            label="Baixar Modelo",
            data=template_content,
            file_name=template_filename,
            mime="text/plain"
        )
