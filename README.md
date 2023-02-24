# Fetch Coding Exercise - Backend Software Engineering Internship

## Description
This project takes in a CSV file containing transaction records and manages the accounts following the rules when spending points.

### File Structure
The project has one main file where the application runs, `Main.py`, and a folder containing the following:
 - `PaymentNode.py` - Transaction node class that stores payer name, points available, and timestamp
 - `PaymentQueue.py` - FIFO Queue data structure that stores the transaction nodes in ascending order according to timestamp
 - `__init__.py` - allows importing `PaymentNode.py` and `PaymentQueue.py` into other files

### Project Process
First, the CSV file is inputted into `Main.py` and is transformed into a Pandas dataframe. Several operations are performed on the dataframe including sorting and reformatting the dates. Then, a FIFO (first-in, first-out) queue is instantiated to store the values in the dataframe. Queues allow you to remove nodes that were added first, which is great for this project as the oldest transactions should be removed first. The queue has an operation to spend points from the least recent timestamp to the most recent timestamp. Finally, an output will be printed to the console/command-line, the account summary of all users' total points.

### Running the project
In order to run the project, you can type in the following command into your command line interface. Make sure that you are in the same directory as `Main.py`.

```
python3 Main.py <*> <**>
```

 - `<*>` - insert the amount of points you want to spend here
 - `<**>` - insert the CSV file name that you want to process

## Prerequisites and Installation
You will need Python installed on your computer to run this project, as well as the Pandas library. To install Python, follow this [link](https://www.python.org/downloads/)

After installing Python onto your device, you can install the Pandas library using pip:
```
pip install pandas
```
