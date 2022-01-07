from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper, relationship

from src.domain.model import Batch, OrderLine


metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("quantity", Integer, nullable=False),
    Column("order_id", String(255)),
)


batches = Table(
    "batches",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reference", String(255)),
    Column("sku", String(255)),
    Column("_purchased_quantity", Integer, nullable=False),
    Column("eta", DateTime, nullable=True),
)


allocations = Table(
    "allocations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("order_line_id", ForeignKey('order_lines.id')),
    Column("batch_id", ForeignKey('batches.id')),
)


def start_mappers():
    lines_mapper = mapper(OrderLine, order_lines)
    mapper(
        Batch,
        batches,
        properties={
            '_allocations': relationship(
                lines_mapper, secondary=allocations, collection_class=set
            )
        }
    )
