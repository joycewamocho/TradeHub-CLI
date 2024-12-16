from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Float
from sqlalchemy.orm import relationship,declarative_base
import datetime
Base = declarative_base()

class  User(Base):
    __tablename__='users'

    id =Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)

    products= relationship('Product', back_populates='user')
    orders=relationship('Order' , back_populates='buyer')
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"


class Product(Base):
    __tablename__ = 'products'

    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    price=Column(Float,nullable=False)
    description=Column(String)
    image_url=Column(String)
    user_id=Column(Integer,ForeignKey('users.id'),nullable=False)

    user=relationship('User',back_populates="products")
    order=relationship('Order',back_populates='product', uselist=False)

    def __repr__(self):
        return f"Product(id ={self.id}, name={self.name}, price={self.price}, description={self.description}, image_url={self.image_url}, user_id={self.user_id})"


class Order(Base):
    __tablename__ ='orders'

    id=Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    buyer_id = Column(Integer, ForeignKey('users.id'))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)  
    
    product = relationship('Product', back_populates='order') 
    buyer = relationship('User', back_populates='orders')  

    def __repr__(self):
        return f"<Order(id={self.id}, product={self.product.name}, buyer={self.buyer.name}, date={self.order_date})>"