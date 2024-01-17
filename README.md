# Takeaway Share

You ordered by takeaway and decided to pay by cash. The times passes while you play and suddenly the rider arrives and you forgot to prepare the cash.
A couple of friends go to the door with the cash they have at the moment and pay the order to the rider.

So, now how do you know how much you have to give to who and how much those friends have to get back?

---

There is no interface, so you have to insert data directly in *order.py*


```python
order = Order()
# Report what every person has to pay for their personal purchase
order.new_purchase("John", "", 12.5)
order.new_purchase("Alice", "", 12.5)
order.new_purchase("Margaret", "", 12.5)

# Report a divided purchase, for example expedition costs or a divided item
order.new_divided_purchase(["John",
                         "Alice",
                         "Margaret"], "", 3.5)

# Report the advanced that someone placed
order.new_advance("John", 20.0)
order.new_advance("Margaret", 20.0)
order.new_advance("Alice", 5.0)

# Calc open debts
order.calc_debts()
# Calc how much one has to give to another
order.calc_transfers()
```
