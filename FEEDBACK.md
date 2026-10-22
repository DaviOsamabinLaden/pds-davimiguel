# Feedback das Aulas 01 e 02

As rotas da Aula 01 e a conversão da Aula 02 estão no código. Os modelos, a chave estrangeira e as rotas de pets estão usando o ORM. Faltam as rotas de donos no `app.py`, que precisam continuar funcionando depois da refatoração, e `Flask-SQLAlchemy` no requirements. Ajusta também o `criar_banco.py` para criar e popular o mesmo banco que o app usa, porque hoje o script grava fora da pasta `instance`. No `requisicoes.http`, coloca `idade` nos exemplos de POST e PUT de pet.
