# ============================================================
#  view.py  —  View Layer (MVC)
#  واجهة المستخدم عبر سطر الأوامر
# ============================================================

from controller import TaskController


class TaskView:
    def __init__(self):
        self.controller = TaskController()

    # ── تشغيل التطبيق ───────────────────────────────────────

    def run(self):
        print("=" * 45)
        print("   📝  نظام إدارة المهام  —  Task Manager")
        print("=" * 45)
        if self._login():
            self._main_menu()
        else:
            print("❌ بيانات الدخول خاطئة. إلى اللقاء!")

    # ── تسجيل الدخول ────────────────────────────────────────

    def _login(self) -> bool:
        print("\n🔐 تسجيل الدخول")
        username = input("اسم المستخدم: ").strip()
        password = input("كلمة المرور : ").strip()
        if self.controller.login(username, password):
            print(f"\n✅ مرحباً {username}!\n")
            return True
        return False

    # ── القائمة الرئيسية ────────────────────────────────────

    def _main_menu(self):
        while True:
            print("-" * 45)
            print("1️⃣  إضافة مهمة جديدة")
            print("2️⃣  عرض جميع المهام")
            print("3️⃣  تعديل مهمة")
            print("4️⃣  حذف مهمة")
            print("5️⃣  تعيين مهمة كمكتملة")
            print("0️⃣  خروج")
            print("-" * 45)
            choice = input("اختر: ").strip()

            if   choice == "1": self._add_task()
            elif choice == "2": self._show_tasks()
            elif choice == "3": self._edit_task()
            elif choice == "4": self._delete_task()
            elif choice == "5": self._complete_task()
            elif choice == "0":
                print("👋 إلى اللقاء!")
                break
            else:
                print("⚠️  اختيار غير صحيح، حاول مجدداً.")

    # ── العمليات ────────────────────────────────────────────

    def _add_task(self):
        print("\n➕ إضافة مهمة")
        title = input("العنوان  : ").strip()
        desc  = input("الوصف    : ").strip()
        task  = self.controller.add_task(title, desc)
        print(f"✅ تمت الإضافة: {task.title}\n")

    def _show_tasks(self):
        tasks = self.controller.get_tasks()
        print(f"\n📋 مهامك ({len(tasks)}):")
        if not tasks:
            print("  لا توجد مهام بعد.")
        for t in tasks:
            print(f"  {t}")
        print()

    def _edit_task(self):
        self._show_tasks()
        try:
            task_id = int(input("رقم المهمة للتعديل: "))
            title   = input("العنوان الجديد (اتركه فارغاً للإبقاء): ").strip() or None
            desc    = input("الوصف الجديد   (اتركه فارغاً للإبقاء): ").strip() or None
            if self.controller.edit_task(task_id, title, desc):
                print("✅ تم التعديل.\n")
            else:
                print("❌ لم يُعثر على المهمة.\n")
        except ValueError:
            print("⚠️  أدخل رقماً صحيحاً.\n")

    def _delete_task(self):
        self._show_tasks()
        try:
            task_id = int(input("رقم المهمة للحذف: "))
            if self.controller.delete_task(task_id):
                print("✅ تم الحذف.\n")
            else:
                print("❌ لم يُعثر على المهمة.\n")
        except ValueError:
            print("⚠️  أدخل رقماً صحيحاً.\n")

    def _complete_task(self):
        self._show_tasks()
        try:
            task_id = int(input("رقم المهمة لتعيينها كمكتملة: "))
            if self.controller.mark_complete(task_id):
                print("✅ تم تعيين المهمة كمكتملة.\n")
            else:
                print("❌ لم يُعثر على المهمة.\n")
        except ValueError:
            print("⚠️  أدخل رقماً صحيحاً.\n")


# ── نقطة البداية ────────────────────────────────────────────
if __name__ == "__main__":
    app = TaskView()
    app.run()
