# restaurant-queuing-simulation
this project is to determine, through simulation, which queuing and table configurations minimize average customer waiting time while maintaining high table utilization for different restaurant types.
🚀 Quick Start (Terminal Method)
This is the fastest way to run the simulation without needing a complex coding environment.
1. Prerequisites
   Ensure you have Python 3 installed on your computer.
   Download the following three files into the same folder:
     simulation.py (The program code)
     restaurant.txt (Your table configurations)
     customers.txt (Your customer arrival data)

2. How to Run
   1. Open your Terminal (Command Prompt on Windows, Terminal on Mac/Linux).
   2. Navigate to your folder using the cd command:
      Bash
      cd path/to/your/folder
   3. Start the simulation:
      Bash
      python simulation.py
   4. Choose a Comparison: The program will prompt you to select one of the three research scenarios defined in our project plan:
      Press 1: HK-Style Cafe (Single Queue vs. Size-Based).
      Press 2: Dim Sum Hall (Coarse vs. Fine-Grained Queues).
      Press 3: High-End Restaurant (Standard vs. VIP Priority).

🛠️ Customizing the Simulation
You can create your own "Case Studies" by editing the input files with any text editor (like Notepad or TextEdit).

Edit restaurant.txt (Tables)
List each table's capacity on a new line.
  Example: A 2 followed by a 4 means your restaurant has one 2-seater and one 4-seater.
  
Edit customers.txt (Arrivals)
Enter data in the format: Arrival_Time Group_Size Dining_Duration.
  Example: 10 4 30 means at time unit 10, a group of 4 arrives and eats for 30 units.
  
📊 Understanding the Output Report
After the simulation runs, it will generate a report showing:
  Average Wait Time: How long customers waited before being seated.
  Table Utilization: How efficiently your tables were used (expressed as a percentage).
  Max Queue Length: The highest number of groups waiting at once—crucial for managing limited space in high-density areas like Hong Kong.
  Service Level: The percentage of groups seated within a "reasonable" time frame.
