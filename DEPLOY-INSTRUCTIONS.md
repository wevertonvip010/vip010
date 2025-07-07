# 🚀 Instruções de Deploy - VIP Mudanças v3.0

## 📋 Checklist Pré-Deploy

- [ ] Código testado localmente
- [ ] Credenciais de produção configuradas
- [ ] Banco de dados configurado
- [ ] Domínio configurado
- [ ] SSL configurado

## 🌐 Deploy Frontend (Vercel)

### 1. Preparar Build
```bash
cd frontend
npm run build
```

### 2. Deploy na Vercel
1. Conectar repositório GitHub à Vercel
2. Configurar build command: `npm run build`
3. Configurar output directory: `dist`
4. Configurar domínio: `app.vipmudancas.com.br`

### 3. Variáveis de Ambiente (Vercel)
```bash
VITE_API_URL=https://seu-backend.render.com/api
```

## 🖥️ Deploy Backend (Render)

### 1. Configurar Render
1. Conectar repositório GitHub ao Render
2. Selecionar pasta: `backend`
3. Build command: `pip install -r requirements.txt`
4. Start command: `python src/main.py`

### 2. Variáveis de Ambiente (Render)
```bash
MONGODB_URI=mongodb+srv://usuario:senha@cluster.mongodb.net/vip_mudancas
JWT_SECRET_KEY=sua-chave-jwt-super-secreta
FLASK_DEBUG=False
SECRET_KEY=sua-chave-flask-secreta
CORS_ORIGINS=https://app.vipmudancas.com.br
```

## 🗄️ Configurar Banco (Railway PostgreSQL)

### 1. Criar Banco no Railway
1. Criar novo projeto no Railway
2. Adicionar PostgreSQL
3. Copiar connection string

### 2. Migrar para PostgreSQL
```python
# Atualizar database.py para usar PostgreSQL
import psycopg2
from sqlalchemy import create_engine

DATABASE_URL = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URL)
```

## 🔧 Configurações de Produção

### 1. Atualizar CORS
```python
# backend/src/config.py
CORS_ORIGINS = [
    "https://app.vipmudancas.com.br",
    "https://vipmudancas.com.br"
]
```

### 2. Configurar JWT
```python
# Usar chave secreta forte
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
```

### 3. Configurar SSL
- Certificado automático via Vercel/Render
- Forçar HTTPS em produção

## 📊 Monitoramento

### 1. Logs
- Vercel: Dashboard de logs automático
- Render: Logs em tempo real
- Railway: Logs do banco de dados

### 2. Métricas
- Uptime monitoring
- Performance monitoring
- Error tracking

## 🔐 Segurança

### 1. Variáveis Sensíveis
- Nunca commitar chaves no código
- Usar variáveis de ambiente
- Rotacionar chaves periodicamente

### 2. HTTPS
- Forçar HTTPS em produção
- Configurar HSTS headers
- Validar certificados

## 🧪 Testes Pós-Deploy

### 1. Funcionalidades Críticas
- [ ] Login funcionando
- [ ] Dashboard carregando
- [ ] Navegação entre páginas
- [ ] API respondendo

### 2. Performance
- [ ] Tempo de carregamento < 3s
- [ ] Responsividade mobile
- [ ] Sem erros no console

## 🆘 Troubleshooting

### Problemas Comuns

**Frontend não carrega:**
- Verificar variável VITE_API_URL
- Verificar build do Vite
- Verificar configuração do domínio

**Backend com erro 500:**
- Verificar variáveis de ambiente
- Verificar conexão com banco
- Verificar logs do Render

**Erro de CORS:**
- Verificar CORS_ORIGINS no backend
- Verificar protocolo (HTTP vs HTTPS)

## 📞 Suporte

Em caso de problemas:
1. Verificar logs das plataformas
2. Testar localmente primeiro
3. Verificar variáveis de ambiente
4. Contatar suporte técnico

---

**Deploy realizado com sucesso! 🎉**

