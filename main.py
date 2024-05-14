from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class TransportMode:
    def __init__(self, name):
        self.name = name

class Bus(TransportMode):
    def __init__(self, name, route):
        super().__init__(name)
        self.route = route

class Train(TransportMode):
    def __init__(self, name, route):
        super().__init__(name)
        self.route = route

class Taxi(TransportMode):
    def __init__(self, name):
        super().__init__(name)

class BodaBoda(TransportMode):
    def __init__(self, name):
        super().__init__(name)

class RideSharing(TransportMode):
    def __init__(self, name):
        super().__init__(name)

class IntegratedMobilityPlatform:
    def __init__(self):
        self.available_modes = {}

    def add_transport_mode(self, transport_mode):
        if isinstance(transport_mode, TransportMode):
            self.available_modes[transport_mode.name] = transport_mode
            print(f"{transport_mode.name} added to the platform.")
            return jsonify({"message": f"{transport_mode.name} added to the platform."}), 200
        else:
            return jsonify({"error": "Invalid transport mode."}), 400

    def search_route(self, source, destination):
        towns_in_kenya = ["Nairobi", "Mombasa", "Kisumu", "Eldoret", "Nakuru", "Meru", "Thika", "Malindi", "Kakamega", "Naivasha", "Kitale", "Garissa", "Nyeri", "Machakos", "Embu", "Kericho", "Bungoma", "Kiambu", "Lamu", "Isiolo", "Mandera", "Nandi", "Lodwar", "Kisii", "Homa Bay", "Wajir", "Marsabit", "Voi", "Nyamira", "Kabarnet", "Busia", "Kitui", "Kilifi", "Wundanyi", "Maralal", "Nyahururu", "Kerugoya", "Siaya", "Emali", "Kajiado", "Ruiru", "Karuri", "Moyale", "Karatina", "Mwingi", "Bomet", "Luanda", "Makueni", "Bondo", "Vihiga", "Webuye", "Ol Kalou", "Gilgil", "Mumias", "Taveta", "Kapsabet", "Oyugis", "Kangundo", "Iten", "Narok", "Kilgoris", "Takaungu", "Kakuma", "Nanyuki", "Lugulu", "Sotik", "Kabati", "Awasi", "Mariakani", "Kathwana", "Kapsowar", "Eldama Ravine", "Ngong", "Keroka", "Limuru", "Naro Moru", "Nkubu", "Molo", "Muhoroni", "Kangema", "Chuka", "Matuu", "Tabaka", "Kwale", "Bura", "Loitokitok", "Londiani", "Ogembo", "Rumuruti", "Laisamis", "Wote", "Kibwezi", "Sagana", "Maragua", "Kiboga", "Rongo", "Kehancha", "Malaba", "Witu", "Kandara", "Merti", "Muranga", "Kathiani", "Maua", "Mbita", "Mpeketoni", "Chwele", "Tala", "Githunguri", "Kinango", "Kinamba", "Njoro"]

        if source in towns_in_kenya and destination in towns_in_kenya:
            for mode_name, mode in self.available_modes.items():
                if isinstance(mode, Bus) or isinstance(mode, Train):
                    if source in mode.route and destination in mode.route:
                        return jsonify({"route": f"Route found via {mode_name}: {source} -> {destination}"}), 200
            return jsonify({"message": "No route available."}), 404
        else:
            return jsonify({"error": "Invalid source or destination."}), 400

    def book_ticket(self, mode_name, source, destination):
        if mode_name in self.available_modes:
            return jsonify({"message": f"Ticket booked for {mode_name} from {source} to {destination}."}), 200
        else:
            return jsonify({"error": "Mode not available."}), 404

mobility_platform = IntegratedMobilityPlatform()

@app.route('/add_transport_mode', methods=['POST'])
def add_transport_mode():
    data = request.json
    mode_type = data.get('type')
    name = data.get('name')
    route = data.get('route')

    if mode_type == "Bus":
        transport_mode = Bus(name, route)
    elif mode_type == "Train":
        transport_mode = Train(name, route)
    elif mode_type == "Taxi":
        transport_mode = Taxi(name)
    elif mode_type == "BodaBoda":
        transport_mode = BodaBoda(name)
    elif mode_type == "RideSharing":
        transport_mode = RideSharing(name)
    else:
        return jsonify({"error": "Invalid mode type."}), 400

    return mobility_platform.add_transport_mode(transport_mode)

@app.route('/search_route', methods=['GET'])
def search_route():
    source = request.args.get('source')
    destination = request.args.get('destination')
    return mobility_platform.search_route(source, destination)

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    data = request.json
    mode_name = data.get('mode_name')
    source = data.get('source')
    destination = data.get('destination')
    return mobility_platform.book_ticket(mode_name, source, destination)

if __name__ == "__main__":
    app.run(debug=True)
