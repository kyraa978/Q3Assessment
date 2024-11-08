import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Function to create table and insert questions for each category
def create_table_and_insert_questions(table_name, questions):
    # Create the table only if it does not exist
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')

    # Insert questions into the table
    for question, option_a, option_b, option_c, option_d, correct_answer in questions:
        cursor.execute(f'''
        INSERT INTO {table_name} (question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    
    conn.commit()
    print(f"Questions have been inserted into the {table_name} table.")

# Define sample questions for each category
ds3850_questions = [
    ("What is the correct syntax to define a function in Python?",
     "def function_name():",
     "function function_name():",
     "function_name():",
     "define function_name():",
     "A"),

    ("Which data type is used to store text in Python?",
     "int",
     "float",
     "str",
     "bool",
     "C"),

    ("How do you create a list in Python?",
     "[1, 2, 3]",
     "(1, 2, 3)",
     "{1: 'a', 2: 'b'}",
     "1, 2, 3",
     "A"),

    ("What is the result of the following expression: 5 % 2?",
     "2.5",
     "3",
     "1",
     "0",
     "C"),

    ("Which keyword is used to define a loop that executes a specific number of times?",
     "for",
     "while",
     "do-while",
     "repeat-until",
     "A"),

    ("How do you check if a variable 'x' is equal to 10?",
     "x == 10",
     "x = 10",
     "x > 10",
     "x < 10",
     "A"),

    ("What is the purpose of the 'break' statement in Python?",
     "To continue to the next iteration of a loop",
     "To exit the current loop",
     "To skip the current iteration of a loop",
     "To define a new block of code",
     "B"),

    ("What is the output of the following code?\n\nprint('Hello' + ' ' + 'World')",
     "HelloWorld",
     "Hello World",
     "Hello + World",
     "Error",
     "B"),

    ("Which data structure is used to store key-value pairs?",
     "List",
     "Tuple",
     "Set",
     "Dictionary",
     "D"),

    ("What is the correct way to import a module named 'my_module' in Python?",
     "import my_module",
     "include my_module",
     "use my_module",
     "require my_module",
     "A")
]

excel_questions = [
    ("Which Excel function is used to calculate the average of a range of numbers?", "AVERAGE()", "SUM()", "MEAN()", "MEDIAN()", "A"),
    ("Which Excel tool is best for summarizing large datasets?", "Pivot Table", "Conditional Formatting", "Data Validation", "Filter", "A"),
    ("What function would you use to count cells based on specific criteria in Excel?", "COUNTIF()", "COUNT()", "COUNTA()", "SUMIF()", "A"),
    ("Which Excel chart type is best for showing the distribution of data?", "Pie Chart", "Line Chart", "Histogram", "Bar Chart", "C"),
    ("How would you calculate the correlation between two sets of data in Excel?", "CORREL()", "COVAR()", "VARIANCE()", "TREND()", "A"),
    ("Which Excel function is used to calculate the standard deviation of a range of numbers?", "STDEV()", "VAR()", "MODE()", "MEDIAN()", "A"),
    ("What is the purpose of the VLOOKUP function in Excel?", "To search for a specific value in a table and return a corresponding value", "To sort data in ascending or descending order", "To create a chart based on data in a range", "To format cells with specific colors or patterns", "A"),
    ("How do you freeze panes in Excel to keep headers visible while scrolling?", "Select the row below the headers and go to View -> Freeze Panes", "Select the column to the right of the headers and go to View -> Freeze Panes", "Select the entire worksheet and go to Format -> Freeze Panes", "Select the cell in the top-left corner of the data and go to Data -> Freeze Panes", "A"),
    ("What is the purpose of the IF function in Excel?", "To perform logical tests and return different values based on the result", "To count the number of cells that meet a specific criteria", "To sum values in a range based on certain conditions", "To sort data in ascending or descending order", "A"),
    ("Which Excel function is used to calculate the present value of a series of future payments?", "PV()", "FV()", "PMT()", "RATE()", "A")
]

biology_questions = [
    ("What is the basic unit of life?", "Atom", "Molecule", "Cell", "Organ", "C"),
    ("What process do plants use to convert sunlight into energy?", "Respiration", "Photosynthesis", "Fermentation", "Digestion", "B"),
    ("Which part of the cell contains genetic material?", "Nucleus", "Cytoplasm", "Cell membrane", "Mitochondria", "A"),
    ("What is the powerhouse of the cell?", "Nucleus", "Endoplasmic reticulum", "Mitochondria", "Golgi apparatus", "C"),
    ("What type of organism is a bacterium?", "Eukaryote", "Prokaryote", "Fungi", "Virus", "B"),
    ("What is the process by which organisms maintain a stable internal environment?", "Homeostasis", "Metabolism", "Excretion", "Reproduction", "A"),
    ("What is the process of DNA replication called?", "Transcription", "Translation", "DNA replication", "Mitosis", "C"),
    ("What is the primary function of the circulatory system?", "To transport oxygen and nutrients to cells", "To eliminate waste products from the body", "To regulate body temperature", "To protect the body from infection", "A"),
    ("What is the largest organ in the human body?", "Liver", "Heart", "Lungs", "Skin", "D"),
    ("What is the process of cell division that results in two identical daughter cells?", "Mitosis", "Meiosis", "Binary fission", "Budding", "A")
]

statistics_questions = [
    ("What is the measure of central tendency that is most affected by outliers?", "Mean", "Median", "Mode", "Range", "A"),
    ("Which statistical measure is used to describe the variability of a dataset?", "Mean", "Median", "Mode", "Standard deviation", "D"),
    ("What is the probability of flipping a coin and getting heads?", "0.5", "0.25", "0.75", "1", "A"),
    ("What is the shape of a normal distribution?", "Skewed left", "Skewed right", "Bell-shaped", "Uniform", "C"),
    ("What is the correlation coefficient used to measure?", "The strength and direction of the linear relationship between two variables", "The average of a set of numbers", "The middle value of a dataset", "The most frequent value in a dataset", "A"),
    ("What is the p-value in hypothesis testing?", "The probability of obtaining a test statistic as extreme as the observed one, assuming the null hypothesis is true", "The probability of rejecting the null hypothesis", "The probability of accepting the null hypothesis", "The probability of making a Type I error", "A"),
    ("What is a confidence interval?", "A range of values that is likely to contain the true population parameter with a certain level of confidence", "A single value that is used to estimate a population parameter", "A measure of the variability of a sample", "A measure of the central tendency of a sample", "A"),
    ("What is the difference between a population and a sample?", "A population is the entire group of interest, while a sample is a subset of the population", "A population is a subset of a sample", "There is no difference between a population and a sample", "A population is always larger than a sample", "A"),
    ("What is the purpose of hypothesis testing?", "To determine if a sample provides enough evidence to reject a null hypothesis", "To calculate the mean, median, and mode of a dataset", "To create a visual representation of data", "To measure the variability of a dataset", "A"),
    ("What is the difference between a one-tailed and a two-tailed test?", "A one-tailed test tests for a specific direction of the effect, while a two-tailed test tests for any difference", "A one-tailed test is more powerful than a two-tailed test", "A two-tailed test is more powerful than a one-tailed test", "There is no difference between a one-tailed and a two-tailed test", "A")
]

communication_questions = [
    ("What is the primary purpose of effective communication?", "To convey information accurately", "To persuade others to agree with your viewpoint", "To build relationships", "All of the above", "D"),
    ("Which communication channel is best for conveying complex information that requires detailed explanation?", "Email", "Phone call", "Face-to-face meeting", "Text message", "C"),
    ("What is nonverbal communication?", "Communication through spoken words", "Communication through written words", "Communication through body language, facial expressions, and tone of voice", "Communication through electronic devices", "C"),
    ("What is active listening?", "Paying attention to the speaker and asking clarifying questions", "Interrupting the speaker to share your own thoughts", "Thinking about your response while the speaker is talking", "Focusing on the speaker's body language", "A"),
    ("What is the difference between verbal and nonverbal communication?", "Verbal communication uses words, while nonverbal communication uses body language and other cues", "Verbal communication is more important than nonverbal communication", "Nonverbal communication is more important than verbal communication", "Verbal and nonverbal communication are equally important", "A"),
    ("What is the purpose of a persuasive communication strategy?", "To convince others to adopt a particular viewpoint or take a specific action", "To inform others about a particular topic", "To build relationships with others", "To entertain others", "A"),
    ("What is the importance of clear and concise communication?", "It helps to avoid misunderstandings", "It saves time and effort", "It makes a positive impression", "All of the above", "D"),
    ("What is the difference between formal and informal communication?", "Formal communication follows specific rules and protocols, while informal communication is more casual", "Formal communication is always written, while informal communication is always spoken", "Formal communication is used for personal relationships, while informal communication is used for professional relationships", "Formal communication is more important than informal communication", "A"),
    ("What is the purpose of feedback in communication?", "To provide constructive criticism and suggestions for improvement", "To praise the other person", "To criticize the other person", "To avoid conflict", "A"),
    ("What is the importance of intercultural communication?", "It helps to bridge cultural differences and promote understanding", "It is only important for international businesses", "It is not important for domestic communication", "It is only important for people who travel internationally", "A")
]

# Create tables and insert questions for each category
create_table_and_insert_questions("DS3850", ds3850_questions)
create_table_and_insert_questions("DS3841", excel_questions)
create_table_and_insert_questions("BIO1020", biology_questions)
create_table_and_insert_questions("ECON3610", statistics_questions)
create_table_and_insert_questions("COMM2025", communication_questions)

# Function to list all tables in the database, excluding sqlite_sequence
def list_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = cursor.fetchall()
    print("Tables in the database (excluding internal sqlite_sequence):")
    for table in tables:
        print(table[0])

# List tables
list_tables()

# Close the connection
conn.close()