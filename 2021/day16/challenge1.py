from pathlib import Path

input_file = Path(__file__).parent / "in.txt"

with input_file.open("r") as f:
    string = f.readline().strip("\n")

hex2bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
binary_string = "".join(hex2bin[c] for c in string)


def parse_packet(packet):
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    if type_id != 4:
        length_type_id = packet[6]
        if length_type_id == "0":
            length = int(packet[7:22], 2)
            index = 22
            packet_length = index + length
            while index < packet_length:
                subpacket_version, subpacket_length = parse_packet(packet[index:])
                index += subpacket_length
                version += subpacket_version
        else:
            number_of_packets = int(packet[7:18], 2)
            index = 18
            for _ in range(number_of_packets):
                subpacket_version, subpacket_length = parse_packet(packet[index:])
                version += subpacket_version
                index += subpacket_length
            packet_length = index
    else:
        number, packet_length = parse_literal_packet(packet)
    return version, packet_length


def parse_literal_packet(packet):
    assert int(packet[3:6], 2) == 4
    done = False
    index = 6
    number = ""
    while not done:
        done = packet[index] == "0"
        number += packet[index + 1 : index + 5]
        index += 5
    number = int(number, 2)
    return number, index


v, _ = parse_packet(binary_string)
print(v)
