import tkinter as tk
from tkinter import ttk, messagebox, font
import psycopg2
from psycopg2 import sql, Error
import configparser
import os

class DatabaseConnection:
    """
    Database connection manager for PostgreSQL streaming service database
    """
    
    def __init__(self):
        self.connection = None
        self.cursor = None
        
        # Default connection parameters - modify these for your database
        self.db_config = {
            'host': 'localhost',
            'database': 'combined_database',
            'user': 'Shachar777',
            'password': 'BugsBunny',
            'port': 5432
        }
    
    def get_connection(self):
        """
        Establish and return a PostgreSQL database connection
        Returns: psycopg2 connection object or None if failed
        """
        try:
            print("🔄 Attempting to connect to PostgreSQL database...")
            
            # Establish connection
            self.connection = psycopg2.connect(
                host=self.db_config['host'],
                database=self.db_config['database'],
                user=self.db_config['user'],
                password=self.db_config['password'],
                port=self.db_config['port']
            )
            
            # Create cursor
            self.cursor = self.connection.cursor()
            
            # Test the connection with a simple query
            self.cursor.execute("SELECT version();")
            db_version = self.cursor.fetchone()
            
            print("✅ SUCCESS: Connected to PostgreSQL database!")
            return self.connection
            
        except Error as e:
            print(f"❌ ERROR: Failed to connect to PostgreSQL database\n{str(e)}")
            return None
        
        except Exception as e:
            print(f"❌ UNEXPECTED ERROR: {str(e)}")
            return None
    
    def close_connection(self):
        """
        Safely close the database connection
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Error as e:
            print(f"❌ Error closing connection: {e}")


class MainMenuWindow:
    """
    Main menu window that opens after successful login
    """
    
    def __init__(self, db_connection):
        self.db = db_connection
        self.window = tk.Tk()
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Configure the main menu window"""
        self.window.title("Streaming Service Management System")
        self.window.geometry("800x600")
        self.window.configure(bg='#2c3e50')
        
        # Center the window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.window.winfo_screenheight() // 2) - (600 // 2)
        self.window.geometry(f"800x600+{x}+{y}")
        
        # Make window non-resizable for now
        self.window.resizable(False, False)
    
    def create_widgets(self):
        """Create the main menu interface"""
        # Title
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(
            self.window,
            text="🎬 Streaming Service Manager",
            font=title_font,
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=30)
        
        # Subtitle
        subtitle_font = font.Font(family="Arial", size=12)
        subtitle_label = tk.Label(
            self.window,
            text="Database Management Dashboard",
            font=subtitle_font,
            bg='#2c3e50',
            fg='#bdc3c7'
        )
        subtitle_label.pack(pady=(0, 40))
        
        # Menu buttons frame
        button_frame = tk.Frame(self.window, bg='#2c3e50')
        button_frame.pack(expand=True)
        
        # Button style
        button_font = font.Font(family="Arial", size=12, weight="bold")
        button_width = 25
        button_height = 2
        
        # Menu buttons
        buttons = [
            ("👥 Manage Customers", self.open_customers_crud),
            ("👤 Manage Profiles", self.open_profiles_crud),
            ("📺 Manage Watch History", self.open_watch_history_crud),
            ("📊 Reports", self.open_reports_screen),
            ("🚪 Exit", self.exit_application)
        ]
        
        for i, (text, command) in enumerate(buttons):
            btn = tk.Button(
                button_frame,
                text=text,
                command=command,
                font=button_font,
                width=button_width,
                height=button_height,
                bg='#3498db',
                fg='white',
                relief='flat',
                cursor='hand2'
            )
            btn.pack(pady=8)
            
            # Hover effects
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg='#2980b9'))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg='#3498db'))
        
        # Status bar
        status_frame = tk.Frame(self.window, bg='#34495e', height=30)
        status_frame.pack(side='bottom', fill='x')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text=f"✅ Connected to database: {self.db.db_config['database']}",
            bg='#34495e',
            fg='#2ecc71',
            font=('Arial', 9)
        )
        self.status_label.pack(side='left', padx=10, pady=5)
        
        # Exit button (removed from status bar, now in main menu)
        
        # Logout option in status bar
        logout_btn = tk.Button(
            status_frame,
            text="Logout",
            command=self.logout,
            bg='#f39c12',
            fg='white',
            font=('Arial', 9),
            relief='flat',
            cursor='hand2'
        )
        logout_btn.pack(side='right', padx=10, pady=3)
    
    def open_customers_crud(self):
        """Open the Customers CRUD screen"""
        print("🔄 Opening Customers CRUD screen...")
        customers_window = CustomersCRUDWindow(self.db, self.window)
        customers_window.run()
    
    def open_profiles_crud(self):
        """Open the Profiles CRUD screen"""
        print("🔄 Opening Profiles CRUD screen...")
        profiles_window = ProfilesCRUDWindow(self.db, self.window)
        profiles_window.run()
    
    def open_watch_history_crud(self):
        """Open the Watch History CRUD screen"""
        print("🔄 Opening Watch History CRUD screen...")
        watch_history_window = WatchHistoryCRUDWindow(self.db, self.window)
        watch_history_window.run()
    
    def open_reports_screen(self):
        """Open the Reports screen for queries and procedures"""
        print("🔄 Opening Reports screen...")
        reports_window = ReportsWindow(self.db, self.window)
        reports_window.run()
    
    def logout(self):
        """Return to login screen"""
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.window.destroy()
            # Restart the login window
            login_app = LoginWindow()
            login_app.run()
    
    def exit_application(self):
        """Close the application and database connection"""
        if messagebox.askokcancel("Exit Application", "Are you sure you want to exit the application?"):
            print("👋 Closing application...")
            self.db.close_connection()
            self.window.quit()  # This will exit the entire application
    
    def run(self):
        """Start the main menu window"""
        self.window.mainloop()


class LoginWindow:
    """
    Login window for the streaming service management application
    """
    
    def __init__(self):
        self.window = tk.Tk()
        self.db = None
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Configure the login window"""
        self.window.title("Streaming Service Login")
        self.window.geometry("450x550")
        self.window.configure(bg='#34495e')
        
        # Center the window on screen
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.window.winfo_screenheight() // 2) - (550 // 2)
        self.window.geometry(f"450x550+{x}+{y}")
        
        # Make window non-resizable
        self.window.resizable(False, False)
        
        # Set window icon (optional)
        try:
            self.window.iconname("StreamingApp")
        except:
            pass
    
    def create_widgets(self):
        """Create the login interface"""
        # Main container
        main_frame = tk.Frame(self.window, bg='#34495e')
        main_frame.pack(expand=True, fill='both', padx=40, pady=40)
        
        # Logo/Title section
        title_frame = tk.Frame(main_frame, bg='#34495e')
        title_frame.pack(pady=(0, 40))
        
        # App icon/emoji
        icon_label = tk.Label(
            title_frame,
            text="🎬",
            font=('Arial', 48),
            bg='#34495e',
            fg='#ecf0f1'
        )
        icon_label.pack()
        
        # App title
        title_font = font.Font(family="Arial", size=20, weight="bold")
        title_label = tk.Label(
            title_frame,
            text="Streaming Service",
            font=title_font,
            bg='#34495e',
            fg='#ecf0f1'
        )
        title_label.pack(pady=(10, 0))
        
        subtitle_label = tk.Label(
            title_frame,
            text="Management System",
            font=('Arial', 12),
            bg='#34495e',
            fg='#bdc3c7'
        )
        subtitle_label.pack()
        
        # Login form
        form_frame = tk.Frame(main_frame, bg='#34495e')
        form_frame.pack(fill='x', pady=20)
        
        # Username field
        tk.Label(
            form_frame,
            text="Username:",
            font=('Arial', 12, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.username_entry = tk.Entry(
            form_frame,
            font=('Arial', 12),
            relief='flat',
            bg='#ecf0f1',
            fg='#2c3e50',
            insertbackground='#2c3e50'
        )
        self.username_entry.pack(fill='x', ipady=8, pady=(0, 15))
        self.username_entry.focus()  # Set focus to username field
        
        # Password field
        tk.Label(
            form_frame,
            text="Password:",
            font=('Arial', 12, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.password_entry = tk.Entry(
            form_frame,
            font=('Arial', 12),
            show='*',
            relief='flat',
            bg='#ecf0f1',
            fg='#2c3e50',
            insertbackground='#2c3e50'
        )
        self.password_entry.pack(fill='x', ipady=8, pady=(0, 25))
        
        # Login button
        self.login_btn = tk.Button(
            form_frame,
            text="🔐 Login",
            command=self.handle_login,
            font=('Arial', 14, 'bold'),
            bg='#27ae60',
            fg='white',
            relief='flat',
            cursor='hand2',
            height=2
        )
        self.login_btn.pack(fill='x', pady=(0, 10))
        
        # Hover effects for login button
        self.login_btn.bind("<Enter>", lambda e: self.login_btn.configure(bg='#219a52'))
        self.login_btn.bind("<Leave>", lambda e: self.login_btn.configure(bg='#27ae60'))
        
        # Test connection button
        test_btn = tk.Button(
            form_frame,
            text="🔗 Test Database Connection",
            command=self.test_database_connection,
            font=('Arial', 10),
            bg='#3498db',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        test_btn.pack(fill='x', pady=(5, 0))
        
        # Hover effects for test button
        test_btn.bind("<Enter>", lambda e: test_btn.configure(bg='#2980b9'))
        test_btn.bind("<Leave>", lambda e: test_btn.configure(bg='#3498db'))
        
        # Info section
        info_frame = tk.Frame(main_frame, bg='#34495e')
        info_frame.pack(side='bottom', fill='x', pady=(30, 0))
        
        info_label = tk.Label(
            info_frame,
            text="💡 Enter any username and password to login\n(No authentication required for demo)",
            font=('Arial', 9),
            bg='#34495e',
            fg='#95a5a6',
            justify='center'
        )
        info_label.pack()
        
        # Bind Enter key to login
        self.window.bind('<Return>', lambda e: self.handle_login())
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="",
            font=('Arial', 9),
            bg='#34495e',
            fg='#e74c3c'
        )
        self.status_label.pack(pady=(10, 0))
    
    def test_database_connection(self):
        """Test the database connection"""
        self.status_label.config(text="Testing database connection...", fg='#f39c12')
        self.window.update()
        
        db = DatabaseConnection()
        connection = db.get_connection()
        
        if connection:
            self.status_label.config(text="✅ Database connection successful!", fg='#27ae60')
            db.close_connection()
            messagebox.showinfo(
                "Connection Test", 
                "✅ Successfully connected to PostgreSQL database!\n\n"
                f"Database: {db.db_config['database']}\n"
                f"Host: {db.db_config['host']}\n"
                f"User: {db.db_config['user']}"
            )
        else:
            self.status_label.config(text="❌ Database connection failed!", fg='#e74c3c')
            messagebox.showerror(
                "Connection Error", 
                "❌ Failed to connect to the database.\n\n"
                "Please check your database configuration and ensure PostgreSQL is running."
            )
    
    def handle_login(self):
        """Handle the login process"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        # Validate input (basic check)
        if not username or not password:
            self.status_label.config(text="❌ Please enter both username and password", fg='#e74c3c')
            return
        
        if not (username == "netflix_admin" and password == "password123"):
            self.status_label.config(text="❌ Invalid username or password", fg='#e74c3c')
            messagebox.showerror("Login Error", "❌ Invalid username or password.\n\nPlease try again.")
            return
        # Update status
        self.status_label.config(text="Logging in...", fg='#f39c12')
        self.window.update()
        
        # Test database connection
        self.db = DatabaseConnection()
        connection = self.db.get_connection()
        
        if not connection:
            self.status_label.config(text="❌ Database connection failed!", fg='#e74c3c')
            messagebox.showerror(
                "Login Error", 
                "❌ Cannot connect to the database.\n\n"
                "Please check your database configuration."
            )
            return
        
        # Simulate login process (no real authentication)
        self.status_label.config(text="✅ Login successful!", fg='#27ae60')
        
        # Show welcome message
        messagebox.showinfo(
            "Login Successful", 
            f"🎉 Welcome, {username}!\n\nYou have successfully logged into the Streaming Service Management System."
        )
        
        # Close login window and open main menu
        self.open_main_menu()
    
    def open_main_menu(self):
        """Close login window and open the main menu"""
        self.window.destroy()  # Close login window
        
        # Open main menu with database connection
        main_menu = MainMenuWindow(self.db)
        main_menu.run()
    
    def run(self):
        """Start the login window"""
        self.window.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox, font
import psycopg2
from psycopg2 import sql, Error
import configparser
import os

# ... (keeping your existing DatabaseConnection and MainMenuWindow classes as they are) ...

class CustomersCRUDWindow:
    """
    CRUD operations window for Customers table
    """
    
    def __init__(self, db_connection, parent_window):
        self.db = db_connection
        self.parent = parent_window
        self.window = tk.Toplevel(parent_window)
        self.selected_customer_id = None
        self.status_label = None  # Initialize status_label    
        self.setup_window()
        self.create_widgets()
        self.load_customers()
    
    def setup_window(self):
        """Configure the customers CRUD window"""
        self.window.title("Manage Customers")
        self.window.geometry("1400x700")  # Made wider to accommodate new fields
        self.window.configure(bg='#2c3e50')
        
        # Center the window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (1400 // 2)
        y = (self.window.winfo_screenheight() // 2) - (700 // 2)
        self.window.geometry(f"1400x700+{x}+{y}")
        
        # Make window modal
        self.window.transient(self.parent)
        self.window.grab_set()
        
        # Handle window close event
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_widgets(self):
        """Create the customers CRUD interface"""
        # Title
        title_label = tk.Label(
            self.window,
            text="👥 Customer Management",
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=15)
        
        # Main container
        main_container = tk.Frame(self.window, bg='#2c3e50')
        main_container.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Left panel for form
        left_panel = tk.Frame(main_container, bg='#34495e', width=450)  # Made wider
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # Right panel for table
        right_panel = tk.Frame(main_container, bg='#34495e')
        right_panel.pack(side='right', expand=True, fill='both')
        
        # Create form in left panel
        self.create_form(left_panel)
        
        # Create table in right panel
        self.create_table(right_panel)
        
        # Status bar
        self.create_status_bar()
    
    def create_form(self, parent):
        """Create the customer form with scrollbar (original sizes)"""
        # Create a canvas and scrollbar for scrolling
        canvas = tk.Canvas(parent, bg='#34495e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#34495e')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "what")
        
        # Bind mouse wheel to canvas
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Form title (ORIGINAL SIZE)
        form_title = tk.Label(
            scrollable_frame,
            text="📝 Customer Details",
            font=('Arial', 14, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        )
        form_title.pack(pady=(15, 10))
        
        # Form frame (ORIGINAL SIZE)
        form_frame = tk.Frame(scrollable_frame, bg='#34495e')
        form_frame.pack(fill='x', padx=100) #20
        
        # Customer ID (ORIGINAL SIZE)
        tk.Label(
            form_frame,
            text="Customer ID:",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(10, 5))

        self.id_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.id_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Customer Name (ORIGINAL SIZE)
        tk.Label(
            form_frame,
            text="Customer Name:",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.name_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.name_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Date of Birth (ORIGINAL SIZE)
        tk.Label(
            form_frame,
            text="Date of Birth (YYYY-MM-DD):",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.dob_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.dob_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Customer Since (ORIGINAL SIZE)
        tk.Label(
            form_frame,
            text="Customer Since (YYYY-MM-DD):",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.since_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.since_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Plan ID (ORIGINAL SIZE)
        tk.Label(
            form_frame,
            text="Plan ID:",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.plan_id_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.plan_id_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Discount ID (ORIGINAL SIZE)
        tk.Label(
            form_frame,
            text="Discount ID:",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.discount_id_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.discount_id_entry.pack(fill='x', ipady=5, pady=(0, 20))
        
        # Buttons frame (ORIGINAL SIZE)
        buttons_frame = tk.Frame(form_frame, bg='#34495e')
        buttons_frame.pack(fill='x', pady=10)
        
        # Insert button (ORIGINAL SIZE)
        insert_btn = tk.Button(
            buttons_frame,
            text="➕ Insert Customer",
            command=self.insert_customer,
            font=('Arial', 10, 'bold'),
            bg='#27ae60',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        insert_btn.pack(fill='x', pady=2)
        
        # Update button (ORIGINAL SIZE)
        update_btn = tk.Button(
            buttons_frame,
            text="✏️ Update Customer",
            command=self.update_customer,
            font=('Arial', 10, 'bold'),
            bg='#f39c12',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        update_btn.pack(fill='x', pady=2)
        
        # Delete button (ORIGINAL SIZE)
        delete_btn = tk.Button(
            buttons_frame,
            text="🗑️ Delete Customer",
            command=self.delete_customer,
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        delete_btn.pack(fill='x', pady=2)
        
        # Clear form button (ORIGINAL SIZE)
        clear_btn = tk.Button(
            buttons_frame,
            text="🔄 Clear Form",
            command=self.clear_form,
            font=('Arial', 10, 'bold'),
            bg='#95a5a6',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        clear_btn.pack(fill='x', pady=2)
        
        # Add hover effects
        for btn in [insert_btn, update_btn, delete_btn, clear_btn]:
            self.add_hover_effect(btn)
        
        # Add bottom padding so the last button is fully accessible when scrolling
        tk.Label(scrollable_frame, text="", bg='#34495e').pack(pady=20)

    def create_table(self, parent):
        """Create the customers table"""
        # Table title
        table_title = tk.Label(
            parent,
            text="📋 Customers List",
            font=('Arial', 14, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        )
        table_title.pack(pady=(15, 10))
        
        # Table frame
        table_frame = tk.Frame(parent, bg='#34495e')
        table_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Create Treeview with additional columns
        columns = ('ID', 'Customer Name', 'Date of Birth', 'Customer Since', 'Plan ID', 'Discount ID')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        # Define column headings and widths
        self.tree.heading('ID', text='ID')
        self.tree.heading('Customer Name', text='Customer Name')
        self.tree.heading('Date of Birth', text='Date of Birth')
        self.tree.heading('Customer Since', text='Customer Since')
        self.tree.heading('Plan ID', text='Plan ID')
        self.tree.heading('Discount ID', text='Discount ID')
        
        self.tree.column('ID', width=60, anchor='center')
        self.tree.column('Customer Name', width=150, anchor='w')
        self.tree.column('Date of Birth', width=100, anchor='center')
        self.tree.column('Customer Since', width=100, anchor='center')
        self.tree.column('Plan ID', width=80, anchor='center')
        self.tree.column('Discount ID', width=80, anchor='center')
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack treeview and scrollbars
        self.tree.pack(side='left', expand=True, fill='both')
        v_scrollbar.pack(side='right', fill='y')
        h_scrollbar.pack(side='bottom', fill='x')
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)
        
        # Refresh button for table
        refresh_btn = tk.Button(
            parent,
            text="🔄 Refresh Table",
            command=self.load_customers,
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        refresh_btn.pack(pady=10)
        self.add_hover_effect(refresh_btn)
    
    def create_status_bar(self):
        """Create status bar"""
        status_frame = tk.Frame(self.window, bg='#34495e', height=30)
        status_frame.pack(side='bottom', fill='x')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 9)
        )
        self.status_label.pack(side='left', padx=10, pady=5)
        
        # Close button
        close_btn = tk.Button(
            status_frame,
            text="❌ Close",
            command=self.on_closing,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 9),
            relief='flat',
            cursor='hand2'
        )
        close_btn.pack(side='right', padx=10, pady=3)
    
    def add_hover_effect(self, button):
        """Add hover effect to buttons"""
        original_color = button.cget('bg')
        
        def on_enter(e):
            # Darken the color on hover
            if original_color == '#27ae60':
                button.configure(bg='#219a52')
            elif original_color == '#f39c12':
                button.configure(bg='#d68910')
            elif original_color == '#e74c3c':
                button.configure(bg='#c0392b')
            elif original_color == '#95a5a6':
                button.configure(bg='#7f8c8d')
            elif original_color == '#3498db':
                button.configure(bg='#2980b9')
        
        def on_leave(e):
            button.configure(bg=original_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def update_status(self, message, color='#ecf0f1'):
        """Update status bar message"""
        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.config(text=message, fg=color)
            self.window.update()
        else:
            print(f"Status: {message}")  # Fallback to console output
    
    def validate_date(self, date_string):
        """Validate date format (YYYY-MM-DD)"""
        try:
            from datetime import datetime
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    def clear_form(self):
        """Clear all form fields"""
        self.id_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.dob_entry.delete(0, 'end')
        self.since_entry.delete(0, 'end')
        self.plan_id_entry.delete(0, 'end')
        self.discount_id_entry.delete(0, 'end')
        self.selected_customer_id = None
        self.update_status("Form cleared")
    
    def load_customers(self):
        """Load customers from database"""
        try:
            self.update_status("Loading customers...", '#f39c12')
            
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Execute query with new columns
            cursor = self.db.cursor
            cursor.execute("""
                SELECT customer_id, customer_name, date_of_birth, customer_since, 
                       plan_id, discount_id 
                FROM Customers 
                ORDER BY customer_id
            """)
            customers = cursor.fetchall()
            
            # Insert data into treeview
            for customer in customers:
                self.tree.insert('', 'end', values=customer)
            
            self.update_status(f"Loaded {len(customers)} customers", '#27ae60')
            
        except Exception as e:
            error_msg = f"Error loading customers: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def on_item_select(self, event):
        """Handle item selection in treeview"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            # Populate form with selected customer data
            self.clear_form()
            self.selected_customer_id = values[0]
            self.id_entry.insert(0, str(values[0]))
            self.name_entry.insert(0, values[1])
            self.dob_entry.insert(0, str(values[2]))
            self.since_entry.insert(0, str(values[3]))
            
            # Handle plan_id and discount_id (they might be None/NULL)
            if values[4] is not None:
                self.plan_id_entry.insert(0, str(values[4]))
            if values[5] is not None:
                self.discount_id_entry.insert(0, str(values[5]))
            
            self.update_status(f"Selected customer: {values[1]}")
    
    def insert_customer(self):
        """Insert new customer"""
        cursor = None
        try:
            # Get form data
            customer_id = self.id_entry.get().strip()
            name = self.name_entry.get().strip()
            dob = self.dob_entry.get().strip()
            since = self.since_entry.get().strip()
            plan_id = self.plan_id_entry.get().strip()
            discount_id = self.discount_id_entry.get().strip()
            
            # Validate input
            if not name:
                messagebox.showerror("Validation Error", "Customer name is required!")
                return
            
            if not dob or not self.validate_date(dob):
                messagebox.showerror("Validation Error", "Please enter a valid date of birth (YYYY-MM-DD)!")
                return
            
            if not since or not self.validate_date(since):
                messagebox.showerror("Validation Error", "Please enter a valid customer since date (YYYY-MM-DD)!")
                return
            
            # Convert empty strings to None for optional fields
            customer_id = customer_id if customer_id else None
            plan_id = int(plan_id) if plan_id else None
            discount_id = int(discount_id) if discount_id else None
            
            self.update_status("Inserting customer...", '#f39c12')
            
            # Get cursor
            cursor = self.db.cursor
            
            # Execute insert query
            if customer_id:
                insert_query = """
                    INSERT INTO Customers (customer_id, customer_name, date_of_birth, customer_since, plan_id, discount_id) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (customer_id, name, dob, since, plan_id, discount_id))
            else:
                insert_query = """
                    INSERT INTO Customers (customer_name, date_of_birth, customer_since, plan_id, discount_id) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (name, dob, since, plan_id, discount_id))
            
            self.db.connection.commit()
            
            # Clear form and refresh table
            self.clear_form()
            self.load_customers()
            
            self.update_status(f"Customer '{name}' inserted successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Customer '{name}' has been added successfully!")
            
        except ValueError as ve:
            error_msg = "Please enter valid numeric values for Plan ID and Discount ID!"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Validation Error", error_msg)
            
        except Exception as e:
            if self.db.connection:
                self.db.connection.rollback()
            error_msg = f"Error inserting customer: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)

    def delete_customer(self):
        """Delete selected customer"""
        try:
            if not self.selected_customer_id:
                messagebox.showwarning("Selection Error", "Please select a customer to delete!")
                return
            
            # Get customer name for confirmation
            customer_name = self.name_entry.get().strip()
            
            # Confirm deletion
            if not messagebox.askyesno("Confirm Delete", 
                                    f"Are you sure you want to delete customer '{customer_name}'?\n\nThis action cannot be undone!"):
                return
            
            self.update_status("Deleting customer...", '#f39c12')
            
            # Execute delete query
            cursor = self.db.cursor
            delete_query = "DELETE FROM Customers WHERE customer_id = %s"
            cursor.execute(delete_query, (self.selected_customer_id,))
            self.db.connection.commit()
            
            # Clear form and refresh table
            self.clear_form()
            self.load_customers()
            
            self.update_status(f"Customer '{customer_name}' deleted successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Customer '{customer_name}' has been deleted successfully!")
            
        except Exception as e:
            self.db.connection.rollback()
            error_msg = f"Error deleting customer: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)

    def update_customer(self):
        """Update selected customer"""
        cursor = None
        try:
            if not self.selected_customer_id:
                messagebox.showwarning("Selection Error", "Please select a customer to update!")
                return
            
            # Get form data
            name = self.name_entry.get().strip()
            dob = self.dob_entry.get().strip()
            since = self.since_entry.get().strip()
            plan_id = self.plan_id_entry.get().strip()
            discount_id = self.discount_id_entry.get().strip()
            
            # Validate input
            if not name:
                messagebox.showerror("Validation Error", "Customer name is required!")
                return
            
            if not dob or not self.validate_date(dob):
                messagebox.showerror("Validation Error", "Please enter a valid date of birth (YYYY-MM-DD)!")
                return
            
            if not since or not self.validate_date(since):
                messagebox.showerror("Validation Error", "Please enter a valid customer since date (YYYY-MM-DD)!")
                return
            
            # Convert empty strings to None for optional fields
            plan_id = int(plan_id) if plan_id else None
            discount_id = int(discount_id) if discount_id else None
            
            # Confirm update
            if not messagebox.askyesno("Confirm Update", f"Are you sure you want to update customer '{name}'?"):
                return
            
            self.update_status("Updating customer...", '#f39c12')
            
            # Get cursor
            cursor = self.db.cursor
            
            # Execute update query
            update_query = """
                UPDATE Customers 
                SET customer_name = %s, date_of_birth = %s, customer_since = %s, 
                    plan_id = %s, discount_id = %s
                WHERE customer_id = %s
            """
            cursor.execute(update_query, (name, dob, since, plan_id, discount_id, self.selected_customer_id))
            self.db.connection.commit()
            
            # Clear form and refresh table
            self.clear_form()
            self.load_customers()
            
            self.update_status(f"Customer '{name}' updated successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Customer '{name}' has been updated successfully!")
            
        except ValueError as ve:
            error_msg = "Please enter valid numeric values for Plan ID and Discount ID!"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Validation Error", error_msg)
            
        except Exception as e:
            if self.db.connection:
                self.db.connection.rollback()
            error_msg = f"Error updating customer: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)

    def on_closing(self):
        """Handle window closing event"""
        self.window.grab_release()  # Release the modal grab
        self.window.destroy()       # Close the window

    def run(self):
        """Start the customers CRUD window"""
        pass  # Window is already created and shown

    #


class ProfilesCRUDWindow:
    """
    CRUD operations window for Profiles table
    """
    
    def __init__(self, db_connection, parent_window):
        self.db = db_connection
        self.parent = parent_window
        self.window = tk.Toplevel(parent_window)
        self.selected_profile_id = None
        self.status_label = None
        self.customer_ids = []  # Store available customer IDs
        self.setup_window()
        self.create_widgets()
        self.load_customer_ids()
        self.load_profiles()
    
    def setup_window(self):
        """Configure the profiles CRUD window"""
        self.window.title("Manage Profiles")
        self.window.geometry("1400x700")
        self.window.configure(bg='#2c3e50')
        
        # Center the window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (1400 // 2)
        y = (self.window.winfo_screenheight() // 2) - (700 // 2)
        self.window.geometry(f"1400x700+{x}+{y}")
        
        # Make window modal
        self.window.transient(self.parent)
        self.window.grab_set()
        
        # Handle window close event
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_widgets(self):
        """Create the profiles CRUD interface"""
        # Title
        title_label = tk.Label(
            self.window,
            text="👤 Profile Management",
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=15)
        
        # Main container
        main_container = tk.Frame(self.window, bg='#2c3e50')
        main_container.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Left panel for form
        left_panel = tk.Frame(main_container, bg='#34495e', width=450)
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # Right panel for table
        right_panel = tk.Frame(main_container, bg='#34495e')
        right_panel.pack(side='right', expand=True, fill='both')
        
        # Create form in left panel
        self.create_form(left_panel)
        
        # Create table in right panel
        self.create_table(right_panel)
        
        # Status bar
        self.create_status_bar()
    
    def create_form(self, parent):
        """Create the profile form"""
        # Form title
        form_title = tk.Label(
            parent,
            text="📝 Profile Details",
            font=('Arial', 14, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        )
        form_title.pack(pady=(15, 10))
        
        # Form frame
        form_frame = tk.Frame(parent, bg='#34495e')
        form_frame.pack(fill='x', padx=20)
        
        # Profile ID (for manual entry)
        tk.Label(
            form_frame,
            text="Profile ID:",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(10, 5))

        self.profile_id_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.profile_id_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Profile Name
        tk.Label(
            form_frame,
            text="Profile Name: *",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.profile_name_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.profile_name_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Is Online (Boolean field)
        tk.Label(
            form_frame,
            text="Online Status:",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.is_online_var = tk.BooleanVar()
        self.is_online_checkbox = tk.Checkbutton(
            form_frame,
            text="Profile is currently online",
            variable=self.is_online_var,
            font=('Arial', 10),
            bg='#34495e',
            fg='#ecf0f1',
            selectcolor='#2c3e50',
            activebackground='#34495e',
            activeforeground='#ecf0f1'
        )
        self.is_online_checkbox.pack(anchor='w', pady=(0, 10))
        
        # Watch History ID
        tk.Label(
            form_frame,
            text="Watch History ID:",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.watch_history_id_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.watch_history_id_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Customer ID (Dropdown)
        tk.Label(
            form_frame,
            text="Customer: *",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.customer_combobox = ttk.Combobox(
            form_frame,
            font=('Arial', 11),
            state='readonly'
        )
        self.customer_combobox.pack(fill='x', ipady=5, pady=(0, 20))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame, bg='#34495e')
        buttons_frame.pack(fill='x', pady=10)
        
        # Insert button
        insert_btn = tk.Button(
            buttons_frame,
            text="➕ Insert Profile",
            command=self.insert_profile,
            font=('Arial', 10, 'bold'),
            bg='#27ae60',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        insert_btn.pack(fill='x', pady=2)
        
        # Update button
        update_btn = tk.Button(
            buttons_frame,
            text="✏️ Update Profile",
            command=self.update_profile,
            font=('Arial', 10, 'bold'),
            bg='#f39c12',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        update_btn.pack(fill='x', pady=2)
        
        # Delete button
        delete_btn = tk.Button(
            buttons_frame,
            text="🗑️ Delete Profile",
            command=self.delete_profile,
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        delete_btn.pack(fill='x', pady=2)
        
        # Clear form button
        clear_btn = tk.Button(
            buttons_frame,
            text="🔄 Clear Form",
            command=self.clear_form,
            font=('Arial', 10, 'bold'),
            bg='#95a5a6',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        clear_btn.pack(fill='x', pady=2)
        
        # Refresh customers button
        refresh_customers_btn = tk.Button(
            buttons_frame,
            text="🔄 Refresh Customers",
            command=self.load_customer_ids,
            font=('Arial', 10, 'bold'),
            bg='#9b59b6',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        refresh_customers_btn.pack(fill='x', pady=2)
        
        # Add hover effects
        for btn in [insert_btn, update_btn, delete_btn, clear_btn, refresh_customers_btn]:
            self.add_hover_effect(btn)
    
    def create_table(self, parent):
        """Create the profiles table"""
        # Table title
        table_title = tk.Label(
            parent,
            text="📋 Profiles List",
            font=('Arial', 14, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        )
        table_title.pack(pady=(15, 10))
        
        # Table frame
        table_frame = tk.Frame(parent, bg='#34495e')
        table_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Create Treeview
        columns = ('Profile ID', 'Profile Name', 'Online Status', 'Watch History ID', 'Customer ID', 'Customer Name')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        # Define column headings and widths
        self.tree.heading('Profile ID', text='Profile ID')
        self.tree.heading('Profile Name', text='Profile Name')
        self.tree.heading('Online Status', text='Online')
        self.tree.heading('Watch History ID', text='Watch History ID')
        self.tree.heading('Customer ID', text='Customer ID')
        self.tree.heading('Customer Name', text='Customer Name')
        
        self.tree.column('Profile ID', width=80, anchor='center')
        self.tree.column('Profile Name', width=150, anchor='w')
        self.tree.column('Online Status', width=80, anchor='center')
        self.tree.column('Watch History ID', width=120, anchor='center')
        self.tree.column('Customer ID', width=100, anchor='center')
        self.tree.column('Customer Name', width=150, anchor='w')
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack treeview and scrollbars
        self.tree.pack(side='left', expand=True, fill='both')
        v_scrollbar.pack(side='right', fill='y')
        h_scrollbar.pack(side='bottom', fill='x')
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)
        
        # Refresh button for table
        refresh_btn = tk.Button(
            parent,
            text="🔄 Refresh Table",
            command=self.load_profiles,
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        refresh_btn.pack(pady=10)
        self.add_hover_effect(refresh_btn)
    
    def create_status_bar(self):
        """Create status bar"""
        status_frame = tk.Frame(self.window, bg='#34495e', height=30)
        status_frame.pack(side='bottom', fill='x')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 9)
        )
        self.status_label.pack(side='left', padx=10, pady=5)
        
        # Close button
        close_btn = tk.Button(
            status_frame,
            text="❌ Close",
            command=self.on_closing,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 9),
            relief='flat',
            cursor='hand2'
        )
        close_btn.pack(side='right', padx=10, pady=3)
    
    def add_hover_effect(self, button):
        """Add hover effect to buttons"""
        original_color = button.cget('bg')
        
        def on_enter(e):
            # Darken the color on hover
            if original_color == '#27ae60':
                button.configure(bg='#219a52')
            elif original_color == '#f39c12':
                button.configure(bg='#d68910')
            elif original_color == '#e74c3c':
                button.configure(bg='#c0392b')
            elif original_color == '#95a5a6':
                button.configure(bg='#7f8c8d')
            elif original_color == '#3498db':
                button.configure(bg='#2980b9')
            elif original_color == '#9b59b6':
                button.configure(bg='#8e44ad')
        
        def on_leave(e):
            button.configure(bg=original_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def update_status(self, message, color='#ecf0f1'):
        """Update status bar message"""
        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.config(text=message, fg=color)
            self.window.update()
        else:
            print(f"Status: {message}")  # Fallback to console output
    
    def clear_form(self):
        """Clear all form fields"""
        self.profile_id_entry.delete(0, 'end')
        self.profile_name_entry.delete(0, 'end')
        self.is_online_var.set(False)
        self.watch_history_id_entry.delete(0, 'end')
        self.customer_combobox.set('')
        self.selected_profile_id = None
        self.update_status("Form cleared")
    
    def load_customer_ids(self):
        """Load customer IDs and names for the dropdown"""
        try:
            self.update_status("Loading customers...", '#f39c12')
            
            cursor = self.db.cursor
            cursor.execute("SELECT customer_id, customer_name FROM Customers ORDER BY customer_name")
            customers = cursor.fetchall()
            
            # Create list of customer options (ID - Name format)
            customer_options = []
            for customer in customers:
                customer_options.append(f"{customer[0]} - {customer[1]}")
            
            # Update combobox
            self.customer_combobox['values'] = customer_options
            self.customer_ids = customers  # Store for reference
            
            self.update_status(f"Loaded {len(customers)} customers", '#27ae60')
            
        except Exception as e:
            error_msg = f"Error loading customers: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def load_profiles(self):
        """Load profiles from database"""
        try:
            self.update_status("Loading profiles...", '#f39c12')
            
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Execute query with JOIN to get customer name
            cursor = self.db.cursor
            cursor.execute("""
                SELECT p.profile_id, p.profile_name, p.is_online, p.watch_history_id, 
                       p.customer_id, c.customer_name
                FROM Profiles p
                LEFT JOIN Customers c ON p.customer_id = c.customer_id
                ORDER BY p.profile_id
            """)
            profiles = cursor.fetchall()
            
            # Insert data into treeview
            for profile in profiles:
                # Convert boolean to readable text
                online_status = "Yes" if profile[2] else "No"
                # Handle None values
                values = (
                    profile[0],  # profile_id
                    profile[1],  # profile_name
                    online_status,  # is_online
                    profile[3] if profile[3] is not None else "",  # watch_history_id
                    profile[4],  # customer_id
                    profile[5] if profile[5] is not None else "Unknown"  # customer_name
                )
                self.tree.insert('', 'end', values=values)
            
            self.update_status(f"Loaded {len(profiles)} profiles", '#27ae60')
            
        except Exception as e:
            error_msg = f"Error loading profiles: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def on_item_select(self, event):
        """Handle item selection in treeview"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            # Populate form with selected profile data
            self.clear_form()
            self.selected_profile_id = values[0]
            
            # Fill form fields
            self.profile_id_entry.insert(0, str(values[0]))
            self.profile_name_entry.insert(0, values[1])
            self.is_online_var.set(values[2] == "Yes")
            
            # Handle watch_history_id (might be empty)
            if values[3]:
                self.watch_history_id_entry.insert(0, str(values[3]))
            
            # Set customer combobox
            customer_id = values[4]
            customer_name = values[5]
            if customer_id and customer_name != "Unknown":
                self.customer_combobox.set(f"{customer_id} - {customer_name}")
            
            self.update_status(f"Selected profile: {values[1]}")
    
    def get_selected_customer_id(self):
        """Extract customer ID from combobox selection"""
        selection = self.customer_combobox.get()
        if selection:
            try:
                # Extract customer ID from "ID - Name" format
                customer_id = int(selection.split(' - ')[0])
                return customer_id
            except (ValueError, IndexError):
                return None
        return None
    
    def insert_profile(self):
        """Insert new profile"""
        cursor = None
        try:
            # Get form data
            profile_id = self.profile_id_entry.get().strip()
            profile_name = self.profile_name_entry.get().strip()
            is_online = self.is_online_var.get()
            watch_history_id = self.watch_history_id_entry.get().strip()
            customer_id = self.get_selected_customer_id()
            
            # Validate input
            if not profile_name:
                messagebox.showerror("Validation Error", "Profile name is required!")
                return
            
            if not customer_id:
                messagebox.showerror("Validation Error", "Please select a customer!")
                return
            
            # Convert empty strings to None for optional fields
            profile_id = int(profile_id) if profile_id else None
            watch_history_id = int(watch_history_id) if watch_history_id else None
            
            self.update_status("Inserting profile...", '#f39c12')
            
            # Get cursor
            cursor = self.db.cursor
            
            # Execute insert query
            if profile_id:
                insert_query = """
                    INSERT INTO Profiles (profile_id, profile_name, is_online, watch_history_id, customer_id) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (profile_id, profile_name, is_online, watch_history_id, customer_id))
            else:
                insert_query = """
                    INSERT INTO Profiles (profile_name, is_online, watch_history_id, customer_id) 
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (profile_name, is_online, watch_history_id, customer_id))
            
            self.db.connection.commit()
            
            # Clear form and refresh table
            self.clear_form()
            self.load_profiles()
            
            self.update_status(f"Profile '{profile_name}' inserted successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Profile '{profile_name}' has been added successfully!")
            
        except ValueError as ve:
            error_msg = "Please enter valid numeric values for Profile ID and Watch History ID!"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Validation Error", error_msg)
            
        except Exception as e:
            if self.db.connection:
                self.db.connection.rollback()
            error_msg = f"Error inserting profile: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def update_profile(self):
        """Update selected profile"""
        cursor = None
        try:
            if not self.selected_profile_id:
                messagebox.showwarning("Selection Error", "Please select a profile to update!")
                return
            
            # Get form data
            profile_name = self.profile_name_entry.get().strip()
            is_online = self.is_online_var.get()
            watch_history_id = self.watch_history_id_entry.get().strip()
            customer_id = self.get_selected_customer_id()
            
            # Validate input
            if not profile_name:
                messagebox.showerror("Validation Error", "Profile name is required!")
                return
            
            if not customer_id:
                messagebox.showerror("Validation Error", "Please select a customer!")
                return
            
            # Convert empty strings to None for optional fields
            watch_history_id = int(watch_history_id) if watch_history_id else None
            
            # Confirm update
            if not messagebox.askyesno("Confirm Update", f"Are you sure you want to update profile '{profile_name}'?"):
                return
            
            self.update_status("Updating profile...", '#f39c12')
            
            # Get cursor
            cursor = self.db.cursor
            
            # Execute update query
            update_query = """
                UPDATE Profiles 
                SET profile_name = %s, is_online = %s, watch_history_id = %s, customer_id = %s
                WHERE profile_id = %s
            """
            cursor.execute(update_query, (profile_name, is_online, watch_history_id, customer_id, self.selected_profile_id))
            self.db.connection.commit()
            
            # Clear form and refresh table
            self.clear_form()
            self.load_profiles()
            
            self.update_status(f"Profile '{profile_name}' updated successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Profile '{profile_name}' has been updated successfully!")
            
        except ValueError as ve:
            error_msg = "Please enter valid numeric values for Watch History ID!"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Validation Error", error_msg)
            
        except Exception as e:
            if self.db.connection:
                self.db.connection.rollback()
            error_msg = f"Error updating profile: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def delete_profile(self):
        """Delete selected profile"""
        try:
            if not self.selected_profile_id:
                messagebox.showwarning("Selection Error", "Please select a profile to delete!")
                return
            
            # Get profile name for confirmation
            profile_name = self.profile_name_entry.get().strip()
            
            # Confirm deletion
            if not messagebox.askyesno("Confirm Delete", 
                                    f"Are you sure you want to delete profile '{profile_name}'?\n\nThis action cannot be undone!"):
                return
            
            self.update_status("Deleting profile...", '#f39c12')
            
            # Execute delete query
            cursor = self.db.cursor
            delete_query = "DELETE FROM Profiles WHERE profile_id = %s"
            cursor.execute(delete_query, (self.selected_profile_id,))
            self.db.connection.commit()
            
            # Clear form and refresh table
            self.clear_form()
            self.load_profiles()
            
            self.update_status(f"Profile '{profile_name}' deleted successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Profile '{profile_name}' has been deleted successfully!")
            
        except Exception as e:
            self.db.connection.rollback()
            error_msg = f"Error deleting profile: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def on_closing(self):
        """Handle window closing event"""
        self.window.grab_release()  # Release the modal grab
        self.window.destroy()       # Close the window
    
    def run(self):
        """Start the profiles CRUD window"""
        pass  # Window is already created and shown


class WatchHistoryCRUDWindow:
    """
    CRUD operations window for Watch_History table
    """
    
    def __init__(self, db_connection, parent_window):
        self.db = db_connection
        self.parent = parent_window
        self.window = tk.Toplevel(parent_window)
        self.selected_watch_history_id = None
        self.status_label = None
        self.profiles = []  # Store available profiles
        self.setup_window()
        self.create_widgets()
        self.load_profiles()
        self.load_watch_history()
    
    def setup_window(self):
        """Configure the watch history CRUD window"""
        self.window.title("Manage Watch History")
        self.window.geometry("1500x700")
        self.window.configure(bg='#2c3e50')
        
        # Center the window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (1500 // 2)
        y = (self.window.winfo_screenheight() // 2) - (700 // 2)
        self.window.geometry(f"1500x700+{x}+{y}")
        
        # Make window modal
        self.window.transient(self.parent)
        self.window.grab_set()
        
        # Handle window close event
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_widgets(self):
        """Create the watch history CRUD interface"""
        # Title
        title_label = tk.Label(
            self.window,
            text="📺 Watch History Management",
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=15)
        
        # Main container
        main_container = tk.Frame(self.window, bg='#2c3e50')
        main_container.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Left panel for form
        left_panel = tk.Frame(main_container, bg='#34495e', width=500)
        left_panel.pack(side='left', fill='y', padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # Right panel for table
        right_panel = tk.Frame(main_container, bg='#34495e')
        right_panel.pack(side='right', expand=True, fill='both')
        
        # Create form in left panel
        self.create_form(left_panel)
        
        # Create table in right panel
        self.create_table(right_panel)
        
        # Status bar
        self.create_status_bar()
    
    def create_form(self, parent):
        """Create the watch history form"""
        # Form title
        form_title = tk.Label(
            parent,
            text="📝 Watch History Details",
            font=('Arial', 14, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        )
        form_title.pack(pady=(15, 10))
        
        # Form frame
        form_frame = tk.Frame(parent, bg='#34495e')
        form_frame.pack(fill='x', padx=20)
        
        # Watch History ID (for manual entry)
        tk.Label(
            form_frame,
            text="Watch History ID:",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(10, 5))

        self.watch_history_id_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.watch_history_id_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Profile ID (Dropdown)
        tk.Label(
            form_frame,
            text="Profile: *",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.profile_combobox = ttk.Combobox(
            form_frame,
            font=('Arial', 11),
            state='readonly'
        )
        self.profile_combobox.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Movie ID
        tk.Label(
            form_frame,
            text="Movie ID: *",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.movie_id_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.movie_id_entry.pack(fill='x', ipady=5, pady=(0, 10))
        
        # Watch Date with calendar-like input
        tk.Label(
            form_frame,
            text="Watch Date (YYYY-MM-DD): *",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        # Date input frame
        date_frame = tk.Frame(form_frame, bg='#34495e')
        date_frame.pack(fill='x', pady=(0, 10))
        
        self.watch_date_entry = tk.Entry(
            date_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.watch_date_entry.pack(side='left', fill='x', expand=True, ipady=5)
        
        # Today button
        today_btn = tk.Button(
            date_frame,
            text="Today",
            command=self.set_today_date,
            font=('Arial', 9),
            bg='#3498db',
            fg='white',
            relief='flat',
            cursor='hand2',
            padx=10
        )
        today_btn.pack(side='right', padx=(5, 0))
        
        # Duration Watched
        tk.Label(
            form_frame,
            text="Duration Watched (minutes): *",
            font=('Arial', 11, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(anchor='w', pady=(0, 5))
        
        self.duration_entry = tk.Entry(
            form_frame,
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='flat'
        )
        self.duration_entry.pack(fill='x', ipady=5, pady=(0, 20))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame, bg='#34495e')
        buttons_frame.pack(fill='x', pady=10)
        
        # Insert button
        insert_btn = tk.Button(
            buttons_frame,
            text="➕ Insert Watch Record",
            command=self.insert_watch_history,
            font=('Arial', 10, 'bold'),
            bg='#27ae60',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        insert_btn.pack(fill='x', pady=2)
        
        # Update button
        update_btn = tk.Button(
            buttons_frame,
            text="✏️ Update Watch Record",
            command=self.update_watch_history,
            font=('Arial', 10, 'bold'),
            bg='#f39c12',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        update_btn.pack(fill='x', pady=2)
        
        # Delete button
        delete_btn = tk.Button(
            buttons_frame,
            text="🗑️ Delete Watch Record",
            command=self.delete_watch_history,
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        delete_btn.pack(fill='x', pady=2)
        
        # Clear form button
        clear_btn = tk.Button(
            buttons_frame,
            text="🔄 Clear Form",
            command=self.clear_form,
            font=('Arial', 10, 'bold'),
            bg='#95a5a6',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        clear_btn.pack(fill='x', pady=2)
        
        # Refresh profiles button
        refresh_profiles_btn = tk.Button(
            buttons_frame,
            text="🔄 Refresh Profiles",
            command=self.load_profiles,
            font=('Arial', 10, 'bold'),
            bg='#9b59b6',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        refresh_profiles_btn.pack(fill='x', pady=2)
        
        # Add hover effects
        for btn in [insert_btn, update_btn, delete_btn, clear_btn, refresh_profiles_btn, today_btn]:
            self.add_hover_effect(btn)
    
    def create_table(self, parent):
        """Create the watch history table"""
        # Table title
        table_title = tk.Label(
            parent,
            text="📋 Watch History List",
            font=('Arial', 14, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        )
        table_title.pack(pady=(15, 10))
        
        # Table frame
        table_frame = tk.Frame(parent, bg='#34495e')
        table_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Create Treeview
        columns = ('Watch History ID', 'Profile ID', 'Profile Name', 'Movie ID', 'Watch Date', 'Duration (min)')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        # Define column headings and widths
        self.tree.heading('Watch History ID', text='WH ID')
        self.tree.heading('Profile ID', text='Profile ID')
        self.tree.heading('Profile Name', text='Profile Name')
        self.tree.heading('Movie ID', text='Movie ID')
        self.tree.heading('Watch Date', text='Watch Date')
        self.tree.heading('Duration (min)', text='Duration (min)')
        
        self.tree.column('Watch History ID', width=80, anchor='center')
        self.tree.column('Profile ID', width=80, anchor='center')
        self.tree.column('Profile Name', width=150, anchor='w')
        self.tree.column('Movie ID', width=80, anchor='center')
        self.tree.column('Watch Date', width=120, anchor='center')
        self.tree.column('Duration (min)', width=120, anchor='center')
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack treeview and scrollbars
        self.tree.pack(side='left', expand=True, fill='both')
        v_scrollbar.pack(side='right', fill='y')
        h_scrollbar.pack(side='bottom', fill='x')
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)
        
        # Refresh button for table
        refresh_btn = tk.Button(
            parent,
            text="🔄 Refresh Table",
            command=self.load_watch_history,
            font=('Arial', 10, 'bold'),
            bg='#3498db',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        refresh_btn.pack(pady=10)
        self.add_hover_effect(refresh_btn)
    
    def create_status_bar(self):
        """Create status bar"""
        status_frame = tk.Frame(self.window, bg='#34495e', height=30)
        status_frame.pack(side='bottom', fill='x')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 9)
        )
        self.status_label.pack(side='left', padx=10, pady=5)
        
        # Close button
        close_btn = tk.Button(
            status_frame,
            text="❌ Close",
            command=self.on_closing,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 9),
            relief='flat',
            cursor='hand2'
        )
        close_btn.pack(side='right', padx=10, pady=3)
    
    
    def add_hover_effect(self, button):
        """Add hover effect to buttons"""
        original_color = button.cget('bg')
        
        def on_enter(e):
            # Darken the color on hover
            if original_color == '#27ae60':
                button.configure(bg='#219a52')
            elif original_color == '#f39c12':
                button.configure(bg='#d68910')
            elif original_color == '#e74c3c':
                button.configure(bg='#c0392b')
            elif original_color == '#95a5a6':
                button.configure(bg='#7f8c8d')
            elif original_color == '#3498db':
                button.configure(bg='#2980b9')
            elif original_color == '#9b59b6':
                button.configure(bg='#8e44ad')
        
        def on_leave(e):
            button.configure(bg=original_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def update_status(self, message, color='#ecf0f1'):
        """Update status bar message"""
        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.config(text=message, fg=color)
            self.window.update()
        else:
            print(f"Status: {message}")  # Fallback to console output
    
    def validate_date(self, date_string):
        """Validate date format (YYYY-MM-DD)"""
        try:
            from datetime import datetime
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    def set_today_date(self):
        """Set today's date in the watch date field"""
        from datetime import date
        today = date.today()
        self.watch_date_entry.delete(0, 'end')
        self.watch_date_entry.insert(0, today.strftime('%Y-%m-%d'))
    
    def clear_form(self):
        """Clear all form fields"""
        self.watch_history_id_entry.delete(0, 'end')
        self.profile_combobox.set('')
        self.movie_id_entry.delete(0, 'end')
        self.watch_date_entry.delete(0, 'end')
        self.duration_entry.delete(0, 'end')
        self.selected_watch_history_id = None
        self.update_status("Form cleared")
    
    def load_profiles(self):
        """Load profile IDs and names for the dropdown"""
        try:
            self.update_status("Loading profiles...", '#f39c12')
            
            cursor = self.db.cursor
            cursor.execute("""
                SELECT p.profile_id, p.profile_name, c.customer_name 
                FROM Profiles p
                LEFT JOIN Customers c ON p.customer_id = c.customer_id
                ORDER BY p.profile_name
            """)
            profiles = cursor.fetchall()
            
            # Create list of profile options (ID - Profile Name (Customer Name) format)
            profile_options = []
            for profile in profiles:
                customer_name = profile[2] if profile[2] else "Unknown Customer"
                profile_options.append(f"{profile[0]} - {profile[1]} ({customer_name})")
            
            # Update combobox
            self.profile_combobox['values'] = profile_options
            self.profiles = profiles  # Store for reference
            
            self.update_status(f"Loaded {len(profiles)} profiles", '#27ae60')
            
        except Exception as e:
            error_msg = f"Error loading profiles: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def load_watch_history(self):
        """Load watch history from database"""
        try:
            self.update_status("Loading watch history...", '#f39c12')
            
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Execute query with JOIN to get profile name
            cursor = self.db.cursor
            cursor.execute("""
                SELECT wh.watch_history_id, wh.movie_id, wh.watch_date, wh.duration_watched,
                       p.profile_id, p.profile_name
                FROM Watch_History wh
                LEFT JOIN Profiles p ON wh.watch_history_id = p.watch_history_id
                ORDER BY wh.watch_history_id
            """)
            watch_records = cursor.fetchall()
            
            # Insert data into treeview
            for record in watch_records:
                values = (
                    record[0],  # watch_history_id
                    record[4] if record[4] is not None else "N/A",  # profile_id
                    record[5] if record[5] is not None else "No Profile",  # profile_name
                    record[1],  # movie_id
                    record[2],  # watch_date
                    f"{record[3]:.2f}" if record[3] is not None else "0.00"  # duration_watched
                )
                self.tree.insert('', 'end', values=values)
            
            self.update_status(f"Loaded {len(watch_records)} watch records", '#27ae60')
            
        except Exception as e:
            error_msg = f"Error loading watch history: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def on_item_select(self, event):
        """Handle item selection in treeview"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            # Populate form with selected watch history data
            self.clear_form()
            self.selected_watch_history_id = values[0]
            
            # Fill form fields
            self.watch_history_id_entry.insert(0, str(values[0]))
            
            # Set profile combobox
            profile_id = values[1]
            profile_name = values[2]
            if profile_id != "N/A" and profile_name != "No Profile":
                # Find matching profile in combobox
                for option in self.profile_combobox['values']:
                    if option.startswith(f"{profile_id} - {profile_name}"):
                        self.profile_combobox.set(option)
                        break
            
            self.movie_id_entry.insert(0, str(values[3]))
            self.watch_date_entry.insert(0, str(values[4]))
            self.duration_entry.insert(0, str(values[5]))
            
            self.update_status(f"Selected watch record ID: {values[0]}")
    
    def get_selected_profile_id(self):
        """Extract profile ID from combobox selection"""
        selection = self.profile_combobox.get()
        if selection:
            try:
                # Extract profile ID from "ID - Name (Customer)" format
                profile_id = int(selection.split(' - ')[0])
                return profile_id
            except (ValueError, IndexError):
                return None
        return None
    
    def insert_watch_history(self):
        """Insert new watch history record"""
        cursor = None
        try:
            # Get form data
            watch_history_id = self.watch_history_id_entry.get().strip()
            profile_id = self.get_selected_profile_id()
            movie_id = self.movie_id_entry.get().strip()
            watch_date = self.watch_date_entry.get().strip()
            duration_watched = self.duration_entry.get().strip()
            
            # Validate input
            if not movie_id:
                messagebox.showerror("Validation Error", "Movie ID is required!")
                return
            
            if not watch_date or not self.validate_date(watch_date):
                messagebox.showerror("Validation Error", "Please enter a valid watch date (YYYY-MM-DD)!")
                return
            
            if not duration_watched:
                messagebox.showerror("Validation Error", "Duration watched is required!")
                return
            
            # Convert and validate numeric inputs
            try:
                movie_id = int(movie_id)
                duration_watched = float(duration_watched)
                watch_history_id = int(watch_history_id) if watch_history_id else None
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter valid numeric values!")
                return
            
            if duration_watched < 0:
                messagebox.showerror("Validation Error", "Duration watched cannot be negative!")
                return
            
            self.update_status("Inserting watch record...", '#f39c12')
            
            # Get cursor
            cursor = self.db.cursor
            
            # Execute insert query
            if watch_history_id:
                insert_query = """
                    INSERT INTO Watch_History (watch_history_id, movie_id, watch_date, duration_watched) 
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (watch_history_id, movie_id, watch_date, duration_watched))
            else:
                insert_query = """
                    INSERT INTO Watch_History (movie_id, watch_date, duration_watched) 
                    VALUES (%s, %s, %s)
                """
                cursor.execute(insert_query, (movie_id, watch_date, duration_watched))
            
            self.db.connection.commit()
            
            # Update profile's watch_history_id if profile was selected
            if profile_id and watch_history_id:
                try:
                    update_profile_query = """
                        UPDATE Profiles SET watch_history_id = %s WHERE profile_id = %s
                    """
                    cursor.execute(update_profile_query, (watch_history_id, profile_id))
                    self.db.connection.commit()
                except Exception as e:
                    print(f"Note: Could not link profile to watch history: {e}")
            
            # Clear form and refresh table
            self.clear_form()
            self.load_watch_history()
            
            self.update_status(f"Watch record inserted successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Watch record has been added successfully!")
            
        except Exception as e:
            if self.db.connection:
                self.db.connection.rollback()
            error_msg = f"Error inserting watch record: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def update_watch_history(self):
        """Update selected watch history record"""
        cursor = None
        try:
            if not self.selected_watch_history_id:
                messagebox.showwarning("Selection Error", "Please select a watch record to update!")
                return
            
            # Get form data
            movie_id = self.movie_id_entry.get().strip()
            watch_date = self.watch_date_entry.get().strip()
            duration_watched = self.duration_entry.get().strip()
            
            # Validate input
            if not movie_id:
                messagebox.showerror("Validation Error", "Movie ID is required!")
                return
            
            if not watch_date or not self.validate_date(watch_date):
                messagebox.showerror("Validation Error", "Please enter a valid watch date (YYYY-MM-DD)!")
                return
            
            if not duration_watched:
                messagebox.showerror("Validation Error", "Duration watched is required!")
                return
            
            # Convert and validate numeric inputs
            try:
                movie_id = int(movie_id)
                duration_watched = float(duration_watched)
            except ValueError:
                messagebox.showerror("Validation Error", "Please enter valid numeric values!")
                return
            
            if duration_watched < 0:
                messagebox.showerror("Validation Error", "Duration watched cannot be negative!")
                return
            
            # Confirm update
            if not messagebox.askyesno("Confirm Update", f"Are you sure you want to update this watch record?"):
                return
            
            self.update_status("Updating watch record...", '#f39c12')
            
            # Get cursor
            cursor = self.db.cursor
            
            # Execute update query
            update_query = """
                UPDATE Watch_History 
                SET movie_id = %s, watch_date = %s, duration_watched = %s
                WHERE watch_history_id = %s
            """
            cursor.execute(update_query, (movie_id, watch_date, duration_watched, self.selected_watch_history_id))
            self.db.connection.commit()
            
            # Clear form and refresh table
            self.clear_form()
            self.load_watch_history()
            self.update_status(f"Watch record updated successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Watch record has been updated successfully!")
            
        except Exception as e:
            if self.db.connection:
                self.db.connection.rollback()
            error_msg = f"Error updating watch record: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def delete_watch_history(self):
        """Delete selected watch history record"""
        try:
            if not self.selected_watch_history_id:
                messagebox.showwarning("Selection Error", "Please select a watch record to delete!")
                return
            
            # Check if any profiles reference this watch history
            cursor = self.db.cursor
            check_query = """
                SELECT profile_id, profile_name 
                FROM Profiles 
                WHERE watch_history_id = %s
            """
            cursor.execute(check_query, (self.selected_watch_history_id,))
            referencing_profiles = cursor.fetchall()
            
            # If there are referencing profiles, ask user what to do
            if referencing_profiles:
                profile_names = ", ".join([f"{p[1]} (ID: {p[0]})" for p in referencing_profiles])
                
                message = f"This watch record is linked to the following profile(s):\n\n{profile_names}\n\n"
                message += "What would you like to do?\n\n"
                message += "• Click 'Yes' to unlink profiles and delete the watch record\n"
                message += "• Click 'No' to cancel deletion"
                
                result = messagebox.askyesno(
                    "Foreign Key Constraint", 
                    message,
                    icon='warning'
                )
                
                if not result:
                    self.update_status("Deletion cancelled", '#f39c12')
                    return
                
                # User chose to proceed - unlink profiles first
                self.update_status("Unlinking profiles...", '#f39c12')
                
                for profile_id, profile_name in referencing_profiles:
                    unlink_query = "UPDATE Profiles SET watch_history_id = NULL WHERE profile_id = %s"
                    cursor.execute(unlink_query, (profile_id,))
                
                self.db.connection.commit()
                self.update_status("Profiles unlinked, now deleting watch record...", '#f39c12')
            
            else:
                # No referencing profiles, just confirm normal deletion
                if not messagebox.askyesno("Confirm Delete", 
                                        f"Are you sure you want to delete this watch record?\n\nWatch History ID: {self.selected_watch_history_id}\n\nThis action cannot be undone!"):
                    return
            
            self.update_status("Deleting watch record...", '#f39c12')
            
            # Now safe to delete the watch history record
            delete_query = "DELETE FROM Watch_History WHERE watch_history_id = %s"
            cursor.execute(delete_query, (self.selected_watch_history_id,))
            self.db.connection.commit()
            
            # Clear form and refresh table
            self.clear_form()
            self.load_watch_history()
            
            self.update_status(f"Watch record deleted successfully!", '#27ae60')
            messagebox.showinfo("Success", f"Watch record has been deleted successfully!")
            
        except Exception as e:
            if self.db.connection:
                self.db.connection.rollback()
            error_msg = f"Error deleting watch record: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Database Error", error_msg)
    
    def on_closing(self):
        """Handle window closing event"""
        self.window.grab_release()  # Release the modal grab
        self.window.destroy()       # Close the window
    
    def run(self):
        """Start the watch history CRUD window"""
        pass  # Window is already created and shown

class ReportsWindow:
    """
    Reports window for query and procedure execution
    """
    
    def __init__(self, db_connection, parent_window):
        self.db = db_connection
        self.parent = parent_window
        self.window = tk.Toplevel(parent_window)
        self.status_label = None
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Configure the reports window"""
        self.window.title("Reports & Database Queries")
        self.window.geometry("1600x800")
        self.window.configure(bg='#2c3e50')
        
        # Center the window
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (1600 // 2)
        y = (self.window.winfo_screenheight() // 2) - (800 // 2)
        self.window.geometry(f"1600x800+{x}+{y}")
        
        # Make window modal
        self.window.transient(self.parent)
        self.window.grab_set()
        
        # Handle window close event
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_widgets(self):
        """Create the reports interface"""
        # Title
        title_label = tk.Label(
            self.window,
            text="📊 Reports & Database Queries",
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=15)
        
        # Main content frame
        main_frame = tk.Frame(self.window, bg='#2c3e50')
        main_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Left panel for report options and inputs
        left_frame = tk.Frame(main_frame, bg='#34495e', width=400)
        left_frame.pack(side='left', fill='y', padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # Right panel for results
        right_frame = tk.Frame(main_frame, bg='#34495e')
        right_frame.pack(side='right', expand=True, fill='both')
        
        # Create left panel content
        self.create_left_panel(left_frame)
        
        # Create right panel content
        self.create_right_panel(right_frame)
        
        # Status bar
        self.create_status_bar()
    
    def create_left_panel(self, parent):
        """Create the left panel with report options and inputs (with scrollbar)"""
        # Create a canvas and scrollbar for scrolling
        canvas = tk.Canvas(parent, bg='#34495e', highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#34495e')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "what")
        
        # Bind mouse wheel to canvas
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Now create all content in scrollable_frame instead of parent
        # Section title
        tk.Label(
            scrollable_frame,
            text="📋 Available Reports & Queries",
            font=('Arial', 14, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        ).pack(pady=(15, 20))
        
        # Reports frame
        reports_frame = tk.Frame(scrollable_frame, bg='#34495e')
        reports_frame.pack(fill='x', padx=20)
        
        # Query A: Top N most recent payments (SMALLER)
        query_a_frame = tk.LabelFrame(
            reports_frame,
            text="📈 Query A: Recent Payments",
            font=('Arial', 10, 'bold'),  # Smaller font
            bg='#34495e',
            fg='#ecf0f1',
            relief='ridge'
        )
        query_a_frame.pack(fill='x', pady=(0, 10))  # Less padding
        
        tk.Label(
            query_a_frame,
            text="Top N payments:",  # Shorter text
            font=('Arial', 9),  # Smaller font
            bg='#34495e',
            fg='#bdc3c7'
        ).pack(anchor='w', padx=8, pady=(3, 0))  # Less padding
        
        self.payments_limit_entry = tk.Entry(
            query_a_frame,
            font=('Arial', 9),  # Smaller font
            bg='#ecf0f1',
            fg='#2c3e50',
            width=8  # Smaller width
        )
        self.payments_limit_entry.pack(anchor='w', padx=8, pady=3)  # Less padding
        self.payments_limit_entry.insert(0, "40")
        
        query_a_btn = tk.Button(
            query_a_frame,
            text="🔍 Run Query A",
            command=self.run_query_a,
            font=('Arial', 9, 'bold'),  # Smaller font
            bg='#3498db',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        query_a_btn.pack(pady=5)  # Less padding
        self.add_hover_effect(query_a_btn)
        
        # Query B: Revenue by country (SMALLER)
        query_b_frame = tk.LabelFrame(
            reports_frame,
            text="🌍 Query B: Revenue by Country",
            font=('Arial', 10, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            relief='ridge'
        )
        query_b_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(
            query_b_frame,
            text="Average revenue per country",
            font=('Arial', 9),
            bg='#34495e',
            fg='#bdc3c7'
        ).pack(anchor='w', padx=8, pady=3)
        
        query_b_btn = tk.Button(
            query_b_frame,
            text="🔍 Run Query B",
            command=self.run_query_b,
            font=('Arial', 9, 'bold'),
            bg='#e67e22',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        query_b_btn.pack(pady=5)
        self.add_hover_effect(query_b_btn)
        
        # Procedure (SMALLER)
        proc_frame = tk.LabelFrame(
            reports_frame,
            text="⚙️ Procedure: Update Profile",
            font=('Arial', 10, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            relief='ridge'
        )
        proc_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(
            proc_frame,
            text="Profile ID:",
            font=('Arial', 9),
            bg='#34495e',
            fg='#bdc3c7'
        ).pack(anchor='w', padx=8, pady=(3, 0))
        
        self.profile_id_entry = tk.Entry(
            proc_frame,
            font=('Arial', 9),
            bg='#ecf0f1',
            fg='#2c3e50',
            width=8
        )
        self.profile_id_entry.pack(anchor='w', padx=8, pady=2)
        
        self.online_status_var = tk.BooleanVar()
        self.online_status_check = tk.Checkbutton(
            proc_frame,
            text="Set Online",  # Shorter text
            variable=self.online_status_var,
            font=('Arial', 9),
            bg='#34495e',
            fg='#bdc3c7',
            selectcolor='#2c3e50',
            activebackground='#34495e'
        )
        self.online_status_check.pack(anchor='w', padx=8, pady=2)
        
        proc_btn = tk.Button(
            proc_frame,
            text="⚙️ Run Procedure",
            command=self.run_procedure_1,
            font=('Arial', 9, 'bold'),
            bg='#27ae60',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        proc_btn.pack(pady=5)
        self.add_hover_effect(proc_btn)
        
        # Function (SMALLER)
        func_frame = tk.LabelFrame(
            reports_frame,
            text="🔧 Function: Customer Data",
            font=('Arial', 10, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            relief='ridge'
        )
        func_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(
            func_frame,
            text="Customer ID:",
            font=('Arial', 9),
            bg='#34495e',
            fg='#bdc3c7'
        ).pack(anchor='w', padx=8, pady=(3, 0))
        
        self.customer_id_entry = tk.Entry(
            func_frame,
            font=('Arial', 9),
            bg='#ecf0f1',
            fg='#2c3e50',
            width=8
        )
        self.customer_id_entry.pack(anchor='w', padx=8, pady=3)
        
        func_btn = tk.Button(
            func_frame,
            text="🔧 Run Function",
            command=self.run_function_1,
            font=('Arial', 9, 'bold'),
            bg='#9b59b6',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        func_btn.pack(pady=5)
        self.add_hover_effect(func_btn)
        
        # Revenue Chart (NEW SECTION)
        chart_frame = tk.LabelFrame(
            reports_frame,
            text="📊 Revenue Chart: Top 40 Months",
            font=('Arial', 10, 'bold'),
            bg='#34495e',
            fg='#ecf0f1',
            relief='ridge'
        )
        chart_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(
            chart_frame,
            text="Generate revenue chart",
            font=('Arial', 9),
            bg='#34495e',
            fg='#bdc3c7'
        ).pack(anchor='w', padx=8, pady=3)
        
        chart_btn = tk.Button(
            chart_frame,
            text="📊 Generate Chart",
            command=self.run_revenue_chart,
            font=('Arial', 9, 'bold'),
            bg='#e74c3c',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        chart_btn.pack(pady=5)
        self.add_hover_effect(chart_btn)
        
        # Clear results button
        clear_btn = tk.Button(
            reports_frame,
            text="🗑️ Clear Results",
            command=self.clear_results,
            font=('Arial', 9, 'bold'),
            bg='#95a5a6',
            fg='white',
            relief='flat',
            cursor='hand2'
        )
        clear_btn.pack(pady=15, fill='x')
        self.add_hover_effect(clear_btn)
        
        # Add some bottom padding
        tk.Label(scrollable_frame, text="", bg='#34495e').pack(pady=20)
    
    def create_right_panel(self, parent):
        """Create the right panel for results display"""
        # Results title
        results_title = tk.Label(
            parent,
            text="📈 Query Results",
            font=('Arial', 14, 'bold'),
            bg='#34495e',
            fg='#ecf0f1'
        )
        results_title.pack(pady=(15, 10))
        
        # Results frame
        results_frame = tk.Frame(parent, bg='#34495e')
        results_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Create Treeview for results (dynamic columns)
        self.results_tree = ttk.Treeview(results_frame, show='headings', height=20)
        
        # Scrollbars for results
        v_scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=self.results_tree.yview)
        h_scrollbar = ttk.Scrollbar(results_frame, orient='horizontal', command=self.results_tree.xview)
        self.results_tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack results treeview and scrollbars
        self.results_tree.pack(side='left', expand=True, fill='both')
        v_scrollbar.pack(side='right', fill='y')
        h_scrollbar.pack(side='bottom', fill='x')
        
        # Results info label
        self.results_info_label = tk.Label(
            parent,
            text="Select a query or procedure from the left panel to view results here.",
            font=('Arial', 10),
            bg='#34495e',
            fg='#bdc3c7',
            wraplength=600
        )
        self.results_info_label.pack(pady=10)
    
    def create_status_bar(self):
        """Create status bar"""
        status_frame = tk.Frame(self.window, bg='#34495e', height=30)
        status_frame.pack(side='bottom', fill='x')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready - Select a query to run",
            bg='#34495e',
            fg='#ecf0f1',
            font=('Arial', 9)
        )
        self.status_label.pack(side='left', padx=10, pady=5)
        
        # Close button
        close_btn = tk.Button(
            status_frame,
            text="❌ Close",
            command=self.on_closing,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 9),
            relief='flat',
            cursor='hand2'
        )
        close_btn.pack(side='right', padx=10, pady=3)
    
    def add_hover_effect(self, button):
        """Add hover effect to buttons"""
        original_color = button.cget('bg')
        
        def on_enter(e):
            if original_color == '#3498db':
                button.configure(bg='#2980b9')
            elif original_color == '#e67e22':
                button.configure(bg='#d35400')
            elif original_color == '#27ae60':
                button.configure(bg='#219a52')
            elif original_color == '#9b59b6':
                button.configure(bg='#8e44ad')
            elif original_color == '#95a5a6':
                button.configure(bg='#7f8c8d')
            elif original_color == '#e74c3c':  # New color for chart button
                button.configure(bg='#c0392b')
        
        def on_leave(e):
            button.configure(bg=original_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def run_revenue_chart(self):
        """Generate and display revenue chart for top 40 months"""
        try:
            import matplotlib.pyplot as plt
            import pandas as pd
            from datetime import datetime
            import calendar
            from decimal import Decimal
            
            self.update_status("Generating revenue chart...", '#f39c12')
            
            cursor = self.db.cursor
            
            # Your exact SQL query
            query = """
            WITH MonthlyPayments AS (
            SELECT 
                EXTRACT(YEAR FROM payment_date) AS year,
                EXTRACT(MONTH FROM payment_date) AS month,
                SUM(amount) AS total_monthly_amount
            FROM Payments
            GROUP BY year, month
            ),
            RankedPayments AS (
            SELECT 
                year,
                month,
                total_monthly_amount,
                RANK() OVER (ORDER BY total_monthly_amount DESC) AS sales_rank
            FROM MonthlyPayments
            )
            SELECT year, month, total_monthly_amount, sales_rank
            FROM RankedPayments
            ORDER BY total_monthly_amount DESC
            LIMIT 40;
            """
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            if not results:
                messagebox.showinfo("No Data", "No payment data found for chart generation.")
                self.update_status("No data available for chart", '#f39c12')
                return
            
            # Convert to pandas DataFrame and handle Decimal types
            df = pd.DataFrame(results, columns=['year', 'month', 'total_revenue', 'rank'])
            
            # Convert Decimal to float for all numeric columns
            df['year'] = df['year'].astype(int)
            df['month'] = df['month'].astype(int)
            df['rank'] = df['rank'].astype(int)
            
            # Convert Decimal to float for revenue column
            df['total_revenue'] = df['total_revenue'].apply(lambda x: float(x) if isinstance(x, Decimal) else float(x))
            
            # Create date labels
            df['date_label'] = df.apply(lambda row: f"{calendar.month_abbr[int(row['month'])]} {int(row['year'])}", axis=1)
            df['date_sort'] = df.apply(lambda row: datetime(int(row['year']), int(row['month']), 1), axis=1)
            
            # Sort by date for better visualization
            df_sorted = df.sort_values('date_sort')
            
            # Create the plot
            plt.style.use('default')
            fig, ax = plt.subplots(figsize=(16, 8))
            
            # Create bar chart
            bars = ax.bar(range(len(df_sorted)), df_sorted['total_revenue'], 
                        color='#3498db', alpha=0.7, edgecolor='#2c3e50', linewidth=1)
            
            # Customize the chart
            ax.set_title('Top 40 Revenue Months', fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel('Month/Year', fontsize=12, fontweight='bold')
            ax.set_ylabel('Total Revenue ($)', fontsize=12, fontweight='bold')
            
            # Set x-axis labels
            ax.set_xticks(range(len(df_sorted)))
            ax.set_xticklabels(df_sorted['date_label'], rotation=45, ha='right')
            
            # Add value labels on bars (now properly handling float values)
            max_revenue = df_sorted['total_revenue'].max()
            for i, (bar, value) in enumerate(zip(bars, df_sorted['total_revenue'])):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + max_revenue*0.01,
                    f'${value:,.0f}', ha='center', va='bottom', fontsize=8, rotation=90)
            
            # Format y-axis to show currency
            ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
            
            # Add grid
            ax.grid(True, alpha=0.3, axis='y')
            
            # Adjust layout
            plt.tight_layout()
            
            # Show the plot
            plt.show()
            
            # Also display the data in the results table (handle Decimal in display)
            display_data = []
            for _, row in df.iterrows():
                display_data.append([
                    int(row['year']), 
                    int(row['month']), 
                    row['date_label'],
                    f"${row['total_revenue']:,.2f}",  # Now using float value
                    int(row['rank'])
                ])
            
            columns = ['Year', 'Month', 'Month/Year', 'Total Revenue', 'Rank']
            self.display_results(display_data, columns, "Top 40 Revenue Months")
            
            self.update_status(f"Revenue chart generated successfully - {len(results)} months plotted", '#27ae60')
            
        except ImportError as ie:
            error_msg = "Missing required packages. Please install: pip install matplotlib pandas"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Missing Dependencies", error_msg)
        except Exception as e:
            error_msg = f"Error generating revenue chart: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Chart Error", error_msg)
            print(f"Full error details: {e}")  # For debugging
        
    def run_revenue_chart_plotly(self):
        """Alternative: Generate interactive revenue chart using Plotly"""
        try:
            import plotly.graph_objects as go
            import plotly.express as px
            import pandas as pd
            from datetime import datetime
            import calendar
            
            self.update_status("Generating interactive revenue chart...", '#f39c12')
            
            cursor = self.db.cursor
            
            # Your exact SQL query
            query = """
            WITH MonthlyPayments AS (
            SELECT 
                EXTRACT(YEAR FROM payment_date) AS year,
                EXTRACT(MONTH FROM payment_date) AS month,
                SUM(amount) AS total_monthly_amount
            FROM Payments
            GROUP BY year, month
            ),
            RankedPayments AS (
            SELECT 
                year,
                month,
                total_monthly_amount,
                RANK() OVER (ORDER BY total_monthly_amount DESC) AS sales_rank
            FROM MonthlyPayments
            )
            SELECT year, month, total_monthly_amount, sales_rank
            FROM RankedPayments
            ORDER BY total_monthly_amount DESC
            LIMIT 40;
            """
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            if not results:
                messagebox.showinfo("No Data", "No payment data found for chart generation.")
                return
            
            # Convert to pandas DataFrame
            df = pd.DataFrame(results, columns=['year', 'month', 'total_revenue', 'rank'])

            # Convert all values to proper Python types
            processed_data = []
            for _, row in df.iterrows():
                processed_data.append([
                    int(row['year']),
                    int(row['month']),
                    float(row['total_revenue']),  # Convert Decimal to float
                    int(row['rank'])
                ])

            # Recreate DataFrame with converted values
            df = pd.DataFrame(processed_data, columns=['year', 'month', 'total_revenue', 'rank'])

            df_sorted = df.sort_values('date_sort')
            
            # Create interactive bar chart
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                x=df_sorted['date_label'],
                y=df_sorted['total_revenue'],
                text=[f"${float(val):,.0f}" for val in df_sorted['total_revenue']],
                textposition='outside',
                marker_color='#3498db',
                marker_line_color='#2c3e50',
                marker_line_width=1,
                hovertemplate='<b>%{x}</b><br>Revenue: $%{y:,.2f}<br>Rank: %{customdata}<extra></extra>',
                customdata=df_sorted['rank']
            ))
            
            fig.update_layout(
                title={
                    'text': 'Top 40 Revenue Months',
                    'x': 0.5,
                    'xanchor': 'center',
                    'font': {'size': 18}
                },
                xaxis_title='Month/Year',
                yaxis_title='Total Revenue ($)',
                xaxis={'tickangle': 45},
                yaxis={'tickformat': '$,.0f'},
                showlegend=False,
                width=1200,
                height=600,
                margin=dict(l=50, r=50, t=80, b=100)
            )
            
            # Show the interactive plot
            fig.show()
            
            # Also display the data in the results table
            display_data = []
            for _, row in df.iterrows():
                display_data.append([
                    int(row['year']), 
                    int(row['month']), 
                    row['date_label'],
                    f"${float(row['total_revenue']):,.2f}",
                    int(row['rank'])
                ])
            
            columns = ['Year', 'Month', 'Month/Year', 'Total Revenue', 'Rank']
            self.display_results(display_data, columns, "Top 40 Revenue Months")
            
            self.update_status(f"Interactive revenue chart generated successfully - {len(results)} months plotted", '#27ae60')
            
        except ImportError as ie:
            error_msg = "Missing required packages. Please install: pip install plotly pandas"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Missing Dependencies", error_msg)
        except Exception as e:
            error_msg = f"Error generating interactive revenue chart: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Chart Error", error_msg)
    
    def update_status(self, message, color='#ecf0f1'):
        """Update status bar message"""
        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.config(text=message, fg=color)
            self.window.update()
        else:
            print(f"Status: {message}")
    
    def display_results(self, data, columns, title="Query Results"):
        """Display results in the treeview"""
        try:
            # Clear existing results
            for item in self.results_tree.get_children():
                self.results_tree.delete(item)
            
            if not data:
                self.results_info_label.config(text="No results found for the selected query.")
                return
            
            # Configure columns
            self.results_tree['columns'] = columns
            self.results_tree['show'] = 'headings'
            
            # Set column headings and widths
            for col in columns:
                self.results_tree.heading(col, text=col)
                self.results_tree.column(col, width=120, anchor='center')
            
            # Insert data
            for row in data:
                # Convert None values to empty strings
                formatted_row = [str(item) if item is not None else "" for item in row]
                self.results_tree.insert('', 'end', values=formatted_row)
            
            # Update info label
            self.results_info_label.config(text=f"{title} - {len(data)} rows returned")
            
        except Exception as e:
            self.update_status(f"Error displaying results: {str(e)}", '#e74c3c')
            messagebox.showerror("Display Error", f"Error displaying results: {str(e)}")
    
    def clear_results(self):
        """Clear the results display"""
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        self.results_info_label.config(text="Results cleared. Select a query to run.")
        self.update_status("Results cleared")
    
    def run_query_a(self):
        """Run Query A: Top N most recent payments"""
        try:
            # Get the limit from input
            limit_text = self.payments_limit_entry.get().strip()
            if not limit_text:
                messagebox.showerror("Input Error", "Please enter a number for the limit!")
                return
            
            try:
                limit = int(limit_text)
                if limit <= 0:
                    raise ValueError("Limit must be positive")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid positive number!")
                return
            
            self.update_status(f"Running Query A: Top {limit} total revenue per month ", '#f39c12')
            
            cursor = self.db.cursor
            query = """
                WITH DiscountedPayments AS (
            SELECT 
                p.payment_date,
                -- Join Payments to Customers, then to Discounts
                p.amount * (1 - COALESCE(d.discount_percent, 0) / 100.0) AS discounted_amount
            FROM Payments p
            JOIN Customers c ON p.customer_id = c.customer_id
            LEFT JOIN Discounts d ON c.discount_id = d.discount_id
            ),
            MonthlyPayments AS (
            SELECT 
                EXTRACT(YEAR FROM payment_date) AS year,
                EXTRACT(MONTH FROM payment_date) AS month,
                SUM(discounted_amount) AS total_monthly_amount
            FROM DiscountedPayments
            GROUP BY year, month
            ),
            RankedPayments AS (
            SELECT 
                year,
                month,
                total_monthly_amount,
                RANK() OVER (ORDER BY total_monthly_amount DESC) AS sales_rank
            FROM MonthlyPayments
            )
            SELECT *
            FROM RankedPayments
            ORDER BY total_monthly_amount DESC
            LIMIT %s;
            """
            cursor.execute(query, (limit,))
            results = cursor.fetchall()
            
            columns = ['Year', 'Month', 'Amount', 'Rank']
            
            self.display_results(results, columns, f"Top {limit} Most Recent Payments")
            self.update_status(f"Query A completed - {len(results)} payments found", '#27ae60')
            
        except Exception as e:
            error_msg = f"Error running Query A: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Query Error", error_msg)
    
    def run_query_b(self):
        """Run Query B: Average revenue per country"""
        try:
            self.update_status("Running Query B: Average revenue per country...", '#f39c12')
            
            cursor = self.db.cursor
            query = """
            SELECT 
            sp.country,
            AVG(sp.monthly_cost * (1 - COALESCE(d.discount_percent, 0) / 100.0)) AS avg_discounted_cost,
            COUNT(c.customer_id) AS subscription_count,
            -- Interpretation: average revenue per customer (not per payment)
            SUM(sp.monthly_cost * (1 - COALESCE(d.discount_percent, 0) / 100.0)) / COUNT(c.customer_id) AS subscription_count_revenue_ratio

            FROM Customers c
            JOIN Subscription_Plans sp ON c.plan_id = sp.plan_id
            LEFT JOIN Discounts d ON c.discount_id = d.discount_id

            GROUP BY sp.country
            ORDER BY subscription_count_revenue_ratio DESC;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            
            columns = ['Country', 'Average Discounted Cost', 'Total Subscriptions']
            
            self.display_results(results, columns, "Average discounted revenue by country")
            self.update_status(f"Query B completed - {len(results)} countries analyzed", '#27ae60')
            
        except Exception as e:
            error_msg = f"Error running Query B: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Query Error", error_msg)
    
    def run_procedure_1(self):
        """Run Procedure 1: Update profile online status"""
        try:
            # Get inputs
            profile_id_text = self.profile_id_entry.get().strip()
            if not profile_id_text:
                messagebox.showerror("Input Error", "Please enter a Profile ID!")
                return
            
            try:
                profile_id = int(profile_id_text)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid Profile ID!")
                return
            
            online_status = self.online_status_var.get()
            
            self.update_status(f"Running Procedure: Update profile {profile_id} status...", '#f39c12')
            
            cursor = self.db.cursor
            
            # Check if profile exists
            cursor.execute("SELECT profile_name FROM Profiles WHERE profile_id = %s", (profile_id,))
            profile = cursor.fetchone()
            
            if not profile:
                messagebox.showerror("Error", f"Profile with ID {profile_id} not found!")
                self.update_status("Profile not found", '#e74c3c')
                return
            
            # Update the profile status
            update_query = "UPDATE Profiles SET is_online = %s WHERE profile_id = %s"
            cursor.execute(update_query, (online_status, profile_id))
            self.db.connection.commit()
            
            # Show the updated profile
            cursor.execute("""
                SELECT profile_id, profile_name, is_online, customer_id, watch_history_id
                FROM Profiles 
                WHERE profile_id = %s
            """, (profile_id,))
            result = cursor.fetchall()
            
            columns = ['Profile ID', 'Profile Name', 'Online Status', 'Customer ID', 'Watch History ID']
            
            self.display_results(result, columns, f"Updated Profile Status")
            
            status_text = "Online" if online_status else "Offline"
            self.update_status(f"Profile {profile[0]} status updated to {status_text}", '#27ae60')
            messagebox.showinfo("Success", f"Profile '{profile[0]}' status updated to {status_text}!")
            
        except Exception as e:
            if self.db.connection:
                self.db.connection.rollback()
            error_msg = f"Error running procedure: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Procedure Error", error_msg)
    
    def run_function_1(self):
        """Run Function 1: Get all favorite movies for a customer"""
        try:
            # Get customer ID input
            customer_id_text = self.customer_id_entry.get().strip()
            if not customer_id_text:
                messagebox.showerror("Input Error", "Please enter a Customer ID!")
                return

            try:
                customer_id = int(customer_id_text)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid Customer ID!")
                return

            self.update_status(f"Running Function: Get favorites for customer {customer_id}...", '#f39c12')

            cursor = self.db.cursor

            # Check if customer exists
            cursor.execute("SELECT customer_name FROM Customers WHERE customer_id = %s", (customer_id,))
            customer = cursor.fetchone()

            if not customer:
                messagebox.showerror("Error", f"Customer with ID {customer_id} not found!")
                self.update_status("Customer not found", '#e74c3c')
                return

            # Check if customer has profiles
            cursor.execute("SELECT COUNT(*) FROM Profiles WHERE customer_id = %s", (customer_id,))
            profile_count = cursor.fetchone()[0]

            if profile_count == 0:
                messagebox.showerror("Error", f"Customer {customer_id} has no profiles!")
                self.update_status("Customer has no profiles", '#e74c3c')
                return

            # Your exact query with parameter substitution
            query = """
            SELECT 
                c.customer_name::VARCHAR,
                COUNT(DISTINCT p.profile_id)::INTEGER,
                COALESCE(SUM(wh.duration_watched), 0)::INTEGER,
                COUNT(DISTINCT f.movie_id)::INTEGER,
                COALESCE(AVG(r.rating), 0)::DECIMAL(4,2),
                COALESCE((SELECT py.amount FROM payments py 
                WHERE py.customer_id = %s 
                ORDER BY py.payment_date DESC LIMIT 1), 0)::DECIMAL(10,2)
            FROM customers c
            LEFT JOIN profiles p ON c.customer_id = p.customer_id
            LEFT JOIN watch_history wh ON p.watch_history_id = wh.watch_history_id
            LEFT JOIN favorites f ON p.profile_id = f.profile_id
            LEFT JOIN reviews r ON p.profile_id = r.profile_id
            WHERE c.customer_id = %s
            GROUP BY c.customer_id, c.customer_name;
            """

            cursor.execute(query, (customer_id, customer_id))
            results = cursor.fetchall()

            columns = ['Customer Name', 'Total Profiles', 'Total Watch Time', 'Favorite Movies Count', 'Average Rating', 'Last Payment Amount']
            self.display_results(results, columns, f"Customer Summary for: {customer[0]}")

            if results:
                self.update_status(f"Function completed - Customer summary retrieved successfully", '#27ae60')
            else:
                self.update_status(f"Function completed - No data found for customer {customer[0]}", '#f39c12')

        except Exception as e:
            error_msg = f"Error running function: {str(e)}"
            self.update_status(error_msg, '#e74c3c')
            messagebox.showerror("Function Error", error_msg)


    
    def on_closing(self):
        """Handle window closing event"""
        self.window.grab_release()  # Release the modal grab
        self.window.destroy()       # Close the window
    
    def run(self):
        """Start the reports window"""
        pass  # Window is already created and shown

    def on_closing(self):
        """Handle window closing event"""
        self.window.grab_release()  # Release the modal grab
        self.window.destroy()       # Close the window

    def run(self):
        """Start the reports window"""
        pass  # Window is already created and shown
        

# ... (keeping your existing LoginWindow and main function as they are) ...

def main():
    """
    Main function to start the application
    """
    print("🚀 Starting Streaming Service Management System")
    print("=" * 50)
    
    # Create and run login window
    login_app = LoginWindow()
    login_app.run()
    
    print("👋 Application closed. Goodbye!")


if __name__ == "__main__":
    main()
