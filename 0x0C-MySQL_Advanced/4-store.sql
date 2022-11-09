-- New trigger
CREATE TRIGGER decrease BEFORE INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;