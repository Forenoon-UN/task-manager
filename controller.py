# ============================================================
#  controller.py  —  Controller Layer (MVC)
#  منطق التحكم: إضافة، حذف، تعديل، عرض المهام
# ============================================================

from models import User, Task


class TaskController:
    def __init__(self):
        self._users: list[User] = []
        self._tasks: list[Task] = []
        self._next_user_id = 1
        self._next_task_id = 1
        self.current_user: User = None

        # مستخدم افتراضي للتجربة
        self._register_default_user()

    # ── المستخدمون ──────────────────────────────────────────

    def _register_default_user(self):
        user = User(self._next_user_id, "admin", "1234")
        self._users.append(user)
        self._next_user_id += 1

    def login(self, username: str, password: str) -> bool:
        for user in self._users:
            if user.login(username, password):
                self.current_user = user
                return True
        return False

    def logout(self):
        self.current_user = None

    # ── المهام ──────────────────────────────────────────────

    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(self._next_task_id, title, description, self.current_user.user_id)
        self._tasks.append(task)
        self._next_task_id += 1
        return task

    def get_tasks(self) -> list[Task]:
        """إرجاع مهام المستخدم الحالي فقط"""
        return [t for t in self._tasks if t.user_id == self.current_user.user_id]

    def edit_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        task = self._find_task(task_id)
        if task:
            task.edit(title, description)
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False

    def mark_complete(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task:
            task.mark_complete()
            return True
        return False

    def _find_task(self, task_id: int) -> Task:
        for t in self.get_tasks():
            if t.task_id == task_id:
                return t
        return None
