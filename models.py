from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Clientes(Base):
    __tablename__ = 'clientes'
    cli_codigo = Column(Integer, primary_key=True, autoincrement=True)
    cli_nome = Column(String(100), nullable=False)
    cli_sobrenome = Column(String(100), nullable=False)
    cli_email = Column(String(100), unique=True, nullable=False)
    cli_senha_hash = Column(String(150), nullable=False)
    cli_criado_em = Column(DateTime, server_default=func.now())

class Categorias(Base):
    __tablename__ = 'categorias'
    cat_codigo = Column(Integer, primary_key=True, autoincrement=True)
    cat_nome = Column(String(100), nullable=False)
    cat_subcategoria = Column(String(100), nullable=False)

class Produtos(Base):
    __tablename__ = 'produtos'
    pro_codigo = Column(Integer, primary_key=True, autoincrement=True)
    pro_nome = Column(String(100), nullable=False)
    pro_cat_codigo = Column(Integer, ForeignKey('categorias.cat_codigo'), nullable=False)
    pro_preco = Column(DECIMAL(10,2), nullable=False)
    pro_estoque = Column(Integer, nullable=False)

class Pedidos(Base):
    __tablename__ = 'pedidos'
    ped_codigo = Column(Integer, primary_key=True, autoincrement=True)
    ped_cli_codigo = Column(Integer, ForeignKey('clientes.cli_codigo'), nullable=False)
    ped_status = Column(String(30), server_default='pendente')
    ped_total = Column(DECIMAL(10,2), nullable=False)
    ped_datacriacao = Column(DateTime, server_default=func.now())

class ItensPedido(Base):
    __tablename__ = 'itens_pedido'
    ipe_codigo = Column(Integer, primary_key=True, autoincrement=True)
    ipe_ped_codigo = Column(Integer, ForeignKey('pedidos.ped_codigo'), nullable=False)
    ipe_pro_codigo = Column(Integer, ForeignKey('produtos.pro_codigo'), nullable=False)
    ipe_quantidade = Column(Integer, nullable=False)
    ipe_preco_unitario = Column(DECIMAL(10,2), nullable=False)
