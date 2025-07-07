from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import hashlib
from datetime import datetime, timedelta
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configurações
app.config['JWT_SECRET_KEY'] = 'vip-mudancas-secret-key-2024'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

# Inicializar extensões
jwt = JWTManager(app)
CORS(app, origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://bhyyqktg.manus.space",
    "https://ledxqeqe.manus.space",
    "https://mlxhcrkp.manus.space",
    "https://ugymbykw.manus.space",
    "https://bsqczymj.manus.space",
    "https://hmuclquw.manus.space"
])

# Banco de dados em memória (para desenvolvimento)
users_db = {}
clientes_db = []
leads_db = []
licitacoes_db = []

def hash_password(password):
    """Hash da senha usando SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def create_default_user():
    """Criar usuário padrão"""
    cpf = "123.456.789-01"
    password = "1234"
    
    users_db[cpf] = {
        'cpf': cpf,
        'password': hash_password(password),
        'nome': 'Administrador',
        'email': 'admin@vipmudancas.com.br',
        'created_at': datetime.now().isoformat()
    }
    logger.info(f"Usuário admin padrão criado: CPF {cpf} / Senha {password}")

# Rotas de autenticação
@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        cpf = data.get('cpf')
        password = data.get('password')
        
        logger.info(f"Tentativa de login: CPF {cpf}")
        
        if not cpf or not password:
            return jsonify({'message': 'CPF e senha são obrigatórios'}), 400
        
        # Verificar se usuário existe
        user = users_db.get(cpf)
        if not user:
            logger.warning(f"Usuário não encontrado: {cpf}")
            return jsonify({'message': 'Credenciais inválidas'}), 401
        
        # Verificar senha
        if user['password'] != hash_password(password):
            logger.warning(f"Senha incorreta para: {cpf}")
            return jsonify({'message': 'Credenciais inválidas'}), 401
        
        # Criar token
        access_token = create_access_token(identity=cpf)
        
        logger.info(f"Login bem-sucedido: {cpf}")
        return jsonify({
            'access_token': access_token,
            'message': 'Login realizado com sucesso',
            'user': {
                'cpf': user['cpf'],
                'nome': user['nome'],
                'email': user['email']
            }
        }), 200
        
    except Exception as e:
        logger.error(f"Erro no login: {str(e)}")
        return jsonify({'message': 'Erro interno do servidor'}), 500

@app.route('/api/auth/verify', methods=['GET'])
@jwt_required()
def verify_token():
    try:
        current_user_cpf = get_jwt_identity()
        user = users_db.get(current_user_cpf)
        
        if not user:
            return jsonify({'message': 'Usuário não encontrado'}), 404
        
        return jsonify({
            'valid': True,
            'user': {
                'cpf': user['cpf'],
                'nome': user['nome'],
                'email': user['email']
            }
        }), 200
        
    except Exception as e:
        logger.error(f"Erro na verificação do token: {str(e)}")
        return jsonify({'message': 'Token inválido'}), 401

# Rotas do dashboard
@app.route('/api/dashboard/stats', methods=['GET'])
@jwt_required()
def dashboard_stats():
    try:
        stats = {
            'total_mudancas': 156,
            'boxes_ocupados': 89,
            'visitas_agendadas': 23,
            'receita_mensal': 45000.00,
            'atividades_recentes': [
                {
                    'id': 1,
                    'tipo': 'mudanca',
                    'descricao': 'Nova mudança agendada - João Silva',
                    'data': datetime.now().isoformat()
                },
                {
                    'id': 2,
                    'tipo': 'vistoria',
                    'descricao': 'Vistoria concluída - Apartamento Centro',
                    'data': (datetime.now() - timedelta(hours=2)).isoformat()
                }
            ]
        }
        return jsonify(stats), 200
        
    except Exception as e:
        logger.error(f"Erro ao buscar estatísticas: {str(e)}")
        return jsonify({'message': 'Erro interno do servidor'}), 500

# Rotas de clientes
@app.route('/api/clientes', methods=['GET'])
@jwt_required()
def get_clientes():
    try:
        return jsonify(clientes_db), 200
    except Exception as e:
        logger.error(f"Erro ao buscar clientes: {str(e)}")
        return jsonify({'message': 'Erro interno do servidor'}), 500

@app.route('/api/clientes', methods=['POST'])
@jwt_required()
def create_cliente():
    try:
        data = request.get_json()
        cliente = {
            'id': len(clientes_db) + 1,
            'nome': data.get('nome'),
            'cpf': data.get('cpf'),
            'telefone': data.get('telefone'),
            'email': data.get('email'),
            'endereco': data.get('endereco'),
            'created_at': datetime.now().isoformat()
        }
        clientes_db.append(cliente)
        return jsonify(cliente), 201
    except Exception as e:
        logger.error(f"Erro ao criar cliente: {str(e)}")
        return jsonify({'message': 'Erro interno do servidor'}), 500

# Rotas de leads
@app.route('/api/leads', methods=['GET'])
@jwt_required()
def get_leads():
    try:
        return jsonify(leads_db), 200
    except Exception as e:
        logger.error(f"Erro ao buscar leads: {str(e)}")
        return jsonify({'message': 'Erro interno do servidor'}), 500

# Rotas de licitações
@app.route('/api/licitacoes', methods=['GET'])
@jwt_required()
def get_licitacoes():
    try:
        return jsonify(licitacoes_db), 200
    except Exception as e:
        logger.error(f"Erro ao buscar licitações: {str(e)}")
        return jsonify({'message': 'Erro interno do servidor'}), 500

# Rota de health check
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '3.0.0'
    }), 200

if __name__ == '__main__':
    # Criar usuário padrão
    create_default_user()
    
    # Iniciar servidor
    logger.info("Iniciando servidor VIP Mudanças v3.0...")
    app.run(host='0.0.0.0', port=5000, debug=True)

