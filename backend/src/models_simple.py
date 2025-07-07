from datetime import datetime
from src.database import db

class Cliente:
    collection = db.clientes
    
    @staticmethod
    def create(data):
        """Criar novo cliente"""
        cliente_data = {
            **data,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "status": data.get("status", "Novo"),
            "perfil": data.get("perfil", ""),
            "documentos": [],
            "historico": []
        }
        
        result = Cliente.collection.insert_one(cliente_data)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        """Listar todos os clientes"""
        clientes = list(Cliente.collection.find())
        return clientes
    
    @staticmethod
    def get_by_id(cliente_id):
        """Buscar cliente por ID"""
        cliente = Cliente.collection.find_one({"_id": cliente_id})
        return cliente
    
    @staticmethod
    def update(cliente_id, data):
        """Atualizar cliente"""
        data["updated_at"] = datetime.utcnow()
        result = Cliente.collection.update_one(
            {"_id": cliente_id},
            {"$set": data}
        )
        return result.modified_count > 0

class Lead:
    collection = db.leads
    
    @staticmethod
    def create(data):
        """Criar novo lead"""
        lead_data = {
            **data,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "status": data.get("status", "Novo"),
            "fonte": data.get("fonte", "LinkedIn"),
            "convertido": False
        }
        
        result = Lead.collection.insert_one(lead_data)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        """Listar todos os leads"""
        leads = list(Lead.collection.find())
        return leads

class Licitacao:
    collection = db.licitacoes
    
    @staticmethod
    def create(data):
        """Criar nova licitação"""
        licitacao_data = {
            **data,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "status": data.get("status", "Aberta"),
            "monitorada": True
        }
        
        result = Licitacao.collection.insert_one(licitacao_data)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        """Listar todas as licitações"""
        licitacoes = list(Licitacao.collection.find())
        return licitacoes

class Orcamento:
    collection = db.orcamentos
    
    @staticmethod
    def create(data):
        """Criar novo orçamento"""
        # Gerar número sequencial
        ultimo = Orcamento.collection.find_one()
        numero = 1
        
        orcamento_data = {
            **data,
            "numero": numero,
            "numero_formatado": f"{numero:03d}-2025",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "status": data.get("status", "Pendente")
        }
        
        result = Orcamento.collection.insert_one(orcamento_data)
        return result.inserted_id

class Financeiro:
    collection = db.financeiro
    
    @staticmethod
    def create_transacao(data):
        """Criar nova transação financeira"""
        transacao_data = {
            **data,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "tipo": data.get("tipo", "receita"),  # receita ou despesa
            "categoria": data.get("categoria", ""),
            "status": data.get("status", "pendente")
        }
        
        result = Financeiro.collection.insert_one(transacao_data)
        return result.inserted_id

class GuardaMoveis:
    collection = db.guarda_moveis
    
    @staticmethod
    def create_box(data):
        """Criar novo box"""
        box_data = {
            **data,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "status": data.get("status", "disponivel"),  # disponivel, ocupado, reservado
            "itens": []
        }
        
        result = GuardaMoveis.collection.insert_one(box_data)
        return result.inserted_id

class Estoque:
    collection = db.estoque
    
    @staticmethod
    def create_item(data):
        """Criar novo item de estoque"""
        item_data = {
            **data,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "quantidade": data.get("quantidade", 0),
            "quantidade_minima": data.get("quantidade_minima", 10),
            "movimentacoes": []
        }
        
        result = Estoque.collection.insert_one(item_data)
        return result.inserted_id

