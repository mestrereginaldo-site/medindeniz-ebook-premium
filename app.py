from flask import Flask, render_template, request, session, redirect, url_for, send_file
import base64
from io import BytesIO
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'medindeniz_secret_key_2025')

# Importações com tratamento de erro
try:
    from utils.pdf_generator import generate_pdf
    PDF_AVAILABLE = True
except ImportError as e:
    print(f"Erro ao importar pdf_generator: {e}")
    PDF_AVAILABLE = False

try:
    from content.chapters import ebook_content
    CONTENT_AVAILABLE = True
except ImportError as e:
    print(f"Erro ao importar chapters: {e}")
    ebook_content = {
        "title": "E-book Premium: Indenização por Erro Médico",
        "subtitle": "Guia completo para profissionais e vítimas",
        "author_name": "Dr. Reginaldo Oliveira",
        "author_title": "Advogado Especialista em Direito Médico",
        "chapters": [
            {
                "title": "Introdução",
                "content": [
                    {"type": "paragraph", "text": "Conteúdo não disponível no momento."}
                ]
            }
        ]
    }
    CONTENT_AVAILABLE = False

try:
    from assets.images import get_image_urls, get_cover_image
    from assets.logo import get_medindeniz_logo_svg, get_medindeniz_about
    IMAGES_AVAILABLE = True
except ImportError as e:
    print(f"Erro ao importar assets: {e}")
    IMAGES_AVAILABLE = False

# Sistema de autenticação
def require_auth(f):
    def decorated(*args, **kwargs):
        if not session.get('autenticado'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated.__name__ = f.__name__
    return decorated

@app.route('/', methods=['GET', 'POST'])
def login():
    try:
        if session.get('autenticado'):
            return redirect(url_for('capa'))
        
        if request.method == 'POST':
            senha = request.form.get('senha')
            if senha == "medindeniz2025":
                session['autenticado'] = True
                return redirect(url_for('capa'))
            else:
                return render_template('login.html', error="Senha incorreta")
        
        return render_template('login.html')
    except Exception as e:
        return f"Erro no login: {str(e)}", 500

@app.route('/capa')
@require_auth
def capa():
    try:
        return render_template('capa.html', 
                             ebook_content=ebook_content,
                             images_available=IMAGES_AVAILABLE)
    except Exception as e:
        return f"Erro na capa: {str(e)}", 500

@app.route('/visualizar')
@require_auth
def visualizar():
    try:
        chapter_index = request.args.get('chapter', 0, type=int)
        if chapter_index >= len(ebook_content["chapters"]):
            chapter_index = 0
        
        chapter = ebook_content["chapters"][chapter_index]
        return render_template('visualizar.html', 
                             chapter=chapter,
                             chapter_index=chapter_index,
                             chapters=ebook_content["chapters"],
                             ebook_content=ebook_content,
                             images_available=IMAGES_AVAILABLE)
    except Exception as e:
        return f"Erro no visualizar: {str(e)}", 500

@app.route('/baixar-pdf')
@require_auth
def baixar_pdf():
    try:
        if PDF_AVAILABLE:
            pdf_data = generate_pdf(
                ebook_content["title"],
                ebook_content["author_name"],
                ebook_content
            )
            
            if pdf_data:
                pdf_bytes = base64.b64decode(pdf_data)
                return send_file(
                    BytesIO(pdf_bytes),
                    download_name="Ebook_Indenizacao_Erro_Medico.pdf",
                    as_attachment=True,
                    mimetype='application/pdf'
                )
        return "Sistema de PDF em manutenção. Tente novamente mais tarde."
    except Exception as e:
        return f"Erro no PDF: {str(e)}", 500

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
