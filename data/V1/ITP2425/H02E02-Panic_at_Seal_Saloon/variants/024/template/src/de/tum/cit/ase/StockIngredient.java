package de.tum.cit.ase;

public class StockIngredient {
    private final String name;
    private final int price;
    private int quantity;

    public StockIngredient(String name, int price, int quantity) {
        if (name == null) {
            this.name = "";
        } else {
            this.name = name;
        }

        if (price < 0) {
            this.price = 0;
        } else {
            this.price = price;
        }

        if (quantity < 0) {
            this.quantity = 0;
        } else {
            this.quantity = quantity;
        }
    }

    public String getName() {
        return this.name;
    }

    public int getPrice() {
        return this.price;
    }

    public int getQuantity() {
        return this.quantity;
    }

    public void setQuantity(int quantity) {
        if (quantity >= 0) {
            this.quantity = quantity;
        }
    }
}