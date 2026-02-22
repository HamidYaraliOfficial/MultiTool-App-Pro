# MultiTool App Pro

## English

### Overview
**MultiTool App Pro** is a comprehensive, all-in-one desktop utility application built with Python and PyQt6. It combines over 20 essential tools and widgets into a single, elegant interface — perfect for developers, students, designers, and power users who need quick access to calculators, timers, text editors, drawing tools, games, and advanced UI demonstrations.

### Key Features
- **20+ Integrated Tools**: Calculator, Timer, Text Editor, Image Viewer, File Browser, Drawing Canvas, Chat Bot, Simple Game, Animation Demo, Custom Widgets, Calendar, LCD Display, Dial Control, Progress Bar, Splitter, Scroll Area, Group Box with all standard widgets.
- **Full Multi-Language Support**: English, فارسی (Persian with RTL layout), 中文 (Chinese), Русский (Russian) — complete translation with dynamic direction.
- **Dynamic Themes**: Windows 11 style, Light, Dark, Default, Red, and Blue — with custom stylesheets and palette adaptation.
- **Modern UI Elements**: Tabbed interface, dock widgets, menu bar, toolbar, status bar, fullscreen mode.
- **Custom Widgets & Animations**: Animated buttons, custom painted widgets, and graphics scene drawing.
- **Settings Persistence**: Language and theme saved via QSettings.
- **Responsive Design**: Splitters, scroll areas, and resizable layouts for optimal usability.
- **Extensible Structure**: Clean, modular code ready for adding new tools.

### Requirements
- Python 3.8+
- PyQt6

### Installation
1. Ensure Python is installed.
2. Install the required package:
   ```bash
   pip install PyQt6
   ```
3. Run the application:
   ```bash
   python MultiToolApp.py
   ```

### Usage
- **Navigation**: Use tabs to switch between tools.
- **Settings**: Access via **Settings** menu to change language or theme instantly.
- **Tools**:
  - **Calculator**: Full scientific functions (sin, cos, tan, log, exp, √, x²).
  - **Timer**: Stopwatch with start/pause/stop/reset.
  - **Drawing Tool**: Freehand drawing with smooth anti-aliased lines.
  - **Chat Bot**: Simple conversational demo.
  - **Game**: Score-based random point game.
  - **Custom Widgets**: Demonstrates `paintEvent` and `QPropertyAnimation`.
- **File Operations**: New, Open, Save text files in the editor.

### Screenshots
- Tabbed workspace with 20+ tools  
- Scientific calculator with function buttons  
- Freehand drawing canvas  
- Persian RTL interface with full translation  
- Dark and Red/Blue custom themes  
- Animated button with bounce effect  

### Technical Highlights
- **Modular Architecture**: Separate classes for each major widget.
- **Signal-Driven**: Language and theme changes propagate via signals.
- **Custom Painting**: `QGraphicsView` with real-time line drawing.
- **Cross-Platform Styling**: Fusion base with custom CSS-like stylesheets.
- **RTL Support**: Automatic layout direction for Persian.

### Contributing
Fork and expand! Add new tools (converter, notes, media player), improve translations, or enhance animations. Pull requests are encouraged.

### License
MIT License – Free for personal and commercial use.

---

## فارسی

### بررسی اجمالی
**MultiTool App Pro** یک برنامه دسکتاپ جامع و همه‌کاره است که با پایتون و PyQt6 ساخته شده و بیش از ۲۰ ابزار ضروری را در یک رابط کاربری زیبا و یکپارچه گرد هم آورده است — مناسب برای توسعه‌دهندگان، دانشجویان، طراحان و کاربران حرفه‌ای که به دسترسی سریع به ماشین حساب، زمان‌سنج، ویرایشگر متن، ابزار نقاشی، بازی و نمایش ویجت‌های پیشرفته نیاز دارند.

### ویژگی‌های کلیدی
- **بیش از ۲۰ ابزار یکپارچه**: ماشین حساب، زمان‌سنج، ویرایشگر متن، نمایشگر تصویر، مرورگر فایل، بوم نقاشی، چت‌بات، بازی ساده، نمایش انیمیشن، ویجت‌های سفارشی، تقویم، نمایشگر LCD، کنترل دیال، نوار پیشرفت، اسپلیتر، منطقه اسکرول، جعبه گروه با تمام ویجت‌های استاندارد.
- **پشتیبانی کامل چندزبانه**: انگلیسی، فارسی (با چیدمان راست‌چین)، چینی، روسی — ترجمه کامل با جهت پویا.
- **تم‌های پویا**: سبک ویندوز ۱۱، روشن، تاریک، پیش‌فرض، قرمز و آبی — با stylesheetهای سفارشی و تطبیق پالت.
- **عناصر رابط کاربری مدرن**: رابط تب‌دار، ویجت‌های داک، نوار منو، نوار ابزار، نوار وضعیت، حالت تمام‌صفحه.
- **ویجت‌ها و انیمیشن‌های سفارشی**: دکمه‌های انیمیشنی، ویجت‌های نقاشی‌شده سفارشی و صحنه گرافیکی.
- **ذخیره تنظیمات**: زبان و تم با QSettings ذخیره می‌شوند.
- **طراحی پاسخگو**: اسپلیترها، مناطق اسکرول و چیدمان‌های قابل تغییر اندازه.
- **ساختار قابل گسترش**: کد تمیز و ماژولار آماده افزودن ابزارهای جدید.

### پیش‌نیازها
- پایتون ۳.۸ یا بالاتر
- PyQt6

### نصب
۱. پایتون را نصب کنید.
۲. بسته موردنیاز را نصب کنید:
   ```bash
   pip install PyQt6
   ```
۳. برنامه را اجرا کنید:
   ```bash
   python MultiToolApp.py
   ```

### نحوه استفاده
- **ناوبری**: از تب‌ها برای جابجایی بین ابزارها استفاده کنید.
- **تنظیمات**: از منوی **تنظیمات** برای تغییر فوری زبان یا تم دسترسی داشته باشید.
- **ابزارها**:
  - **ماشین حساب**: توابع علمی کامل (sin, cos, tan, log, exp, √, x²).
  - **زمان‌سنج**: کرنومتر با شروع/توقف موقت/توقف/ریست.
  - **ابزار نقاشی**: نقاشی آزاد با خطوط نرم و ضددندانه.
  - **چت‌بات**: دموی گفت‌وگوی ساده.
  - **بازی**: بازی امتیازدهی تصادفی.
  - **ویجت‌های سفارشی**: نمایش `paintEvent` و `QPropertyAnimation`.
- **عملیات فایل**: جدید، باز کردن، ذخیره فایل‌های متنی در ویرایشگر.

### تصاویر
- فضای کاری تب‌دار با بیش از ۲۰ ابزار  
- ماشین حساب علمی با دکمه‌های توابع  
- بوم نقاشی آزاد  
- رابط فارسی راست‌چین با ترجمه کامل  
- تم‌های تاریک و قرمز/آبی سفارشی  
- دکمه انیمیشنی با افکت پرش  

### نکات فنی
- **معماری ماژولار**: کلاس‌های جداگانه برای هر ویجت اصلی.
- **سیگنال‌محور**: تغییرات زبان و تم از طریق سیگنال‌ها منتشر می‌شوند.
- **نقاشی سفارشی**: `QGraphicsView` با رسم خط لحظه‌ای.
- **استایل‌بندی چندپلتفرمی**: پایه Fusion با stylesheetهای CSSمانند.
- **پشتیبانی راست‌چین**: جهت چیدمان خودکار برای فارسی.

### مشارکت
فورک کنید و گسترش دهید! ابزارهای جدید (مبدل، یادداشت، پخش رسانه)، بهبود ترجمه‌ها یا تقویت انیمیشن‌ها اضافه کنید. Pull request تشویق می‌شود.

### مجوز
مجوز MIT – آزاد برای استفاده شخصی و تجاری.

---

## 中文

### 概述
**MultiTool App Pro** 是一款功能全面的一体化桌面实用程序，使用 Python 和 PyQt6 构建，将 20 多个实用工具整合到一个优雅的界面中 — 适合开发者、学生、设计师和高级用户快速访问计算器、计时器、文本编辑器、绘图工具、游戏和高级 UI 演示。

### 主要功能
- **20+ 集成工具**：计算器、计时器、文本编辑器、图像查看器、文件浏览器、绘图画布、聊天机器人、简单游戏、动画演示、自定义小部件、日历、LCD 显示、拨号控制、进度条、拆分器、滚动区域、包含所有标准小部件的组框。
- **完整多语言支持**：英语、波斯语（RTL 布局）、中文、俄语 — 完全翻译，动态方向。
- **动态主题**：Windows 11 风格、明亮、暗黑、默认、红色和蓝色 — 自定义样式表和调色板适配。
- **现代 UI 元素**：标签式界面、停靠小部件、菜单栏、工具栏、状态栏、全屏模式。
- **自定义小部件与动画**：动画按钮、自定义绘制小部件和图形场景绘图。
- **设置持久化**：语言和主题通过 QSettings 保存。
- **响应式设计**：拆分器、滚动区域和可调整大小的布局。
- **可扩展结构**：干净模块化代码，易于添加新工具。

### 要求
- Python 3.8+
- PyQt6

### 安装
1. 确保已安装 Python。
2. 安装所需包：
   ```bash
   pip install PyQt6
   ```
3. 运行应用程序：
   ```bash
   python MultiToolApp.py
   ```

### 使用方法
- **导航**：使用标签页切换工具。
- **设置**：通过 **设置** 菜单即时更改语言或主题。
- **工具**：
  - **计算器**：完整科学函数（sin、cos、tan、log、exp、√、x²）。
  - **计时器**：秒表，支持开始/暂停/停止/重置。
  - **绘图工具**：自由绘图，平滑抗锯齿线条。
  - **聊天机器人**：简单对话演示。
  - **游戏**：随机得分游戏。
  - **自定义小部件**：展示 `paintEvent` 和 `QPropertyAnimation`。
- **文件操作**：在编辑器中新建、打开、保存文本文件。

### 截图
- 包含 20+ 工具的标签式工作区  
- 带函数按钮的科学计算器  
- 自由绘图画布  
- 波斯语 RTL 界面，完整翻译  
- 暗黑和红色/蓝色自定义主题  
- 带弹跳效果的动画按钮  

### 技术亮点
- **模块化架构**：每个主要小部件独立类。
- **信号驱动**：语言和主题变更通过信号传播。
- **自定义绘制**：`QGraphicsView` 实时线条绘制。
- **跨平台样式**：Fusion 基础加 CSS 样式表。
- **RTL 支持**：为波斯语自动布局方向。

### 贡献
欢迎 fork 并扩展！添加新工具（转换器、笔记、媒体播放器），改进翻译或增强动画。欢迎 Pull Request。

### 许可证
MIT 许可证 – 免费用于个人和商业用途。