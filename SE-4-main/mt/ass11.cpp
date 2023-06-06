#include <iostream>
#include <fstream>
using namespace std;
struct Student {
    int rollNumber;
    string name;
    string division;
    string address;
};
void addStudentRecord() {
    Student student;

    cout << "Enter Roll Number: ";
    cin >> student.rollNumber;
    cin.ignore();    cout << "Enter Name: ";
    getline(cin, student.name);
    cout << "Enter Division: ";
    getline(cin, student.division);
    cout << "Enter Address: ";
    getline(cin, student.address);
ofstream outFile("student.txt", ios::app); 
    if (outFile.is_open()) {
        outFile << student.rollNumber << "," << student.name << "," << student.division << "," << student.address << endl;
        outFile.close();
        cout << "Student record added successfully!" << endl;
    } else {
        cout << "Error: Unable to open file." << endl;
    }
}
void deleteStudentRecord() {
    int rollNumber;
    cout << "Enter Roll Number to delete: ";
    cin >> rollNumber;
    ifstream inFile("student.txt");
    ofstream tempFile("temp.txt");
    bool recordFound = false;
    if (inFile.is_open() && tempFile.is_open()) {
        string line;
        while (getline(inFile, line)) {
            int currentRollNumber = stoi(line.substr(0, line.find(',')));
            if (currentRollNumber != rollNumber) {
                tempFile << line << endl;
            } else {
                recordFound = true;
            }
        }
        inFile.close();
        tempFile.close();
        remove("student.txt");
        rname("temp.txt", "student.txt");
        if (recordFound) {
            cout << "Student record deleted successfully!" << endl;
        } else {
            cout << "Student record not found." << endl;
        }
    } else {
        cout << "Error: Unable to open file." << endl;
    }
}
void displayStudentInfo() {
    int rollNumber;
    cout << "Enter Roll Number to search: ";
    cin >> rollNumber;
    ifstream inFile("student.txt");
    if (inFile.is_open()) {
        bool recordFound = false;
        string line;
        while (getline(inFile, line)) {
            int currentRollNumber = stoi(line.substr(0, line.find(',')));
            if (currentRollNumber == rollNumber) {
                recordFound = true;
                cout << "Student Information:" << endl;
                cout << line << endl;
                break;
            }
        }
        inFile.close();
        if (!recordFound) {
            cout << "Student record not found." << endl;
        }
    } else {
        cout << "Error: Unable to open file." << endl;
    }
}
int main() {
    int choice;
    while (true) {
        cout << "Student Information System" << endl;
        cout << "1. Add Student Record" << endl;
        cout << "2. Delete Student Record" << endl;
        cout << "3. Display Student Information" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice) {
            case 1:
                addStudentRecord();
                break;
            case 2:
                deleteStudentRecord();
                break;
            case 3:
                displayStudentInfo();
                break;
            case 4:
                cout << "Exiting the program..." << endl;
                return 0;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
        cout << endl;
    }
    return 0;
}