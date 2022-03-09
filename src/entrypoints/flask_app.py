from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from src import OutOfStock, InvalidSku
from src.domain.model import OrderLine, Batch
from src.adapters import orm, repository
from src.service_layer import services


orm.start_mappers()
app = Flask(__name__)
get_session = sessionmaker(bid=create_engine(config.get_postgres_uri()))


@app.route("/allocate", methods=["POST"])
def allocate():
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    line = OrderLine(
        request.json["order_id"],
        request.json["sku"],
        request.json["quantity"],
    )
    try:
        batch_reference = services.allocate(line, repo, session)
        return {"batch_reference": batch_reference}, 201
    except (OutOfStock, InvalidSku) as exc:
        return {"message": str(exc)}, 400
