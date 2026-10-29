from app import app, db, Dono, Pet

with app.app_context():
    # Cria todas as tabelas na pasta instance/
    db.create_all()

    # Só insere os dados de exemplo se o banco estiver vazio
    if Dono.query.first() is None:
        ana = Dono(nome="Ana Paula Ribeiro", telefone="45999110001")
        bruno = Dono(nome="Bruno Martins", telefone="45999110002")

        db.session.add(ana)
        db.session.add(bruno)
        db.session.commit()

        rex = Pet(nome="Rex", especie="cachorro", idade=4, dono_id=ana.id)
        mimi = Pet(nome="Mimi", especie="gato", idade=2, dono_id=ana.id)
        thor = Pet(nome="Thor", especie="cachorro", idade=7, dono_id=bruno.id)

        db.session.add(rex)
        db.session.add(mimi)
        db.session.add(thor)
        db.session.commit()

        print("Banco de dados criado e populado com sucesso na pasta instance/!")
    else:
        print("Banco de dados já contém registros.")