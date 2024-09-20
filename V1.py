import tkinter as tk
from tkinter import ttk, filedialog
import webbrowser
from datetime import datetime
import csv

class PersonSearchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Find It!")
        self.geometry("800x800")

        self.platforms = [
            "Google", "Facebook", "LinkedIn", "Twitter", "Instagram", 
            "GitHub", "TikTok", "YouTube", "Reddit", "Twitch", 
            "VSCO", "Tinder", "Pinterest", "BeReal", "Tumblr"
        ]
        self.search_results = []

        self.create_widgets()

    def create_widgets(self):
        # Input fields
        ttk.Label(self, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.first_name = ttk.Entry(self)
        self.first_name.grid(row=0, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        ttk.Label(self, text="Last Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.last_name = ttk.Entry(self)
        self.last_name.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        ttk.Label(self, text="Phone Number:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.phone = ttk.Entry(self)
        self.phone.grid(row=2, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        ttk.Label(self, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.email = ttk.Entry(self)
        self.email.grid(row=3, column=1, columnspan=5, padx=5, pady=5, sticky="ew")

        # Date range
        ttk.Label(self, text="Date Range:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.start_date = ttk.Entry(self, width=12)
        self.start_date.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(self, text="to").grid(row=4, column=2)
        self.end_date = ttk.Entry(self, width=12)
        self.end_date.grid(row=4, column=3, padx=5, pady=5, sticky="w")

        # Platform selection
        ttk.Label(self, text="Platforms:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.platform_vars = []
        self.direct_search_vars = []
        for i, platform in enumerate(self.platforms):
            var = tk.BooleanVar(value=True)
            self.platform_vars.append(var)
            direct_var = tk.BooleanVar(value=False)
            self.direct_search_vars.append(direct_var)
            ttk.Checkbutton(self, text=platform, variable=var).grid(row=5+i//3, column=i%3*2, padx=5, pady=2, sticky="w")
            ttk.Checkbutton(self, text="Direct", variable=direct_var).grid(row=5+i//3, column=i%3*2+1, padx=5, pady=2, sticky="w")

        # Search button
        self.search_button = ttk.Button(self, text="Search", command=self.perform_search)
        self.search_button.grid(row=11, column=0, columnspan=6, pady=10)

        # Export button
        self.export_button = ttk.Button(self, text="Export Results", command=self.export_results)
        self.export_button.grid(row=12, column=0, columnspan=6, pady=10)

        # Results area
        self.results_text = tk.Text(self, height=20, width=90)
        self.results_text.grid(row=13, column=0, columnspan=6, padx=5, pady=5)

    def perform_search(self):
        self.results_text.delete(1.0, tk.END)
        self.search_results = []

        first_name = self.first_name.get()
        last_name = self.last_name.get()
        phone = self.phone.get()
        email = self.email.get()
        start_date = self.start_date.get()
        end_date = self.end_date.get()

        date_query = self.construct_date_query(start_date, end_date)

        for i, platform in enumerate(self.platforms):
            if self.platform_vars[i].get():
                result = self.search_platform(platform, first_name, last_name, phone, email, date_query, self.direct_search_vars[i].get())
                self.search_results.append(result)
                self.results_text.insert(tk.END, f"Searched {platform}: {result['url']}\n")

    def construct_date_query(self, start_date, end_date):
        if not start_date and not end_date:
            return ""
        
        query = " after:"
        if start_date:
            query += start_date
        else:
            query += "2000-01-01"
        
        query += " before:"
        if end_date:
            query += end_date
        else:
            query += datetime.now().strftime("%Y-%m-%d")
        
        return query

    def search_platform(self, platform, first_name, last_name, phone, email, date_query, direct_search):
        query = f"{first_name} {last_name} {phone} {email}"
        
        if direct_search:
            url = self.get_direct_search_url(platform, query)
        else:
            base_url = "https://www.google.com/search?q="
            if platform != "Google":
                if platform == "VSCO":
                    query += f" site:vsco.co"
                elif platform == "BeReal":
                    query += f" site:bere.al"
                else:
                    query += f" site:{platform.lower()}.com"
            query += date_query
            url = base_url + query.replace(" ", "+")
        
        webbrowser.open_new_tab(url)
        return {"platform": platform, "url": url}

    def get_direct_search_url(self, platform, query):
        query = query.replace(" ", "+")
        if platform == "Google":
            return f"https://www.google.com/search?q={query}"
        elif platform == "Facebook":
            return f"https://www.facebook.com/search/top/?q={query}"
        elif platform == "LinkedIn":
            return f"https://www.linkedin.com/search/results/all/?keywords={query}"
        elif platform == "Twitter":
            return f"https://twitter.com/search?q={query}"
        elif platform == "Instagram":
            return f"https://www.instagram.com/explore/tags/{query}/"
        elif platform == "GitHub":
            return f"https://github.com/search?q={query}"
        elif platform == "TikTok":
            return f"https://www.tiktok.com/search?q={query}"
        elif platform == "YouTube":
            return f"https://www.youtube.com/results?search_query={query}"
        elif platform == "Reddit":
            return f"https://www.reddit.com/search/?q={query}"
        elif platform == "Twitch":
            return f"https://www.twitch.tv/search?term={query}"
        elif platform == "VSCO":
            return f"https://vsco.co/search/{query}"
        elif platform == "Tinder":
            return "https://tinder.com/"  # Tinder doesn't have a public search URL
        elif platform == "Pinterest":
            return f"https://www.pinterest.com/search/pins/?q={query}"
        elif platform == "BeReal":
            return "https://bere.al/en"  # BeReal doesn't have a public search URL
        elif platform == "Tumblr":
            return f"https://www.tumblr.com/search/{query}"
        else:
            return f"https://www.google.com/search?q={query}+site:{platform.lower()}.com"

    def export_results(self):
        if not self.search_results:
            self.results_text.insert(tk.END, "No results to export.\n")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])
        if not file_path:
            return

        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["platform", "url"])
            writer.writeheader()
            writer.writerows(self.search_results)

        self.results_text.insert(tk.END, f"Results exported to {file_path}\n")

if __name__ == "__main__":
    app = PersonSearchApp()
    app.mainloop() 