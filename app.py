from flask import Flask, render_template, request, session, redirect, url_for, send_file
import base64
from io import BytesIO
import os

app = Flask(__name__)
app.secret_key = 'medindeniz_secret_key_2025'

# Dados do e-book diretamente no código (sem imports externos)
ebook_content = {
    "title": "E-book Premium: Indenização por Erro Médico",
    "subtitle": "Guia completo para profissionais e vítimas", 
    "author_name": "Dr. Reginaldo Oliveira",
    "author_title": "Advogado Especialista em Direito Médico",
    "chapters": [
        {
            "title": "Introdução ao Erro Médico",
            "content": """
            <h3>Bem-vindo ao guia completo sobre indenização por erro médico</h3>
            <p>Este material foi desenvolvido para oferecer informações valiosas tanto para vítimas quanto para profissionais do direito que atuam nesta área.</p>
            <p>Os erros médicos podem ter consequências devastadoras na vida dos pacientes, desde sequelas permanentes até, nos casos mais graves, o óbito.</p>
            <div class="alert alert-info">
                <strong>💡 Dica:</strong> Compreender seus direitos é o primeiro passo para buscar uma reparação justa.
            </div>
            """
        },
        {
            "title": "Capítulo 1: Identificação do Erro Médico",
            "content": """
            <h3>Como identificar um erro médico</h3>
            <p>O erro médico é caracterizado por uma falha no exercício da profissão médica que resulta em dano ao paciente.</p>
            
            <h4>Tipos de Erro Médico:</h4>
            <ul>
                <li><strong>Negligência:</strong> Quando o médico deixa de tomar os cuidados necessários</li>
                <li><strong>Imprudência:</strong> Quando o profissional age precipitadamente</li>
                <li><strong>Imperícia:</strong> Falta de habilidade técnica ou conhecimento</li>
            </ul>
            
            <div class="alert alert-warning">
                <strong>⚠️ Atenção:</strong> Nem todo resultado adverso caracteriza erro médico. É necessário comprovar o nexo causal.
            </div>
            """
        },
        {
            "title": "Capítulo 2: Cálculo de Indenizações",
            "content": """
            <h3>Como calcular indenizações por erro médico</h3>
            <p>Determinar o valor da indenização é um dos aspectos mais complexos destes processos.</p>
            
            <h4>Parâmetros de Referência:</h4>
            <table class="table">
                <thead>
                    <tr>
                        <th>Gravidade</th>
                        <th>Valor (R$)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Leve</td>
                        <td>10.000 a 30.000</td>
                    </tr>
                    <tr>
                        <td>Moderado</td>
                        <td>30.000 a 100.000</td>
                    </tr>
                    <tr>
                        <td>Grave</td>
                        <td>100.000 a 300.000</td>
                    </tr>
                </tbody>
            </table>
            
            <p>Valores baseados em jurisprudência recente, sujeitos a variação conforme o caso.</p>
            """
        }
    ]
}

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

@app.route('/capa')
@require_auth
def capa():
    return render_template('capa.html', ebook_content=ebook_content)

@app.route('/visualizar')
@require_auth
def visualizar():
    chapter_index = request.args.get('chapter', 0, type=int)
    if chapter_index >= len(ebook_content["chapters"]):
        chapter_index = 0
    
    chapter = ebook_content["chapters"][chapter_index]
    
    return render_template('visualizar.html', 
                         chapter=chapter,
                         chapter_index=chapter_index,
                         total_chapters=len(ebook_content["chapters"]))

@app.route('/baixar-pdf')
@require_auth
def baixar_pdf():
    # PDF simulado - em produção você pode gerar um PDF real
    pdf_content = "%PDF-1.4\n%Simulated PDF content\nE-book: Indenização por Erro Médico\nConteúdo completo disponível online."
    return send_file(
        BytesIO(pdf_content.encode()),
        download_name="Ebook_Indenizacao_Erro_Medico.pdf",
        as_attachment=True,
        mimetype='application/pdf'
    )

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
