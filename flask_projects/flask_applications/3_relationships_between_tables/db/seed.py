import json
from models import db
from models.user import User
from models.product import Product
from models.order import Order

def load_initial_data(filepath='assets/data.json'):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Create sample user
        user_data = data.get('users', [])[0]
        user = User(
            id=user_data['id'],
            name=user_data['name'],
            email=user_data['email']
        )
        user.set_password(user_data['password'])  # ✅ Set BEFORE session.add
        db.session.add(user)
        db.session.flush()

        user_id = user.id

        # Load Products
        product_map = {}
        for p in data.get('products', []):
            product = Product(
                name=p['name'],
                description=p.get('description'),
                price=p['price'],
                stock=p.get('stock', 0),
                created_by=user_id
            )
            db.session.add(product)
            product_map[product.name] = product

        db.session.flush()

        # Load Orders
        for o in data.get('orders', []):
            order = Order(
                user_id=o['user_id'],
                created_by=user_id,
                total=o['total'],
            )
            for pname in o.get('product_names', []):
                product = product_map.get(pname)
                if not product:
                    raise ValueError(f"Product '{pname}' not found for order '{o['user_id']}'")
                order.products.append(product)
            db.session.add(order)

        db.session.commit()
        print("✅ Seed data loaded successfully.")

    except FileNotFoundError:
        print(f"❌ File '{filepath}' not found.")
    except json.JSONDecodeError:
        print("❌ JSON decode error.")
    except Exception as e:
        db.session.rollback()
        print(f"❌ Unexpected error: {e}")
