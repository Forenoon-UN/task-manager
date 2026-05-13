# ============================================================
#  models.py  —  Model Layer (MVC)
#  يحتوي على فئتي User و Task (البيانات فقط)
# ============================================================

class User:
    def __init__(self, user_id: int, username: str, password: str):
        self.user_id  = user_id
        self.username = username
        self.password = password

    def login(self, username: str, password: str) -> bool:
        """تحقق من بيانات الدخول — يرجع True إذا صحيحة"""
        return self.username == username and self.password == password

    def __str__(self):
        return f"User({self.user_id}, {self.username})"


class Task:
    def __init__(self, task_id: int, title: str, description: str = "", user_id: int = None):
        self.task_id     = task_id
        self.title       = title
        self.description = description
        self.is_completed = False
        self.user_id     = user_id

    def mark_complete(self):
        """تعيين المهمة كمكتملة"""
        self.is_completed = True

    def edit(self, title: str = None, description: str = None):
        """تعديل عنوان أو وصف المهمة"""
        if title:
            self.title = title
        if description:
            self.description = description

    def __str__(self):
        status = "✔ مكتملة" if self.is_completed else "○ غير مكتملة"
        return f"[{self.task_id}] {self.title} | {status}\n    {self.description}"
