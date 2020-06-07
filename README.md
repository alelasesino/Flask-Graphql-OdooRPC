# GraphQL Odoo

[![Licence LGPL](https://img.shields.io/badge/licence-LGPL--3-blue.png)](http://www.gnu.org/licenses/lgpl-3.0-standalone.html)

Es una aplicación web creada con el framework llamado [Flask](https://flask.palletsprojects.com/en/1.1.x/), utiliza mediante la librería [odoo-rpc](https://github.com/OCA/odoorpc) una comunicación mediante el protocolo XML-RPC con el software de planificación de recursos empresariales [Odoo](https://github.com/odoo/odoo).

## Visión General

La aplicación crea una interfaz de programación de aplicaciones (API), permitiendo acceder y modificar los datos de los diferentes modelos que tiene Odoo.

Implementa un esquema mediante la librería de [Graphene](https://graphene-python.org/), en el cual se han definido una serie de consultas, mutaciones y tipos de datos.

## Uso

Ejecuta el fichero `app.py` para levantar un servidor de desarrollo. Dirígete a `http://localhost:5555/`. La aplicación se reiniciara automáticamente cuando se realize algún cambio en los ficheros fuente.

Dirígete a `http://localhost:5555/graphql` para acceder al entorno gráfico que ofrece GraphQL y realizar sus propias consultas.

Para comenzar a trabajar con esta aplicación, es recomendable tener conocimiento de los siguientes conceptos

- Aprenda los [conceptos básicos de GraphQL](https://graphql.org/learn/)
- Examine las consultas de ejemplo guardadas en el historial
- Comience a realizar sus propias consultas al esquema de GraphQL

## Obsoleto

Esta aplicación ha quedado obsoleta ya que su funcionalidad ha sido implantada en el módulo de [graphql_odoo](https://github.com/alelasesino/graphql_odoo) creado en Odoo.

## Créditos

Este módulo ha sido creado como parte del proyecto de final de grado por Alejandro Pérez Álvarez.

Para cualquier consulta, contacta con <alejperez99@hotmail.com>.
