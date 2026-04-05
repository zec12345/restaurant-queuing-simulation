# COMP1110_Group_Project
this project is to determine, through simulation, which queuing and table configurations minimize average customer waiting time while maintaining high table utilization for different restaurant types.

Project Topic: (C) Restaurant queue simulation
Team members: 
Cheung Tsun Ho
Man Hoi Ling Kaitlyn
Oey Jade Evangeline
Tang Chun Lok
Tang Man Yui

Introduction: 
1. Background
   Efficient table management is a critical issue for restaurants, especially in a high-density urban area such as Hong Kong, where space is often limited yet there is a high volume of customers. This tension is most visible during peak hour, where restaurants must balance the trade-off between minimising customer
   wait times and maximising table usage. Inefficient table management directly impacts business performance, leads to dissatisfaction among customers and lost revenue due to slower rate of turnover. Therefore, there is a need to find a balance between queue management strategies and the needs of various client group
   sizes.
   Through creating a discrete event simulation, we aim to replicate real-world arrival scenarios and seating constraints for different types of restaurants to determine the optimal queue management strategies for each. We could therefore also investigate how a particular restaurant arrangement influences various
   measures, such as average waiting time, table usage, and number of groups served. Ultimately, this helps the restaurant make informed decisions to improve business performance and customer experience.

2. Purpose of each file
   1. main.py: we only have one core coding file to deal with the whole simulation. It contains a function that can read two information text files (customers.txt and restaurant.txt), a few function that run the whole process and a function that generates a matrics report. The program mainly manage three different types of restaurants commonly found in Hong Kong, and comparing how varying different factors will affect the average waiting time of customers. Specifically, we will compare a Hong Kong-styled, dim sum hall, and a high-end restaurant, as they have distinct queuing characteristics as outlined below.
      
   - Hong Kong-styled cafe
      Hong Kong-styled cafes are often fast-paced and busy, with many small tables and small groups of people.
      * Variation A: Only FCFS queueing
      * Variation B: If queue ≥ 7 groups of people use size-based grouping, else FCFS queueing
      * Research Question: Which setup minimizes wait time during lunch rush?

   - Dim Sum Hall
      Traditional dim sum restaurants in Hong Kong are characterised by their large seating capacities, long dining duration and a mix of small and large family groups.
     * Variation A: Coarse queues (1-6, 7+)
     * Variation B: Fine-grained queues (1-2, 3-4, 5-6, 7+)
     * Research Question: Does finer queue splitting improve table matching?

   - High-End Restaurant
        High-End restaurants prioritise customer experience and often operate with a VIP membership system with limited walk-in seats to maintain exclusivity.
        * Variation A: 100% walk-ins with FCFS queueing
        * Variation B: 90% walk-ins with FCFS queueing + 10% VIP priority queueing
        * Research Question: How do VIP priority queues impact regular customer wait times?
   2. customers.txt: As the program is just a replication of a real world arrival scenarios and a simulation for different types of restaurants. It cannot randomly generate the situation of customers by the program itself, this text file provides the information of customers that the program will follow including which time unit each customers arrive, how many people in each customers groups and their dining duration.
      
   3. restaurant.txt: Similar with customers.txt, this text file is also editable by users, it stores the information of the numbers of table that a restaurant contains and their capacity (how many customers that a table can serve).
      
🚀 Quick Start 
1. Prerequisites
   Ensure you have Python 3 installed on your computer.
   Download the following three files from the "code" directory, after downloading make sure they are on the same directory on your computers:
     simulation.py (The program code)
     restaurant.txt (Your table configurations)
     customers.txt (Your customer arrival data)

2. How to Run
   1. Open your Terminal (Command Prompt on Windows, Terminal on Mac/Linux).
   2. Navigate to your folder using the cd command:
      `cd path/to/your/folder`
   4. Start the simulation:
      `python main.py`
   5. Choose a Comparison: The program will prompt you to select one of the three research scenarios defined in our project plan:
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
  Average Wait Time: Average time that customers waited before being seated.
  Table Utilization: How efficiently your tables were used (expressed as a percentage).
  Max Queue Length: The highest number of groups waiting at once—crucial for managing limited space in high-density areas like Hong Kong.
  Service Level: The percentage of groups seated within a "reasonable" time frame (waiting time <=10 units).
