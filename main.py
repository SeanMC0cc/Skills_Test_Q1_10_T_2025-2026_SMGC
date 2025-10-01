from pyscript import display, document

def create_order(event):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contact = document.getElementById("contact").value

    ramen = document.getElementById("ramen").value
    cake = document.getElementById("cake").value
    curry = document.getElementById("curry").value
    tea = document.getElementById("Tea").value
    Sparkling_Water = document.getElementById("Sparkling_Water").value

    total = 0
    if ramen: total += 300
    if cake: total += 150
    if curry: total += 250
    if tea: total += 80
    if Sparkling_Water: total += 60

    message = f"""
        Customer Information:
        Name    : {name}
        Address : {address}
        Contact : {contact}

        Order Status:
        ramen           : {ramen}
        cake            : {cake}
        curry           : {curry}
        Tea             : {tea}
        Sparkling_Water : {Sparkling_Water}

        Total Amount: ₱{total}
    """
    display(message, target="output")