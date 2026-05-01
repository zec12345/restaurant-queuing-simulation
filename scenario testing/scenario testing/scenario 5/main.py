import os
import math

class CustomerGroup:
    def __init__(self, arrival_time, size, dining_duration, is_vip=False):
        self.arrival_time = arrival_time
        self.size = size
        self.dining_duration = dining_duration
        self.is_vip = is_vip
        self.wait_time = 0
        self.seated_time = None
        self.leave_time = None

class Table:
    def __init__(self, table_id, capacity):
        self.table_id = table_id
        self.capacity = capacity
        self.current_group = None
        self.occupied_until = 0
        self.total_occupied_time = 0

class RestaurantSimulation:
    def __init__(self, strategy_type, queue_config):
        self.strategy_type = strategy_type  # FCFS, Size-Based, or VIP
        self.queue_config = queue_config    # List of tuples (min_size, max_size)
        self.tables = []
        self.queues = {i: [] for i in range(len(queue_config))}
        self.completed_groups = []
        self.current_time = 0

    def load_restaurant(self, filename):
        """Reads table capacities from file."""
        if not os.path.exists(filename): return
        with open(filename, 'r') as f:
            for i, line in enumerate(f):
                capacity = int(line.strip())
                self.tables.append(Table(i, capacity))

    def load_customers(self, filename, vip_percent=0):
        """Reads arrival_time, size, duration from file."""
        customers = []
        if not os.path.exists(filename): return customers
        with open(filename, 'r') as f:
            for line in f:
                parts = list(map(int, line.split()))
                if len(parts) == 3:
                    arrival, size, duration = parts
                    is_vip = (len(customers) % 10 < (vip_percent / 10)) # Simple VIP toggle
                    customers.append(CustomerGroup(arrival, size, duration, is_vip))
        return sorted(customers, key=lambda x: x.arrival_time)

    def get_queue_index(self, group):
        """Assigns group to a queue based on size ranges."""
        for i, (min_s, max_s) in enumerate(self.queue_config):
            if min_s <= group.size <= max_s:
                return i
        return len(self.queue_config) - 1 # Default to last queue

    def run(self, customers):
        max_queue_lengths = {i: 0 for i in range(len(self.queue_config))}
        arrival_idx = 0
        
        # Run until all customers are served
        while arrival_idx < len(customers) or any(self.queues.values()) or any(t.current_group for t in self.tables):
            
            # 1. Process Arrivals
            while arrival_idx < len(customers) and customers[arrival_idx].arrival_time <= self.current_time:
                group = customers[arrival_idx]
                q_idx = self.get_queue_index(group)
                
                # VIP logic: Insert at front if strategy allows
                if self.strategy_type == "VIP" and group.is_vip:
                    self.queues[q_idx].insert(0, group)
                else:
                    self.queues[q_idx].append(group)
                arrival_idx += 1

            # Update max queue lengths
            for i in self.queues:
                max_queue_lengths[i] = max(max_queue_lengths[i], len(self.queues[i]))

            # 2. Check for freeing tables
            for table in self.tables:
                if table.current_group and self.current_time >= table.occupied_until:
                    group = table.current_group
                    group.leave_time = self.current_time
                    self.completed_groups.append(group)
                    table.current_group = None

            # 3. Seat customers (Prioritize FCFS across all queues if standard FCFS)
            available_tables = sorted([t for t in self.tables if t.current_group is None], key=lambda x: x.capacity)
            
            for table in available_tables:
                best_group = None
                best_q_idx = -1

                # Logic: Find earliest group from queues that fits this table
                for q_idx in self.queues:
                    if self.queues[q_idx]:
                        candidate = self.queues[q_idx][0]
                        if candidate.size <= table.capacity:
                            if best_group is None or candidate.arrival_time < best_group.arrival_time:
                                best_group = candidate
                                best_q_idx = q_idx
                
                if best_group:
                    self.queues[best_q_idx].pop(0)
                    best_group.seated_time = self.current_time
                    best_group.wait_time = self.current_time - best_group.arrival_time
                    table.current_group = best_group
                    table.occupied_until = self.current_time + best_group.dining_duration
                    table.total_occupied_time += best_group.dining_duration

            self.current_time += 1

        return self.generate_report(max_queue_lengths)

    def generate_report(self, max_queues):
        total_wait = sum(g.wait_time for g in self.completed_groups)
        count = len(self.completed_groups)
        avg_wait = total_wait / count if count > 0 else 0
        
        total_possible_time = self.current_time * len(self.tables)
        actual_occupied = sum(t.total_occupied_time for t in self.tables)
        utilization = (actual_occupied / total_possible_time) * 100 if total_possible_time > 0 else 0
        
        service_level = (len([g for g in self.completed_groups if g.wait_time <= 10]) / count) * 100

        report = f"--- Simulation Results ({self.strategy_type}) ---\n"
        report += f"Groups Served: {count}\n"
        report += f"Average Wait Time: {avg_wait:.2f} units\n"
        report += f"Table Utilization: {utilization:.2f}%\n"
        report += f"Service Level (Wait <= 10): {service_level:.2f}%\n"
        report += f"Max Queue Lengths: {list(max_queues.values())}\n"
        return report

def main():
    print("Restaurant Queue Simulation Comparison")
    print("1. HK Cafe (FCFS vs Size-Based threshold)")
    print("2. Dim Sum Hall (Coarse vs Fine-Grained queues)")
    print("3. High-End (Standard vs VIP Priority)")
    choice = input("Select comparison to run (1/2/3): ")

    # Setup paths (ensure these files exist in your folder)
    cust_file = "customers.txt"
    rest_file = "restaurant.txt"

    if choice == '1':
        # Variation A: Pure FCFS
        simA = RestaurantSimulation("FCFS", [(1, 10)])
        # Variation B: Size-Based
        simB = RestaurantSimulation("Size-Based", [(1, 2), (3, 4), (5, 10)])
        title = "Comparison 1: Hong Kong Cafe"
    elif choice == '2':
        simA = RestaurantSimulation("Coarse", [(1, 6), (7, 20)])
        simB = RestaurantSimulation("Fine", [(1, 2), (3, 4), (5, 6), (7, 20)])
        title = "Comparison 2: Dim Sum Hall"
    else:
        simA = RestaurantSimulation("FCFS", [(1, 20)])
        simB = RestaurantSimulation("VIP", [(1, 20)]) # 10% VIP in logic
        title = "Comparison 3: High-End Restaurant"

    # Run A
    print(f"\nRunning {title} - Variation A...")
    customersA = simA.load_customers(cust_file)
    simA.load_restaurant(rest_file)
    print(simA.run(customersA))

    # Run B
    print(f"Running {title} - Variation B...")
    customersB = simB.load_customers(cust_file, vip_percent=(10 if choice == '3' else 0))
    simB.load_restaurant(rest_file)
    print(simB.run(customersB))

if __name__ == "__main__":
    main()