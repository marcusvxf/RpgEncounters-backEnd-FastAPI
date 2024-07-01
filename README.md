# Rpg Ecounter Organizer

<b>PT-BR</b>
Essa é uma aplicação para mestres de rpg com intuito de facilitar a montagem dos encontros nas campanhas de rpg facilitando o mapeamento de iniciativas a reutilização de criaturas e mais, o projeto foi feito em python com a fastApi.


<b>EN-US</b>
This is an application for dungeon masters with the aim of facilitating the assembly of encounters in rpg campaigns, facilitating the mapping of initiatives, the reuse of creatures and more, the project was made in Python with fastApi.


#### How to Configure?

First you need to install these libs :
``` bash
    $ pip install fastApi
    $ pip install SQLAlchemy
    $ pip install mysqlclient
    $ pip install Alembic
```

After, run the migrations :
``` bash
    # if you need to create the migrations run  
    # $ alembic revision --autogenerate
    $ alembic upgrade head 
```

Now run the application :
``` bash
    $ uvicorn app.main:app --reload
```