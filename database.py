from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Criação da Base para os modelos
Base = declarative_base()

# 1. Tabela para a Série Histórica do IPCA
class Ipca(Base):
    __tablename__ = 'ipca'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_referencia = Column(String, nullable=False) # Ex: '2023-01'
    indice_mensal = Column(Float, nullable=False)

# 2. Tabela para as Categorias da Cesta Básica
class CategoriaItem(Base):
    __tablename__ = 'categoria_item'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    quantidade_pedida = Column(Float, nullable=False)
    unidade_medida = Column(String, nullable=False)
    is_bonus = Column(Boolean, default=False)
    
    # Relacionamento com os produtos extraídos
    produtos = relationship("ProdutoExtraido", back_populates="categoria")

# 3. Tabela para os Produtos Extraídos via Web Scraping
class ProdutoExtraido(Base):
    __tablename__ = 'produto_extraido'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria_id = Column(Integer, ForeignKey('categoria_item.id'), nullable=False)
    nome_produto = Column(String, nullable=False)
    marca = Column(String, nullable=True)
    preco_unitario = Column(Float, nullable=False)
    url_origem = Column(String, nullable=True)
    data_coleta = Column(DateTime, default=datetime.now)
    
    # Relacionamento inverso
    categoria = relationship("CategoriaItem", back_populates="produtos")

# Configuração e Criação do Banco de Dados SQLite
def criar_banco():
    # Cria o arquivo do banco de dados na raiz do projeto
    engine = create_engine('sqlite:///cesta_basica.db', echo=True)
    
    # Cria as tabelas
    Base.metadata.create_all(engine)
    print("Banco de dados 'cesta_basica.db' e tabelas criados com sucesso!")
    
    return engine

# Executa a criação se rodar este script diretamente
if __name__ == "__main__":
    criar_banco()