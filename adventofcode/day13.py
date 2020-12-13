def parse_bus_info(bus_info):
    time, bus_ids = bus_info.splitlines()
    time = int(time)
    # bus_ids = ["x" if bus == "x" else int(bus) for bus in bus_ids.split(",")]
    bus_ids = [int(bus) for bus in bus_ids.split(",") if bus != "x"]

    return time, bus_ids


def earliest_bus(start_time, bus_ids):
    delta = 0
    while True:
        time = start_time + delta

        for bus in bus_ids:
            if time % bus == 0:
                return time, bus

        delta += 1
