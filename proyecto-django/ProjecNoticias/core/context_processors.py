def total_carrito(request):
    total = 0
    print("REQUEST", request)
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():

            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return {"total_carrito": total}
