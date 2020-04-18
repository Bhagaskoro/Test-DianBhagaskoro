CREATE TABLE Category (
    id_category int NOT NULL,
    name varchar(100) NOT NULL,
    PRIMARY KEY (id_category)
);
CREATE TABLE Cashier (
    id_cashier int NOT NULL,
    name varchar(100) NOT NULL,
    PRIMARY KEY (id_cashier)
);
CREATE TABLE Product (
    id int NOT NULL,
    name varchar(100) NOT NULL,
    price int,
    id_category int,
    id_cashier int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_category) REFERENCES Category(id_category),
    FOREIGN KEY (id_cashier) REFERENCES Cashier(id_cashier)
);
insert into Category(id_category, name) values(1, "Food");
insert into Category(id_category, name) values(2, "Drink");
insert into Cashier(id_cashier, name) values(1, "Pevita Pearce");
insert into Cashier(id_cashier, name) values(2, "Raisa Andriana");
insert into Cashier(id_cashier, name) values(3, "Dian Bhagaskoro");
insert into Product(id, name, price, id_category, id_cashier) values(1, "Latte", 10000, 2, 1);
insert into Product(id, name, price, id_category, id_cashier) values(2, "Cake", 20000, 1, 2);
insert into Product(id, name, price, id_category, id_cashier) values(3, "Fried Chicken", 45000, 1, 3);

Select Cashier.name, Product.name, Category.name, Product.Price From Product,Category,Cashier Where Product.id_cashier = Cashier.id_cashier AND Product.id_category = Category.id_category;
