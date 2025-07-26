class Train:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.seats = ["Available"] * total_seats

    def display_seats(self):
        print(f"\nSeat Layout for {self.name}:")
        for i, status in enumerate(self.seats, start=1):
            print(f"Seat {i}: {status}")
        print()

    def book_seat(self, seat_number):
        if 1 <= seat_number <= self.total_seats:
            if self.seats[seat_number - 1] == "Available":
                self.seats[seat_number - 1] = "Booked"
                print(f"✅ Seat {seat_number} successfully booked.\n")
            else:
                print(f"⚠️ Seat {seat_number} is already booked.\n")
        else:
            print("❌ Invalid seat number.\n")

    def available_seats(self):
        available = self.seats.count("Available")
        print(f"🪑 Total Available Seats: {available}\n")


# --- Main Program ---

def main():
    train = Train("Express 101", 10)

    while True:
        print("===== Train Seat Information System =====")
        print("1. Display Seat Layout")
        print("2. Book a Seat")
        print("3. Show Available Seats")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            train.display_seats()
        elif choice == "2":
            try:
                seat_num = int(input("Enter seat number to book: "))
                train.book_seat(seat_num)
            except ValueError:
                print("❌ Please enter a valid number.\n")
        elif choice == "3":
            train.available_seats()
        elif choice == "4":
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
