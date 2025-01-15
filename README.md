# **PubMed Paper Fetcher**

## **Description**
The PubMed Research Retriever is a Python tool that retrieves research papers from PubMed based on user-defined queries, focusing on papers related to pharmaceutical and biotech industries. It filters results to identify authors affiliated with companies, and allows users to save the data to a CSV file. The tool includes a command-line interface (CLI) with options for debugging and error handling, making it a useful resource for researchers seeking relevant publications efficiently.

---

## **Project Organization**
The code is organized into two main parts:
### **1. Module (`pubmed_utils.py`)**
This is a utility module containing the functions to interact with the PubMed API and process the data. The key functions in this module include:
   - `fetch_pubmed_ids`: Fetches PubMed IDs for a given search query.
   - `fetch_paper_details`: Retrieves detailed paper information for each PubMed ID.
   - `parse_paper_details`: Parses the XML response from PubMed and extracts the required paper details.
   - `filter_non_academic_authors`: Identifies non-academic authors based on company keywords.
   - `save_to_csv`: Saves the retrieved data into a CSV file.


### **2. Module 2(`main.py`)**
The entry point for the program, which provides a command-line interface (CLI) for the user. The script accepts a PubMed query, an optional file to save results, and an option to enable debug mode.
---

## **Installation**

### **Prerequisites**
- Python 3.8 or later
- Poetry (for dependency management)

### **Steps**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/RAHUL-299/pharma-research-fetcher
   cd pharma-research-fetcher
   ```

2. **Install Dependencies**
   If Poetry is not installed, you can install it using:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   Then, install project dependencies:
   ```bash
   poetry install
   ```

3. **Activate Virtual Environment**
   ```bash
   poetry shell
   ```

---

## **Run the program to fetch papers based on a query:
bash
Copy code
**

### **Basic Usage**
Run the program from the command line:
```bash
poetry run get-papers-list "your query here"
```

### ** To save results to a CSV file:**
```bash
poetry run python my_project/main.py "cancer research" -f results.csv
```
This will execute the program and save the results to results.csv.
### ** To enable debug mode:**
Enable debug mode to print detailed logs:
```bash
poetry run python my_project/main.py "cancer research" -d
```
### **Tools and Libraries Used**
1.Poetry: A Python dependency manager used to install and manage project dependencies. Poetry Documentation
2.Requests: A simple and elegant HTTP library for Python, used to make requests to the PubMed API. Requests Documentation
3.XML ElementTree: A standard Python library for parsing and creating XML. Used to parse PubMed's XML responses.
4.CSV: A Python standard library for handling CSV files.

### **Functionality**
1.Fetch Research Papers: The program queries the PubMed database based on a user-defined search query.
2.Save Results: Users can choose to save the fetched results to a CSV file for further analysis.
3.Debug Mode: Debugging is available to print detailed logs for troubleshooting.
4.Non-academic Author Identification: The program identifies authors affiliated with pharmaceutical or biotech companies based on company keywords (e.g., "Pharma", "Biotech", "HealthTech").


### **LLM Assistance**
This project was developed with assistance from **OpenAI's GPT-4**, which helped in:
- Refactoring code for readability and maintainability.
- Designing robust error-handling mechanisms.
- Creating this README.md file with structure tweaks and wording suggestions.

Learn more about GPT-4: [https://openai.com/gpt](https://openai.com/gpt)

---

