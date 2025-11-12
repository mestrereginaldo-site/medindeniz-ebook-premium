from flask import Flask, render_template_string
import os

app = Flask(__name__)
app.secret_key = 'test_secret_key_123'

@app.route('/')
def hello():
    try:
        # Template HTML simples em string para testar
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>MedIndeniz - Teste</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f0f2f6; }
                .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                h1 { color: #1E64C8; text-align: center; }
                .success { color: green; text-align: center; font-size: 18px; margin: 20px 0; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 MedIndeniz - Teste</h1>
                <div class="success">✅ Aplicação Flask está funcionando!</div>
                <p>Se você está vendo esta página, significa que:</p>
                <ul>
                    <li>✅ Flask está instalado corretamente</li>
                    <li>✅ Servidor está rodando</li>
                    <li>✅ Templates básicos funcionam</li>
                </ul>
                <p><strong>Próximo passo:</strong> Vamos adicionar o sistema de autenticação.</p>
                <a href="/login" style="display: inline-block; padding: 10px 20px; background: #1E64C8; color: white; text-decoration: none; border-radius: 5px;">Ir para Login</a>
            </div>
        </body>
        </html>
        """
        return render_template_string(html)
    except Exception as e:
        return f"Erro: {str(e)}", 500

@app.route('/login')
def login():
    try:
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Login - MedIndeniz</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f0f2f6; }
                .container { max-width: 400px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                h1 { color: #1E64C8; text-align: center; }
                .form-group { margin-bottom: 20px; }
                input[type="password"] { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; box-sizing: border-box; }
                button { width: 100%; padding: 12px; background: #1E64C8; color: white; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🔐 Login</h1>
                <p>Teste do sistema de autenticação</p>
                <form method="POST" action="/login">
                    <div class="form-group">
                        <label>Senha:</label>
                        <input type="password" name="senha" required>
                    </div>
                    <button type="submit">Acessar</button>
                </form>
                <p style="text-align: center; margin-top: 20px; color: #666;">
                    Use a senha: <strong>medindeniz2025</strong>
                </p>
            </div>
        </body>
        </html>
        """
        return render_template_string(html)
    except Exception as e:
        return f"Erro no login: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
