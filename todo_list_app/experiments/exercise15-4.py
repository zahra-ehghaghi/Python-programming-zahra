import webbrowser
search_str = input("Enter Search String ").replace(" ","+")
webbrowser.open_new_tab(f"http://www.google.com?q={search_str}")