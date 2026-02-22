import sys
import os
import math
import random
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTextEdit, QLineEdit, QListWidget, QTableWidget, QTableWidgetItem,
    QComboBox, QCheckBox, QSlider, QProgressBar, QSpinBox, QDoubleSpinBox,
    QDateEdit, QTimeEdit, QDateTimeEdit, QTabWidget, QGroupBox, QRadioButton,
    QToolBar, QMenuBar, QMenu, QFileDialog, QMessageBox, QDialog,
    QFormLayout, QScrollArea, QGraphicsView, QGraphicsScene, QGraphicsRectItem,
    QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem, QSplitter,
    QStatusBar, QDockWidget, QCalendarWidget, QLCDNumber, QDial, QProgressDialog,
    QColorDialog, QFontDialog, QInputDialog, QStyleFactory, QGridLayout
)
from PyQt6.QtCore import Qt, QTimer, QDate, QTime, QDateTime, QRectF, QPointF, QPropertyAnimation, QEasingCurve, QSettings, pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QImage, QPainter, QPen, QBrush, QColor, QFont, QKeySequence, QMovie, QAction

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(100, 100)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QPen(Qt.GlobalColor.blue, 2))
        painter.drawEllipse(10, 10, 80, 80)
        painter.drawText(20, 50, "Custom")

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutBounce)
    
    def animate(self):
        rect = self.geometry()
        self.animation.setStartValue(rect)
        rect.moveLeft(rect.left() + 50)
        self.animation.setEndValue(rect)
        self.animation.start()

class LanguageManager:
    def __init__(self):
        self.translations = {
            'en': {
                'app_title': 'MultiTool App',
                'file_menu': 'File',
                'new': 'New',
                'open': 'Open',
                'save': 'Save',
                'exit': 'Exit',
                'edit_menu': 'Edit',
                'cut': 'Cut',
                'copy': 'Copy',
                'paste': 'Paste',
                'view_menu': 'View',
                'zoom_in': 'Zoom In',
                'zoom_out': 'Zoom Out',
                'tools_menu': 'Tools',
                'calculator': 'Calculator',
                'timer': 'Timer',
                'notepad': 'Notepad',
                'settings_menu': 'Settings',
                'language': 'Language',
                'theme': 'Theme',
                'help_menu': 'Help',
                'about': 'About',
                'welcome': 'Welcome to MultiTool App',
                'select_language': 'Select Language',
                'english': 'English',
                'persian': 'Persian',
                'chinese': 'Chinese',
                'russian': 'Russian',
                'select_theme': 'Select Theme',
                'windows11': 'Windows 11',
                'light': 'Light',
                'dark': 'Dark',
                'default': 'Default',
                'red': 'Red',
                'blue': 'Blue',
                'text_editor': 'Text Editor',
                'image_viewer': 'Image Viewer',
                'file_browser': 'File Browser',
                'settings': 'Settings',
                'about_app': 'About App',
                'calculator_tab': 'Calculator',
                'timer_tab': 'Timer',
                'drawing_tool': 'Drawing Tool',
                'chat_bot': 'Chat Bot',
                'game': 'Game',
                'database': 'Database',
                'animation_demo': 'Animation Demo',
                'custom_widgets': 'Custom Widgets',
                'advanced_settings': 'Advanced Settings',
                'export': 'Export',
                'import': 'Import',
                'print': 'Print',
                'undo': 'Undo',
                'redo': 'Redo',
                'find': 'Find',
                'replace': 'Replace',
                'fullscreen': 'Fullscreen',
                'status_bar': 'Status Bar',
                'toolbar': 'Toolbar',
                'dock_widgets': 'Dock Widgets',
                'calendar': 'Calendar',
                'lcd_display': 'LCD Display',
                'dial_control': 'Dial Control',
                'progress': 'Progress',
                'color_picker': 'Color Picker',
                'font_picker': 'Font Picker',
                'input_dialog': 'Input Dialog',
                'message_box': 'Message Box',
                'error': 'Error',
                'info': 'Information',
                'warning': 'Warning',
                'question': 'Question',
                'splitter_demo': 'Splitter Demo',
                'scroll_area': 'Scroll Area',
                'group_box': 'Group Box',
                'radio_buttons': 'Radio Buttons',
                'check_boxes': 'Check Boxes',
                'sliders': 'Sliders',
                'spin_boxes': 'Spin Boxes',
                'date_edit': 'Date Edit',
                'time_edit': 'Time Edit',
                'datetime_edit': 'DateTime Edit',
                'combo_box': 'Combo Box',
                'list_widget': 'List Widget',
                'table_widget': 'Table Widget',
                'line_edit': 'Line Edit',
                'text_edit': 'Text Edit',
                'label': 'Label',
                'button': 'Button',
                'start': 'Start',
                'stop': 'Stop',
                'reset': 'Reset',
                'calculate': 'Calculate',
                'draw': 'Draw',
                'clear': 'Clear',
                'send': 'Send',
                'play': 'Play',
                'pause': 'Pause',
                'save_settings': 'Save Settings',
                'load_settings': 'Load Settings',
                'version': 'Version 1.0',
                'author': 'Developed by Hamid Yarali',
                'description': 'A multifunctional application with support for multiple languages and themes.'
            },
            'fa': {
                'app_title': 'برنامه چندابزاری',
                'file_menu': 'فایل',
                'new': 'جدید',
                'open': 'باز کردن',
                'save': 'ذخیره',
                'exit': 'خروج',
                'edit_menu': 'ویرایش',
                'cut': 'برش',
                'copy': 'کپی',
                'paste': 'چسباندن',
                'view_menu': 'نمایش',
                'zoom_in': 'بزرگنمایی',
                'zoom_out': 'کوچکنمایی',
                'tools_menu': 'ابزارها',
                'calculator': 'ماشین حساب',
                'timer': 'زمان سنج',
                'notepad': 'یادداشت',
                'settings_menu': 'تنظیمات',
                'language': 'زبان',
                'theme': 'تم',
                'help_menu': 'کمک',
                'about': 'درباره',
                'welcome': 'خوش آمدید به برنامه چندابزاری',
                'select_language': 'انتخاب زبان',
                'english': 'انگلیسی',
                'persian': 'فارسی',
                'chinese': 'چینی',
                'russian': 'روسی',
                'select_theme': 'انتخاب تم',
                'windows11': 'ویندوز 11',
                'light': 'روشن',
                'dark': 'تاریک',
                'default': 'پیش فرض',
                'red': 'قرمز',
                'blue': 'آبی',
                'text_editor': 'ویرایشگر متن',
                'image_viewer': 'نمایشگر تصویر',
                'file_browser': 'مرورگر فایل',
                'settings': 'تنظیمات',
                'about_app': 'درباره برنامه',
                'calculator_tab': 'ماشین حساب',
                'timer_tab': 'زمان سنج',
                'drawing_tool': 'ابزار نقاشی',
                'chat_bot': 'چت بات',
                'game': 'بازی',
                'database': 'پایگاه داده',
                'animation_demo': 'نمایش انیمیشن',
                'custom_widgets': 'ویجت های سفارشی',
                'advanced_settings': 'تنظیمات پیشرفته',
                'export': 'صادرات',
                'import': 'واردات',
                'print': 'چاپ',
                'undo': 'بازگشت',
                'redo': 'جلو',
                'find': 'جستجو',
                'replace': 'جایگزین',
                'fullscreen': 'تمام صفحه',
                'status_bar': 'نوار وضعیت',
                'toolbar': 'نوار ابزار',
                'dock_widgets': 'ویجت های داک',
                'calendar': 'تقویم',
                'lcd_display': 'نمایشگر LCD',
                'dial_control': 'کنترل دیال',
                'progress': 'پیشرفت',
                'color_picker': 'انتخاب رنگ',
                'font_picker': 'انتخاب فونت',
                'input_dialog': 'دیالوگ ورودی',
                'message_box': 'جعبه پیام',
                'error': 'خطا',
                'info': 'اطلاعات',
                'warning': 'هشدار',
                'question': 'سوال',
                'splitter_demo': 'نمایش اسپلیتر',
                'scroll_area': 'منطقه اسکرول',
                'group_box': 'جعبه گروه',
                'radio_buttons': 'دکمه های رادیویی',
                'check_boxes': 'چک باکس ها',
                'sliders': 'اسلایدرها',
                'spin_boxes': 'اسپین باکس ها',
                'date_edit': 'ویرایش تاریخ',
                'time_edit': 'ویرایش زمان',
                'datetime_edit': 'ویرایش تاریخ و زمان',
                'combo_box': 'کامبو باکس',
                'list_widget': 'لیست ویجت',
                'table_widget': 'جدول ویجت',
                'line_edit': 'ویرایش خط',
                'text_edit': 'ویرایش متن',
                'label': 'برچسب',
                'button': 'دکمه',
                'start': 'شروع',
                'stop': 'توقف',
                'reset': 'ریست',
                'calculate': 'محاسبه',
                'draw': 'کشیدن',
                'clear': 'پاک کردن',
                'send': 'ارسال',
                'play': 'پخش',
                'pause': 'مکث',
                'save_settings': 'ذخیره تنظیمات',
                'load_settings': 'بارگذاری تنظیمات',
                'version': 'نسخه 1.0',
                'author': 'توسعه یافته توسط حمید یارعلی',
                'description': 'یک برنامه چندمنظوره با پشتیبانی از چندین زبان و تم.'
            },
            'zh': {
                'app_title': '多工具应用',
                'file_menu': '文件',
                'new': '新建',
                'open': '打开',
                'save': '保存',
                'exit': '退出',
                'edit_menu': '编辑',
                'cut': '剪切',
                'copy': '复制',
                'paste': '粘贴',
                'view_menu': '视图',
                'zoom_in': '放大',
                'zoom_out': '缩小',
                'tools_menu': '工具',
                'calculator': '计算器',
                'timer': '计时器',
                'notepad': '记事本',
                'settings_menu': '设置',
                'language': '语言',
                'theme': '主题',
                'help_menu': '帮助',
                'about': '关于',
                'welcome': '欢迎使用多工具应用',
                'select_language': '选择语言',
                'english': '英语',
                'persian': '波斯语',
                'chinese': '中文',
                'russian': '俄语',
                'select_theme': '选择主题',
                'windows11': 'Windows 11',
                'light': '浅色',
                'dark': '深色',
                'default': '默认',
                'red': '红色',
                'blue': '蓝色',
                'text_editor': '文本编辑器',
                'image_viewer': '图像查看器',
                'file_browser': '文件浏览器',
                'settings': '设置',
                'about_app': '关于应用',
                'calculator_tab': '计算器',
                'timer_tab': '计时器',
                'drawing_tool': '绘图工具',
                'chat_bot': '聊天机器人',
                'game': '游戏',
                'database': '数据库',
                'animation_demo': '动画演示',
                'custom_widgets': '自定义小部件',
                'advanced_settings': '高级设置',
                'export': '导出',
                'import': '导入',
                'print': '打印',
                'undo': '撤销',
                'redo': '重做',
                'find': '查找',
                'replace': '替换',
                'fullscreen': '全屏',
                'status_bar': '状态栏',
                'toolbar': '工具栏',
                'dock_widgets': '停靠小部件',
                'calendar': '日历',
                'lcd_display': 'LCD 显示',
                'dial_control': '拨号控制',
                'progress': '进度',
                'color_picker': '颜色选择器',
                'font_picker': '字体选择器',
                'input_dialog': '输入对话框',
                'message_box': '消息框',
                'error': '错误',
                'info': '信息',
                'warning': '警告',
                'question': '问题',
                'splitter_demo': '拆分器演示',
                'scroll_area': '滚动区域',
                'group_box': '组框',
                'radio_buttons': '单选按钮',
                'check_boxes': '复选框',
                'sliders': '滑块',
                'spin_boxes': '旋转框',
                'date_edit': '日期编辑',
                'time_edit': '时间编辑',
                'datetime_edit': '日期时间编辑',
                'combo_box': '组合框',
                'list_widget': '列表小部件',
                'table_widget': '表格小部件',
                'line_edit': '行编辑',
                'text_edit': '文本编辑',
                'label': '标签',
                'button': '按钮',
                'start': '开始',
                'stop': '停止',
                'reset': '重置',
                'calculate': '计算',
                'draw': '绘制',
                'clear': '清除',
                'send': '发送',
                'play': '播放',
                'pause': '暂停',
                'save_settings': '保存设置',
                'load_settings': '加载设置',
                'version': '版本 1.0',
                'author': '由 Hamid Yarali 开发',
                'description': '一个支持多种语言和主题的多功能应用程序。'
            },
            'ru': {
                'app_title': 'Многофункциональное приложение',
                'file_menu': 'Файл',
                'new': 'Новый',
                'open': 'Открыть',
                'save': 'Сохранить',
                'exit': 'Выход',
                'edit_menu': 'Правка',
                'cut': 'Вырезать',
                'copy': 'Копировать',
                'paste': 'Вставить',
                'view_menu': 'Вид',
                'zoom_in': 'Увеличить',
                'zoom_out': 'Уменьшить',
                'tools_menu': 'Инструменты',
                'calculator': 'Калькулятор',
                'timer': 'Таймер',
                'notepad': 'Блокнот',
                'settings_menu': 'Настройки',
                'language': 'Язык',
                'theme': 'Тема',
                'help_menu': 'Справка',
                'about': 'О программе',
                'welcome': 'Добро пожаловать в многофункциональное приложение',
                'select_language': 'Выберите язык',
                'english': 'Английский',
                'persian': 'Персидский',
                'chinese': 'Китайский',
                'russian': 'Русский',
                'select_theme': 'Выберите тему',
                'windows11': 'Windows 11',
                'light': 'Светлая',
                'dark': 'Темная',
                'default': 'По умолчанию',
                'red': 'Красная',
                'blue': 'Синяя',
                'text_editor': 'Текстовый редактор',
                'image_viewer': 'Просмотрщик изображений',
                'file_browser': 'Обозреватель файлов',
                'settings': 'Настройки',
                'about_app': 'О приложении',
                'calculator_tab': 'Калькулятор',
                'timer_tab': 'Таймер',
                'drawing_tool': 'Инструмент рисования',
                'chat_bot': 'Чат-бот',
                'game': 'Игра',
                'database': 'База данных',
                'animation_demo': 'Демонстрация анимации',
                'custom_widgets': 'Пользовательские виджеты',
                'advanced_settings': 'Расширенные настройки',
                'export': 'Экспорт',
                'import': 'Импорт',
                'print': 'Печать',
                'undo': 'Отменить',
                'redo': 'Повторить',
                'find': 'Найти',
                'replace': 'Заменить',
                'fullscreen': 'Полноэкранный режим',
                'status_bar': 'Строка состояния',
                'toolbar': 'Панель инструментов',
                'dock_widgets': 'Док-виджеты',
                'calendar': 'Календарь',
                'lcd_display': 'LCD-дисплей',
                'dial_control': 'Контроль циферблата',
                'progress': 'Прогресс',
                'color_picker': 'Выбор цвета',
                'font_picker': 'Выбор шрифта',
                'input_dialog': 'Диалог ввода',
                'message_box': 'Сообщение',
                'error': 'Ошибка',
                'info': 'Информация',
                'warning': 'Предупреждение',
                'question': 'Вопрос',
                'splitter_demo': 'Демонстрация сплиттера',
                'scroll_area': 'Область прокрутки',
                'group_box': 'Групповой бокс',
                'radio_buttons': 'Радиокнопки',
                'check_boxes': 'Чекбоксы',
                'sliders': 'Слайдеры',
                'spin_boxes': 'Спинбоксы',
                'date_edit': 'Редактирование даты',
                'time_edit': 'Редактирование времени',
                'datetime_edit': 'Редактирование даты и времени',
                'combo_box': 'Комбо бокс',
                'list_widget': 'Список виджет',
                'table_widget': 'Таблица виджет',
                'line_edit': 'Строка редактирования',
                'text_edit': 'Текст редактирования',
                'label': 'Метка',
                'button': 'Кнопка',
                'start': 'Старт',
                'stop': 'Стоп',
                'reset': 'Сброс',
                'calculate': 'Рассчитать',
                'draw': 'Нарисовать',
                'clear': 'Очистить',
                'send': 'Отправить',
                'play': 'Играть',
                'pause': 'Пауза',
                'save_settings': 'Сохранить настройки',
                'load_settings': 'Загрузить настройки',
                'version': 'Версия 1.0',
                'author': 'Разработано Hamid Yarali',
                'description': 'Многофункциональное приложение с поддержкой нескольких языков и тем.'
            }
        }
        self.current_lang = 'en'

    def get_text(self, key):
        return self.translations.get(self.current_lang, self.translations['en']).get(key, key)

    def set_language(self, lang):
        self.current_lang = lang

class ThemeManager:
    def __init__(self):
        self.themes = {
            'windows11': 'windowsvista',
            'light': """
                QWidget { background-color: #f8f9fa; color: #212529; font-family: Segoe UI; }
                QPushButton { background-color: #e9ecef; border: 1px solid #ced4da; padding: 8px; border-radius: 6px; }
                QPushButton:hover { background-color: #dee2e6; }
                QTabWidget::pane { border: 1px solid #ced4da; }
                QMenuBar { background-color: #f8f9fa; }
            """,
            'dark': """
                QWidget { background-color: #212529; color: #f8f9fa; font-family: Segoe UI; }
                QPushButton { background-color: #343a40; border: 1px solid #495057; padding: 8px; border-radius: 6px; }
                QPushButton:hover { background-color: #495057; }
                QTabWidget::pane { border: 1px solid #495057; }
                QMenuBar { background-color: #212529; }
            """,
            'default': "",
            'red': """
                QWidget { background-color: #ffebee; color: #c62828; }
                QPushButton { background-color: #ef9a9a; border: 1px solid #e57373; padding: 8px; border-radius: 6px; }
                QPushButton:hover { background-color: #e57373; }
            """,
            'blue': """
                QWidget { background-color: #e3f2fd; color: #1565c0; }
                QPushButton { background-color: #90caf9; border: 1px solid #42a5f5; padding: 8px; border-radius: 6px; }
                QPushButton:hover { background-color: #42a5f5; }
            """
        }
        self.current_theme = 'default'

    def apply_theme(self, app, theme):
        self.current_theme = theme
        style = self.themes.get(theme, "")
        if style in QStyleFactory.keys():
            app.setStyle(style)
            app.setStyleSheet("")
        else:
            app.setStyle('Fusion')
            app.setStyleSheet(style)

class CalculatorWidget(QWidget):
    def __init__(self, lang_manager):
        super().__init__()
        self.lang_manager = lang_manager
        layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Segoe UI", 16))
        layout.addWidget(self.display)
        buttons_layout = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', 'x²', 'sin',
            'cos', 'tan', 'log', 'exp'
        ]
        positions = [(i//4, i%4) for i in range(len(buttons))]
        for pos, btn_text in zip(positions, buttons):
            button = QPushButton(btn_text)
            button.setFont(QFont("Segoe UI", 12))
            button.clicked.connect(self.on_button_clicked)
            buttons_layout.addWidget(button, *pos)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text == '=':
            try:
                result = eval(self.display.text().replace('√', 'math.sqrt').replace('x²', '**2'))
                self.display.setText(str(result))
            except:
                self.display.setText(self.lang_manager.get_text('error'))
        elif text == 'C':
            self.display.clear()
        elif text in ['√', 'x²', 'sin', 'cos', 'tan', 'log', 'exp']:
            try:
                value = float(self.display.text())
                if text == '√':
                    result = math.sqrt(value)
                elif text == 'x²':
                    result = value ** 2
                elif text == 'sin':
                    result = math.sin(math.radians(value))
                elif text == 'cos':
                    result = math.cos(math.radians(value))
                elif text == 'tan':
                    result = math.tan(math.radians(value))
                elif text == 'log':
                    result = math.log10(value)
                elif text == 'exp':
                    result = math.exp(value)
                self.display.setText(str(result))
            except:
                self.display.setText(self.lang_manager.get_text('error'))
        else:
            self.display.setText(self.display.text() + text)

class TimerWidget(QWidget):
    def __init__(self, lang_manager):
        super().__init__()
        self.lang_manager = lang_manager
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.time = 0
        layout = QVBoxLayout()
        self.display = QLabel('00:00:00')
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setFont(QFont("Segoe UI", 24))
        layout.addWidget(self.display)
        buttons_layout = QHBoxLayout()
        start_btn = QPushButton(self.lang_manager.get_text('start'))
        stop_btn = QPushButton(self.lang_manager.get_text('stop'))
        reset_btn = QPushButton(self.lang_manager.get_text('reset'))
        start_btn.clicked.connect(self.start_timer)
        stop_btn.clicked.connect(self.stop_timer)
        reset_btn.clicked.connect(self.reset_timer)
        buttons_layout.addWidget(start_btn)
        buttons_layout.addWidget(stop_btn)
        buttons_layout.addWidget(reset_btn)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.time = 0
        self.display.setText('00:00:00')

    def update_time(self):
        self.time += 1
        hours = self.time // 3600
        minutes = (self.time % 3600) // 60
        seconds = self.time % 60
        self.display.setText(f'{hours:02}:{minutes:02}:{seconds:02}')

class DrawingWidget(QGraphicsView):
    def __init__(self, lang_manager):
        super().__init__()
        self.lang_manager = lang_manager
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.pen = QPen(QColor("blue"), 4, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        self.last_point = None
        self.setRenderHint(QPainter.RenderHint.Antialiasing)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.last_point = self.mapToScene(event.pos())

    def mouseMoveEvent(self, event):
        if self.last_point is not None:
            point = self.mapToScene(event.pos())
            self.scene.addLine(self.last_point.x(), self.last_point.y(), point.x(), point.y(), self.pen)
            self.last_point = point

    def mouseReleaseEvent(self, event):
        self.last_point = None

    def clear(self):
        self.scene.clear()

class ChatBotWidget(QWidget):
    def __init__(self, lang_manager):
        super().__init__()
        self.lang_manager = lang_manager
        layout = QVBoxLayout()
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)
        input_layout = QHBoxLayout()
        self.input_edit = QLineEdit()
        send_btn = QPushButton(self.lang_manager.get_text('send'))
        send_btn.clicked.connect(self.send_message)
        input_layout.addWidget(self.input_edit)
        input_layout.addWidget(send_btn)
        layout.addLayout(input_layout)
        self.setLayout(layout)

    def send_message(self):
        message = self.input_edit.text()
        if message:
            self.chat_display.append(f"<b>You:</b> {message}")
            response = self.get_response(message)
            self.chat_display.append(f"<b>Bot:</b> {response}")
            self.input_edit.clear()

    def get_response(self, message):
        responses = {
            'hello': 'Hi there!',
            'سلام': 'سلام! چطور می‌توانم کمک کنم؟',
            '你好': '你好！有什么可以帮助你的？',
            'привет': 'Привет! Чем могу помочь?'
        }
        return responses.get(message.lower(), "I don't understand that yet.")

class GameWidget(QWidget):
    def __init__(self, lang_manager):
        super().__init__()
        self.lang_manager = lang_manager
        layout = QVBoxLayout()
        self.score_label = QLabel('Score: 0')
        self.score_label.setFont(QFont("Segoe UI", 18))
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.score_label)
        self.game_button = QPushButton(self.lang_manager.get_text('play'))
        self.game_button.clicked.connect(self.play_game)
        layout.addWidget(self.game_button)
        self.setLayout(layout)
        self.score = 0

    def play_game(self):
        self.score += random.randint(5, 25)
        self.score_label.setText(f'Score: {self.score}')

class SettingsDialog(QDialog):
    language_changed = pyqtSignal(str)
    theme_changed = pyqtSignal(str)

    def __init__(self, lang_manager, theme_manager, parent=None):
        super().__init__(parent)
        self.lang_manager = lang_manager
        self.theme_manager = theme_manager
        self.setWindowTitle(self.lang_manager.get_text('settings'))
        layout = QFormLayout()
        self.lang_combo = QComboBox()
        self.lang_combo.addItems([
            self.lang_manager.get_text('english'),
            self.lang_manager.get_text('persian'),
            self.lang_manager.get_text('chinese'),
            self.lang_manager.get_text('russian')
        ])
        layout.addRow(self.lang_manager.get_text('select_language'), self.lang_combo)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems([
            self.lang_manager.get_text('windows11'),
            self.lang_manager.get_text('light'),
            self.lang_manager.get_text('dark'),
            self.lang_manager.get_text('default'),
            self.lang_manager.get_text('red'),
            self.lang_manager.get_text('blue')
        ])
        layout.addRow(self.lang_manager.get_text('select_theme'), self.theme_combo)
        buttons_layout = QHBoxLayout()
        save_btn = QPushButton(self.lang_manager.get_text('save_settings'))
        save_btn.clicked.connect(self.save_settings)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        buttons_layout.addWidget(save_btn)
        buttons_layout.addWidget(close_btn)
        layout.addRow(buttons_layout)
        self.setLayout(layout)

    def save_settings(self):
        settings = QSettings("HY", "MultiToolApp")
        lang_index = self.lang_combo.currentIndex()
        lang_map = {0: 'en', 1: 'fa', 2: 'zh', 3: 'ru'}
        settings.setValue("language", lang_map.get(lang_index, 'en'))
        theme_index = self.theme_combo.currentIndex()
        theme_map = {0: 'windows11', 1: 'light', 2: 'dark', 3: 'default', 4: 'red', 5: 'blue'}
        settings.setValue("theme", theme_map.get(theme_index, 'default'))
        self.language_changed.emit(lang_map.get(lang_index, 'en'))
        self.theme_changed.emit(theme_map.get(theme_index, 'default'))
        self.close()

class AboutDialog(QDialog):
    def __init__(self, lang_manager, parent=None):
        super().__init__(parent)
        self.lang_manager = lang_manager
        self.setWindowTitle(self.lang_manager.get_text('about_app'))
        layout = QVBoxLayout()
        title = QLabel("<h2>" + self.lang_manager.get_text('app_title') + "</h2>")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        version = QLabel(self.lang_manager.get_text('version'))
        layout.addWidget(version)
        author = QLabel(self.lang_manager.get_text('author'))
        layout.addWidget(author)
        description = QLabel(self.lang_manager.get_text('description'))
        description.setWordWrap(True)
        layout.addWidget(description)
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lang_manager = LanguageManager()
        self.theme_manager = ThemeManager()
        self.setWindowTitle(self.lang_manager.get_text('app_title'))
        self.setGeometry(100, 100, 1400, 900)
        self.setWindowIcon(QIcon())
        
        # Menu Bar
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        self.create_menus()
        
        # Tool Bar
        self.tool_bar = QToolBar()
        self.addToolBar(self.tool_bar)
        self.create_toolbar()
        
        # Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage(self.lang_manager.get_text('welcome'))
        
        # Dock Widgets
        self.left_dock = QDockWidget("Explorer", self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.left_dock)
        self.right_dock = QDockWidget("Properties", self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.right_dock)
        
        # Central Widget
        self.central_widget = QTabWidget()
        self.setCentralWidget(self.central_widget)
        self.create_tabs()
        
        # Apply initial theme
        self.theme_manager.apply_theme(QApplication.instance(), 'default')
        
        # Load saved settings
        self.load_initial_settings()

    def create_menus(self):
        file_menu = QMenu(self.lang_manager.get_text('file_menu'), self)
        new_action = QAction(self.lang_manager.get_text('new'), self)
        new_action.triggered.connect(self.new_file)
        open_action = QAction(self.lang_manager.get_text('open'), self)
        open_action.triggered.connect(self.open_file)
        save_action = QAction(self.lang_manager.get_text('save'), self)
        save_action.triggered.connect(self.save_file)
        exit_action = QAction(self.lang_manager.get_text('exit'), self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        self.menu_bar.addMenu(file_menu)
        
        edit_menu = QMenu(self.lang_manager.get_text('edit_menu'), self)
        cut_action = QAction(self.lang_manager.get_text('cut'), self)
        copy_action = QAction(self.lang_manager.get_text('copy'), self)
        paste_action = QAction(self.lang_manager.get_text('paste'), self)
        undo_action = QAction(self.lang_manager.get_text('undo'), self)
        redo_action = QAction(self.lang_manager.get_text('redo'), self)
        find_action = QAction(self.lang_manager.get_text('find'), self)
        replace_action = QAction(self.lang_manager.get_text('replace'), self)
        edit_menu.addAction(cut_action)
        edit_menu.addAction(copy_action)
        edit_menu.addAction(paste_action)
        edit_menu.addSeparator()
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        edit_menu.addSeparator()
        edit_menu.addAction(find_action)
        edit_menu.addAction(replace_action)
        self.menu_bar.addMenu(edit_menu)
        
        view_menu = QMenu(self.lang_manager.get_text('view_menu'), self)
        fullscreen_action = QAction(self.lang_manager.get_text('fullscreen'), self)
        fullscreen_action.triggered.connect(self.toggle_fullscreen)
        view_menu.addAction(fullscreen_action)
        self.menu_bar.addMenu(view_menu)
        
        settings_menu = QMenu(self.lang_manager.get_text('settings_menu'), self)
        settings_action = QAction(self.lang_manager.get_text('settings'), self)
        settings_action.triggered.connect(self.show_settings)
        settings_menu.addAction(settings_action)
        self.menu_bar.addMenu(settings_menu)
        
        help_menu = QMenu(self.lang_manager.get_text('help_menu'), self)
        about_action = QAction(self.lang_manager.get_text('about'), self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        self.menu_bar.addMenu(help_menu)

    def create_toolbar(self):
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        self.tool_bar.addAction(new_action)
        self.tool_bar.addAction(open_action)
        self.tool_bar.addAction(save_action)

    def create_tabs(self):
        self.text_editor_tab = QTextEdit()
        self.central_widget.addTab(self.text_editor_tab, self.lang_manager.get_text('text_editor'))
        
        self.image_viewer_tab = QLabel("Image Viewer - Open an image to view")
        self.image_viewer_tab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.central_widget.addTab(self.image_viewer_tab, self.lang_manager.get_text('image_viewer'))
        
        self.file_browser_tab = QListWidget()
        self.central_widget.addTab(self.file_browser_tab, self.lang_manager.get_text('file_browser'))
        
        self.calculator_tab = CalculatorWidget(self.lang_manager)
        self.central_widget.addTab(self.calculator_tab, self.lang_manager.get_text('calculator_tab'))
        
        self.timer_tab = TimerWidget(self.lang_manager)
        self.central_widget.addTab(self.timer_tab, self.lang_manager.get_text('timer_tab'))
        
        drawing_layout = QVBoxLayout()
        self.drawing_widget = DrawingWidget(self.lang_manager)
        clear_btn = QPushButton(self.lang_manager.get_text('clear'))
        clear_btn.clicked.connect(self.drawing_widget.clear)
        drawing_layout.addWidget(self.drawing_widget)
        drawing_layout.addWidget(clear_btn)
        drawing_tab = QWidget()
        drawing_tab.setLayout(drawing_layout)
        self.central_widget.addTab(drawing_tab, self.lang_manager.get_text('drawing_tool'))
        
        self.chat_bot_tab = ChatBotWidget(self.lang_manager)
        self.central_widget.addTab(self.chat_bot_tab, self.lang_manager.get_text('chat_bot'))
        
        self.game_tab = GameWidget(self.lang_manager)
        self.central_widget.addTab(self.game_tab, self.lang_manager.get_text('game'))
        
        self.animation_tab = QWidget()
        animation_layout = QVBoxLayout()
        self.animated_button = AnimatedButton(self.lang_manager.get_text('animation_demo'))
        self.animated_button.clicked.connect(self.animated_button.animate)
        animation_layout.addWidget(self.animated_button)
        self.animation_tab.setLayout(animation_layout)
        self.central_widget.addTab(self.animation_tab, self.lang_manager.get_text('animation_demo'))
        
        self.custom_widget_tab = CustomWidget()
        self.central_widget.addTab(self.custom_widget_tab, self.lang_manager.get_text('custom_widgets'))
        
        self.calendar_tab = QCalendarWidget()
        self.central_widget.addTab(self.calendar_tab, self.lang_manager.get_text('calendar'))
        
        self.lcd_tab = QLCDNumber()
        self.lcd_tab.display(2026)
        self.central_widget.addTab(self.lcd_tab, self.lang_manager.get_text('lcd_display'))
        
        self.dial_tab = QDial()
        self.central_widget.addTab(self.dial_tab, self.lang_manager.get_text('dial_control'))
        
        self.progress_tab = QProgressBar()
        self.progress_tab.setValue(75)
        self.central_widget.addTab(self.progress_tab, self.lang_manager.get_text('progress'))
        
        self.splitter_tab = QSplitter()
        self.splitter_tab.addWidget(QLabel("Left Panel"))
        self.splitter_tab.addWidget(QLabel("Right Panel"))
        self.central_widget.addTab(self.splitter_tab, self.lang_manager.get_text('splitter_demo'))
        
        scroll_tab = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        for i in range(30):
            scroll_layout.addWidget(QLabel(f"Scrollable Item {i+1} - Long Content Example"))
        scroll_widget.setLayout(scroll_layout)
        scroll_tab.setWidget(scroll_widget)
        self.central_widget.addTab(scroll_tab, self.lang_manager.get_text('scroll_area'))
        
        group_tab = QGroupBox(self.lang_manager.get_text('group_box'))
        group_layout = QVBoxLayout()
        group_layout.addWidget(QRadioButton(self.lang_manager.get_text('radio_buttons')))
        group_layout.addWidget(QCheckBox(self.lang_manager.get_text('check_boxes')))
        group_layout.addWidget(QSlider(Qt.Orientation.Horizontal))
        group_layout.addWidget(QSpinBox())
        group_layout.addWidget(QDateEdit())
        group_layout.addWidget(QTimeEdit())
        group_layout.addWidget(QDateTimeEdit())
        combo = QComboBox()
        combo.addItems(["Option 1", "Option 2", "Option 3"])
        group_layout.addWidget(combo)
        list_widget = QListWidget()
        list_widget.addItems(["Item A", "Item B", "Item C"])
        group_layout.addWidget(list_widget)
        table = QTableWidget(4, 4)
        for i in range(4):
            for j in range(4):
                table.setItem(i, j, QTableWidgetItem(f"Cell {i},{j}"))
        group_layout.addWidget(table)
        group_layout.addWidget(QLineEdit())
        group_layout.addWidget(QTextEdit())
        group_tab.setLayout(group_layout)
        self.central_widget.addTab(group_tab, self.lang_manager.get_text('group_box'))

    def new_file(self):
        self.text_editor_tab.clear()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    self.text_editor_tab.setText(f.read())
            except:
                QMessageBox.warning(self, "Error", "Could not open file.")

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File")
        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write(self.text_editor_tab.toPlainText())
            except:
                QMessageBox.warning(self, "Error", "Could not save file.")

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def show_settings(self):
        dialog = SettingsDialog(self.lang_manager, self.theme_manager, self)
        dialog.language_changed.connect(self.change_language)
        dialog.theme_changed.connect(self.change_theme)
        dialog.exec()

    def show_about(self):
        dialog = AboutDialog(self.lang_manager, self)
        dialog.exec()

    def change_language(self, lang):
        self.lang_manager.set_language(lang)
        direction = Qt.LayoutDirection.RightToLeft if lang in ['fa'] else Qt.LayoutDirection.LeftToRight
        QApplication.instance().setLayoutDirection(direction)
        self.retranslate_ui()

    def change_theme(self, theme):
        self.theme_manager.apply_theme(QApplication.instance(), theme)

    def retranslate_ui(self):
        self.setWindowTitle(self.lang_manager.get_text('app_title'))
        self.menu_bar.clear()
        self.create_menus()
        self.tool_bar.clear()
        self.create_toolbar()
        for i in range(self.central_widget.count()):
            key = ['text_editor', 'image_viewer', 'file_browser', 'calculator_tab', 'timer_tab',
                   'drawing_tool', 'chat_bot', 'game', 'animation_demo', 'custom_widgets',
                   'calendar', 'lcd_display', 'dial_control', 'progress', 'splitter_demo',
                   'scroll_area', 'group_box'][i]
            self.central_widget.setTabText(i, self.lang_manager.get_text(key))
        self.status_bar.showMessage(self.lang_manager.get_text('welcome'))

    def load_initial_settings(self):
        settings = QSettings("HY", "MultiToolApp")
        lang = settings.value("language", 'en')
        theme = settings.value("theme", 'default')
        self.change_language(lang)
        self.change_theme(theme)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())