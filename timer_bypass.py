import time

# 🚀 PROOF OF CONCEPT: PythonAnywhere Threading Limit Bypass
# Developed by: DeadEnd Systems (Arbaj-Dev)
# Purpose: Creating a custom task execution engine to bypass server restrictions.

# Custom dictionary to store tasks and their execution time
task_queue = {}

def schedule_task(task_id, delay_seconds, action_function):
    """Schedules a task to run after X seconds without using threading.Timer"""
    execute_time = time.time() + delay_seconds
    task_queue[task_id] = {"execute_time": execute_time, "action": action_function}
    print(f"[+] Task {task_id} scheduled for {delay_seconds} seconds later.")

def run_custom_loop():
    """Main execution engine that runs continuously to check and execute tasks"""
    print("[*] Custom Timer Engine Started. Bypassing Background Limits...")
    while True:
        current_time = time.time()
        tasks_to_remove = []

        for task_id, task_data in task_queue.items():
            if current_time >= task_data["execute_time"]:
                print(f"[!] Executing Task: {task_id}")
                # Execute the scheduled action
                task_data["action"]() 
                tasks_to_remove.append(task_id)
        
        # Clean up executed tasks
        for task_id in tasks_to_remove:
            del task_queue[task_id]
            
        # Prevent CPU overload
        time.sleep(1) 

# Example usage of the engine (Without using blocked threads)
# schedule_task("auto_delete_msg_101", 600, delete_message_function)
# run_custom_loop()
