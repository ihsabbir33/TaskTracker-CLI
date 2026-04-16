\# 📝 Task Tracker CLI



A simple and powerful \*\*Command Line Interface (CLI)\*\* application to manage your daily tasks efficiently.



\---



\## 🚀 Features



\* ➕ Add new tasks

\* ✏️ Update existing tasks

\* ❌ Delete tasks

\* 🔄 Mark tasks as \*in-progress\* or \*done\*

\* 📋 List all tasks

\* 🔍 Filter tasks by status



\---



\## 🛠️ Technologies Used



\* Python

\* JSON (for data storage)

\* argparse (CLI argument handling)



\---



\## 📦 Installation



1\. Clone the repository:



```bash

git clone https://github.com/ihsabbir33/TaskTracker-CLI.git

cd TaskTracker-CLI

```



2\. Run the application:



```bash

python task\_cli.py

```



\---



\## ⚙️ Usage



\### ➕ Add Task



```bash

python task\_cli.py add --desc "Buy groceries"

```



\### 📋 List Tasks



```bash

python task\_cli.py list

```



\### 🔄 Mark In Progress



```bash

python task\_cli.py mark-in-progress --id 1

```



\### ✅ Mark Done



```bash

python task\_cli.py mark-done --id 1

```



\### ✏️ Update Task



```bash

python task\_cli.py update --id 1 --desc "Updated task"

```



\### ❌ Delete Task



```bash

python task\_cli.py delete --id 1

```



\### 🔍 Filter Tasks



```bash

python task\_cli.py list --status done

python task\_cli.py list --status todo

python task\_cli.py list --status in-progress

```



\---



\## 📁 Project Structure



```

task-tracker/

│

├── task\_cli.py

├── tasks.json

└── README.md

```



\---



\## ⚠️ Notes



\* `tasks.json` is used to store tasks locally

\* If the file is empty or corrupted, the app will handle it automatically



\---



\## 💡 Future Improvements



\* GUI version (Tkinter)

\* Export tasks to file

\* Add due dates \& priority



\---



\## 👨‍💻 Author



\*\*Sabbir Ahmed\*\*



GitHub: https://github.com/ihsabbir33



\---



\## ⭐ Show your support



If you like this project, give it a ⭐ on GitHub!



