# Quản lý danh sách công việc
def display_menu():
    print("\n--- Quản Lý Danh Sách Công Việc ---")
    print("1. Thêm công việc")
    print("2. Hiển thị danh sách công việc")
    print("3. Đánh dấu công việc đã hoàn thành")
    print("4. Xóa công việc")
    print("5. Thoát")

def add_task(task_list):
    task = input("Nhập công việc mới: ")
    task_list.append({"task": task, "completed": False})
    print(f"Đã thêm: {task}")

def show_tasks(task_list):
    if not task_list:
        print("Danh sách công việc trống.")
    else:
        print("\nDanh sách công việc:")
        for i, task in enumerate(task_list, start=1):
            status = "Đã hoàn thành" if task["completed"] else "Chưa hoàn thành"
            print(f"{i}. {task['task']} - {status}")

def mark_task_complete(task_list):
    show_tasks(task_list)
    try:
        task_num = int(input("Nhập số thứ tự công việc muốn đánh dấu hoàn thành: "))
        if 1 <= task_num <= len(task_list):
            task_list[task_num - 1]["completed"] = True
            print("Đã đánh dấu công việc hoàn thành.")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def delete_task(task_list):
    show_tasks(task_list)
    try:
        task_num = int(input("Nhập số thứ tự công việc muốn xóa: "))
        if 1 <= task_num <= len(task_list):
            removed_task = task_list.pop(task_num - 1)
            print(f"Đã xóa: {removed_task['task']}")
        else:
            print("Số thứ tự không hợp lệ.")
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")

def main():
    task_list = []
    while True:
        display_menu()
        choice = input("Chọn một tùy chọn (1-5): ")
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            show_tasks(task_list)
        elif choice == "3":
            mark_task_complete(task_list)
        elif choice == "4":
            delete_task(task_list)
        elif choice == "5":
            print("Chương trình kết thúc. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()
