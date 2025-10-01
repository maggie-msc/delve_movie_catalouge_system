import os
import re
import tkinter as tk
from time import time
from tkinter import *


from PIL import Image, ImageTk
        

class gui:

    def __init__(self, indexed_lists, images):
        self.root = tk.Tk()
        self.root.title("Delve")
        self.root.geometry("1500x900")
        self.canvas= tk.Canvas(self.root, width= 1500, height= 900)

        self.indexed_lists = indexed_lists
        self.images = images
        self.list = []
        self.results_with_indexes = []
        self.alist = []
        self.num_of_searches = 0
        self.isFilterOn = False
        self.save_entry = ""

        self.moviel_label = tk.Label(self.root)
        self.entry1 = tk.Entry(self.root, bd=1, width=20)
        self.search = tk.Button(self.root, text="search", command=lambda:[self.find_movies(self.entry1.get())], width=9)
        self.ascending = None
        self.button1 = tk.Button(self.root, text="Sort", command=self.find_movies_desc)
        self.emptyspace = tk.Label(self.root, text="           ")

        self.genrelist = ["Adventure", "Nature", "Superhero", "Comedy", "Clear Filter"]
        self.click = tk.StringVar(self.root)
        self.click.set("Filter Results")
        self.genre_filter = tk.OptionMenu(self.root, self.click, *self.genrelist)


        self.entry1.grid(column=0, row=0, columnspan=2, sticky="n")
        self.search.grid(column=2, row=0, columnspan=2, sticky="n")
        self.button1.grid(column=4, row=0, columnspan=2, sticky="n")
        self.emptyspace.grid(column=6, row=0, columnspan=2, sticky="n")
        self.genre_filter.grid(column=8, row=0, columnspan=2, sticky="n")

    
        
        self.root.mainloop()

    def filter(self):
        apply = tk.Button(self.root, text="Apply Filter", command=self.select_an_option)
        apply.grid(row=0, column=10, rowspan=1, sticky='n')

    # FILTER OPTIONS FOR DIFFERENT GENRES
    def select_an_option(self):
        if self.click.get() == "Comedy":
            self.comedy()
        elif self.click.get() == "Adventure":
            self.adventure()
        elif self.click.get() == "Nature":
            self.nature()
        elif self.click.get() == "Superhero":
            self.superhero()
        else:
            self.find_movies_asc()

    def recreate_layout(self):
        self.moviel_label = tk.Label(self.root)
        self.entry1 = tk.Entry(self.root, bd=1, width=16)
        self.search = tk.Button(self.root, text="search", command=lambda:[self.find_movies(self.entry1.get())], width=9)
        self.ascending = None
        self.button1 = tk.Button(self.root, text="Sort", command=self.find_movies_desc)
        self.emptyspace = tk.Label(self.root, text="           ")

        self.genrelist = ["Adventure", "Nature", "Superhero", "Comedy", "Clear Filter"]
        self.click = tk.StringVar(self.root)
        self.click.set("Filter Results")
        self.genre_filter = tk.OptionMenu(self.root, self.click, *self.genrelist)


        self.entry1.grid(column=0, row=0, columnspan=2, sticky="n")
        self.search.grid(column=2, row=0, columnspan=2, sticky="n")
        self.button1.grid(column=4, row=0, columnspan=2, sticky="n")
        self.emptyspace.grid(column=6, row=0, columnspan=2, sticky="n")
        self.genre_filter.grid(column=8, row=0, columnspan=2, sticky="n")

        
        


    # FILTER SEARCH RESULTS FOR: ADVENTURE
    def adventure(self):

        self.ascending = True
        
        self.find_movies(self.entry1.get())
        self.clear_rows()
        self.recreate_layout()
        self.filter()
        self.entry1.insert(0, self.save_entry)
        self.button1['text'] = "Sort Descending"
        self.button1['command'] = self.find_movies_desc
        
        adventure_list = []
        for each_list in self.results_with_indexes:
            output = binary_search(each_list, 0, len(each_list)-1, "adventure")
            if type(output) is str:
                adventure_list.append(output)
            else:
                continue

        count = 0
        times_tables = []
        for element in range(len(adventure_list)):
            if element % 3 == 0:
                count += 1
                times_tables.append(element)
        
        
        # SORT RESULTS
        start = time.time()
        bubble_sort_filter_list(adventure_list)
        end = time.time()
        print(f"Bubble Sort performance: {(end-start)}")

        # ARRANGING RESULTS IN GRID FORMAT
        second_count = 0
        for i in range(6, 6+count):
            for j in range(6):
                if j == 0:
                    result = adventure_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)

                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j, columnspan=1)
                if j == 1:
                    result = adventure_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+1, columnspan=1)
                if j == 2:
                    result = adventure_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+2, columnspan=1)
                if j == 3:
                    result = adventure_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+3, columnspan=1)
                if j == 4:
                    result = adventure_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+4, columnspan=1)
                if j == 5:
                    result = adventure_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+5, columnspan=1)
                if second_count == (len(adventure_list)-1):
                    break
                second_count += 1

    # FILTER SEARCH RESULTS FOR: NATURE
    def nature(self):

        
        self.ascending = True
        self.find_movies(self.entry1.get())
        self.clear_rows()
        self.recreate_layout()
        self.filter()
        self.entry1.insert(0, self.save_entry)
        self.button1['text'] = "Sort Descending"
        self.button1['command'] = self.find_movies_desc

        nature_list = []
        for each_list in self.results_with_indexes:
            output = binary_search(each_list, 0, len(each_list)-1, "nature")
            if type(output) is str:
                nature_list.append(output)
            else:
                continue

        count = 0
        times_tables = []
        for element in range(len(nature_list)):
            if element % 3 == 0:
                count += 1
                times_tables.append(element)
        
        
        # SORT RESULTS
        bubble_sort_filter_list(nature_list)

        # ARRANGING RESULTS IN GRID FORMAT
        second_count = 0
        for i in range(6, 6+count):
            for j in range(6):
                if j == 0:
                    result = nature_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)

                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j, columnspan=1)
                if j == 1:
                    result = nature_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+1, columnspan=1)
                if j == 2:
                    result = nature_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+2, columnspan=1)
                if j == 3:
                    result = nature_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+3, columnspan=1)
                if j == 4:
                    result = nature_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+4, columnspan=1)
                if j == 5:
                    result = nature_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+5, columnspan=1)
                if second_count == (len(nature_list)-1):
                    break
                second_count += 1


    # FILTER SEARCH RESULTS FOR: SUPERHERO
    def superhero(self):
        self.ascending = True
        self.find_movies(self.entry1.get())
        self.clear_rows()
        self.recreate_layout()
        self.filter()
        self.entry1.insert(0, self.save_entry)
        self.button1['text'] = "Sort Descending"
        self.button1['command'] = self.find_movies_desc

        superhero_list = []
        for each_list in self.results_with_indexes:
            output = binary_search(each_list, 0, len(each_list)-1, "superhero")
            if type(output) is str:
                superhero_list.append(output)
            else:
                continue

        count = 0
        times_tables = []
        for element in range(len(superhero_list)):
            if element % 3 == 0:
                count += 1
                times_tables.append(element)
        
        
        # SORT RESULTS
        bubble_sort_filter_list(superhero_list)

        # ARRANGING RESULTS IN GRID FORMAT
        second_count = 0
        for i in range(6, 6+count):
            for j in range(6):
                if j == 0:
                    result = superhero_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)

                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j, columnspan=1)
                if j == 1:
                    result = superhero_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+1, columnspan=1)
                if j == 2:
                    result = superhero_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+2, columnspan=1)
                if j == 3:
                    result = superhero_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+3, columnspan=1)
                if j == 4:
                    result = superhero_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+4, columnspan=1)
                if j == 5:
                    result = superhero_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+5, columnspan=1)
                if second_count == (len(superhero_list)-1):
                    break
                second_count += 1



    # FILTER SEARCH RESULTS FOR: COMEDY
    def comedy(self):

        self.ascending = True
        self.find_movies(self.entry1.get())
        self.clear_rows()
        self.recreate_layout()
        self.filter()
        self.entry1.insert(0, self.save_entry)
        self.button1['text'] = "Sort Descending"
        self.button1['command'] = self.find_movies_desc

        comedy_list = []
        for each_list in self.results_with_indexes:
            output = binary_search(each_list, 0, len(each_list)-1, "comedy")
            if type(output) is str:
                comedy_list.append(output)
            else:
                continue

        count = 0
        times_tables = []
        for element in range(len(comedy_list)):
            if element % 3 == 0:
                count += 1
                times_tables.append(element)
        
        
        # SORT RESULTS
        bubble_sort_filter_list(comedy_list)

        # ARRANGING RESULTS IN GRID FORMAT
        second_count = 0
        for i in range(6, 6+count):
            for j in range(6):
                if j == 0:
                    result = comedy_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)

                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j, columnspan=1)
                if j == 1:
                    result = comedy_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+1, columnspan=1)
                if j == 2:
                    result = comedy_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+2, columnspan=1)
                if j == 3:
                    result = comedy_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+3, columnspan=1)
                if j == 4:
                    result = comedy_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+4, columnspan=1)
                if j == 5:
                    result = comedy_list[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+5, columnspan=1)
                if second_count == (len(comedy_list)-1):
                    break
                second_count += 1


    # CLEARING GRID ELEMENTS
    def clear_rows(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        

    # SORT SEARCH RESULTS IN ASCENDING ORDER
    def find_movies_asc(self):
        self.ascending = True
        self.button1['text'] = "Sort Descending"
        self.button1['command'] = self.find_movies_desc
        self.results_with_indexes = []
        count = 0
        times_tables = []
        for element in range(len(self.alist)):
            if element % 3 == 0:
                count += 1
                times_tables.append(element)
        
        
        # SORT RESULTS
        selection_sort_asc(self.alist)

        # ARRANGING RESULTS IN GRID FORMAT
        # 'second_count' tracks the indexes of the search result movie list 'alist'
        second_count = 0
        for i in range(6, 6+count):
            for j in range(6):
                if j == 0:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)

                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j, columnspan=1)
                if j == 1:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+1, columnspan=1)
                if j == 2:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+2, columnspan=1)
                if j == 3:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+3, columnspan=1)
                if j == 4:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+4, columnspan=1)
                if j == 5:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+5, columnspan=1)
                if second_count == (len(self.alist)-1):
                    break
                second_count += 1


    # SORT SEARCH RESULTS IN DESCENDING ORDER
    def find_movies_desc(self):
        self.ascending = False
        self.button1['text'] = "Sort Ascending"
        self.button1['command'] = self.find_movies_asc

        self.results_with_indexes = []
        count = 0
        times_tables = []
        for element in range(len(self.alist)):
            if element % 3 == 0:
                count += 1
                times_tables.append(element)
        
        
        # SORT RESULTS
        start = time.time()
        selection_sort_desc(self.alist)
        end = time.time()
        print(f"Selection sort performance: {(end-start)}")

        # ARRANGING RESULTS IN GRID FORMAT
        # 'second_count' tracks the indexes of the search result movie list 'alist'
        second_count = 0
        for i in range(6, 6+count):
            for j in range(6):
                if j == 0:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)

                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j, columnspan=1)
                if j == 1:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+1, columnspan=1)
                if j == 2:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+2, columnspan=1)
                if j == 3:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+3, columnspan=1)
                if j == 4:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+4, columnspan=1)
                if j == 5:
                    result = self.alist[second_count]
                    for element in self.images:
                        if result == element[:-4]:
                            self.moviel_label.forget()
                            self.moviel_label = tk.Label(self.root)
                            path = "images/"+str(element)
                            image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                            self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                            self.moviel_label.photo = image1
                            self.moviel_label['compound'] = tk.TOP
                            self.moviel_label.grid(row=i, column=j+5, columnspan=1)
                if second_count == (len(self.alist)-1):
                    break
                second_count += 1

    def start_again(self):
        self.root.destroy()
        gui(all_indexed_keywords, movie_imgs)

    def clear_for_filter(self):
        self.clear_rows()
        self.recreate_layout()
        

        
    
        
    # GET RESULTS FROM SEARCH BAR AND DISPLAY ASSOCIATED MOVIES WITH KEYWORD (USER INPUT)
    def find_movies(self, input):

        self.save_entry = input
        self.clear_for_filter()
        
        self.filter()
        self.ascending = True
        self.button1['text'] = "Sort Descending"
        self.button1['command'] = self.find_movies_desc

        self.entry1.insert(0, self.save_entry)


        self.alist = []
        self.results_with_indexes = []

        #IF THERES IS NO INPUT WHEN USER CLICKS SEARCH BUTTON
        if len(input) == 0:
            self.start_again()
        else:
        #IF THERE IS AN INPUT LONGER THAN 1 CHARACTER, START TO FIND MOVIES
            #BINARY SEARCH - FOR EVERY INDEXED LIST IN THE NESTED LIST, FIND THE INPUT VALUE AND APPEND MOVIES FOUND TO 'ALIST'
            for each_list in self.indexed_lists:
                start = time.time()
                output = binary_search(each_list, 0, len(each_list)-1, input)
                end = time.time()
                #print(f"Binary search performance time: {(end-start)}")
                if type(output) is str:
                    self.results_with_indexes.append(each_list)
                    self.alist.append(output)
                else:
                    continue

            # FIND THE NUMBER OF ROWS BASED ON THE LENGTH OF THE LIST AND BUILD GRID FORMAT
            count = 0
            times_tables = []
            for element in range(len(self.alist)):
                if element % 6 == 0:
                    count += 1
                    times_tables.append(element)
            
            
            # SORT RESULTS
            start = time.time()
            quick_sort(self.alist)
            end = time.time()
            print(f"Quick sort performance: {(end-start)}")

            # ARRANGING RESULTS IN GRID FORMAT
            # 'second_count' tracks the indexes of the search result movie list 'alist'
            second_count = 0
            for i in range(6, 6+count):
                for j in range(6):
                    if j == 0:
                        result = self.alist[second_count]
                        for element in self.images:
                            if result == element[:-4]:
                                self.moviel_label.forget()
                                self.moviel_label = tk.Label(self.root)

                                path = "images/"+str(element)
                                image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                                self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                                self.moviel_label.photo = image1
                                self.moviel_label['compound'] = tk.TOP
                                self.moviel_label.grid(row=i, column=j, columnspan=1)
                    if j == 1:
                        result = self.alist[second_count]
                        for element in self.images:
                            if result == element[:-4]:
                                self.moviel_label.forget()
                                self.moviel_label = tk.Label(self.root)
                                path = "images/"+str(element)
                                image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                                self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                                self.moviel_label.photo = image1
                                self.moviel_label['compound'] = tk.TOP
                                self.moviel_label.grid(row=i, column=j+1, columnspan=1)
                    if j == 2:
                        result = self.alist[second_count]
                        for element in self.images:
                            if result == element[:-4]:
                                self.moviel_label.forget()
                                self.moviel_label = tk.Label(self.root)
                                path = "images/"+str(element)
                                image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                                self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                                self.moviel_label.photo = image1
                                self.moviel_label['compound'] = tk.TOP
                                self.moviel_label.grid(row=i, column=j+2, columnspan=1)
                    if j == 3:
                        result = self.alist[second_count]
                        for element in self.images:
                            if result == element[:-4]:
                                self.moviel_label.forget()
                                self.moviel_label = tk.Label(self.root)
                                path = "images/"+str(element)
                                image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                                self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                                self.moviel_label.photo = image1
                                self.moviel_label['compound'] = tk.TOP
                                self.moviel_label.grid(row=i, column=j+3, columnspan=1)
                    if j == 4:
                        result = self.alist[second_count]
                        for element in self.images:
                            if result == element[:-4]:
                                self.moviel_label.forget()
                                self.moviel_label = tk.Label(self.root)
                                path = "images/"+str(element)
                                image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                                self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                                self.moviel_label.photo = image1
                                self.moviel_label['compound'] = tk.TOP
                                self.moviel_label.grid(row=i, column=j+4, columnspan=1)
                    if j == 5:
                        result = self.alist[second_count]
                        for element in self.images:
                            if result == element[:-4]:
                                self.moviel_label.forget()
                                self.moviel_label = tk.Label(self.root)
                                path = "images/"+str(element)
                                image1 = ImageTk.PhotoImage(Image.open(path).resize((100, 200)))
                                self.moviel_label = tk.Label(self.root, text=result, image=image1, pady=20, padx=26)
                                self.moviel_label.photo = image1
                                self.moviel_label['compound'] = tk.TOP
                                self.moviel_label.grid(row=i, column=j+5, columnspan=1)
                    if second_count == (len(self.alist)-1):
                        break
                    second_count += 1
                

                
# EXTRACTING KEYWORDS FROM MOVIE FILES
def extract(movie_file):
    directory_ = os.path.basename("movies")
    f = open(directory_+"/"+movie_file, "r")
    movie = f.read()
    all_categories = re.findall(r'(?<=wgCategories":\[)[\w\W]*?(?=])', movie)
    new_categories = all_categories[0].replace('"', '').split(',')
    return new_categories

# INDEXING KEYWORDS EXTRACTED WITH MOVIE FILE NAMES
def index(index_keywords, movie_file):
    keywords = extract(movie_file)
    for i in keywords:
        index_keywords.append((i, movie_file))

    return index_keywords



# BUBBLE SORT - FOR SORTING FILTERED SEARCH RESULTS
def bubble_sort_filter_list(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-1):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    
    return alist

# BINARY SEARCH - FOR SEARCHING KEYWORDS IN INDEXED MOVIE LISTS BASED ON USER INPUT IN THE SEARCH BAR
def binary_search(alist, low, high, target):
    if high >= low:
        mid = (high+low)//2
        if (target.lower() in alist[mid][0]) or (target.capitalize() in alist[mid][0]):
            return alist[mid][1]
        elif (target.lower() < alist[mid][0]) or (target.capitalize() < alist[mid][0]):
            return binary_search(alist, 0, mid-1, target)
        else:
            return binary_search(alist, mid+1, high, target)
    else:
        return None

# QUICK SORT ASCENDING - FOR SORTING SEARCH RESULTS
def partition(list1, low, high):
    pivot = list1[high]
    index = low
    for i in range(low, high):
        if list1[i] <= pivot:
            temp = list1[index]
            list1[index] = list1[i]
            list1[i] = temp
            index +=1

    swap = list1[high]
    list1[high] = list1[index]
    list1[index] = swap

    return index


def qsort(l, low, high):
    if low < high:
        pivot = partition(l, low, high)

        qsort(l, low, pivot-1)
        qsort(l, pivot+1, high)


def quick_sort(alist):
    qsort(alist, 0, len(alist)-1)


# INSERTION SORT - FOR SORTING INDEXED WORDS WITH MOVIES
def insertion_sort(alist):
    for i in range(len(alist)):
        j = i
        while(j > 0 and alist[j-1][0] > alist[j][0]):
            temp = alist[j]
            alist[j] = alist[j-1]
            alist[j-1] = temp
            j-=1

    return alist

# SELECTION SORT ASCENDING - FOR SORTING BUTTON
def getMinIndex_asc(alist, start, end):
    min_index = start # at index 0
    for i in range(start+1, end): #start at index 1
        if alist[i] < alist[min_index]:
            min_index = i
    return min_index
    

def swap_asc(alist, i, j):
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp


def selection_sort_asc(alist):
    n = len(alist)
    for index in range(n):
        min_position = getMinIndex_asc(alist, index, n)

        swap_asc(alist, index, min_position)

# SELECTION SORT DESCENDING - FOR SORTING BUTTON
def getMinIndex_desc(alist, start, end):
    min_index = start # at index 0
    for i in range(start+1, end): #start at index 1
        if alist[i] > alist[min_index]:
            min_index = i
    return min_index
    

def swap_desc(alist, i, j):
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp


def selection_sort_desc(alist):
    n = len(alist)
    for index in range(n):
        min_position = getMinIndex_desc(alist, index, n)

        swap_desc(alist, index, min_position)


# RETRIEVEING ALL MOVIE FILES FROM DIRECTORY 'movies'
all_files = "movies"
movie_list = []
for afile in os.listdir(all_files):
    if afile == ".DS_Store":
        continue
    movie_list.append(afile)

# RETRIEVEING ALL IMAGE FILES FROM DIRECTORY 'images'
all_images = "images"
movie_imgs = []
for img in os.listdir(all_images):
    if img == ".DS_Store":
        continue
    movie_imgs.append(img)


all_indexed_keywords = []

import time

# EXTRACTING AND INDEXING MOVIE FILES
for each_file in movie_list:
    keywords = []
    index_keywords = []
    keywords.append(extract(each_file))
    index(index_keywords, each_file)
    start = time.time()
    all_indexed_keywords.append(insertion_sort(index_keywords))
    end = time.time()

print(f"Insertion sort performance time: {(end-start)}")

# VARIBALE FOR TESTING PERFORMANCE
indexed_keywords_6 = []
indexed_keywords_12 = []

# APPENDING 6 MOVIE FILES
for i in range(0, 6):
    indexed_keywords_6.append(all_indexed_keywords[i])

# APPEDNING 12 MOVIE FILES
for i in range(0, 12):
    indexed_keywords_12.append(all_indexed_keywords[i])

# MAIN APPLICATION TO RUN
app = gui(all_indexed_keywords, movie_imgs)


"""

TESTING SECTION BELOW

"""


#6 MOVIE FILES
#app = gui(indexed_keywords_6, movie_imgs)

# 12 MOVIE FILES
#app = gui(indexed_keywords_12, movie_imgs)

# ALL 22 MOVIE FILES
#app = gui(all_indexed_keywords, movie_imgs)

"""
COMMENT OUT OTHER TESTS BEFORE RUNNING - TETSING WITH QUEUE
VARIABLE 'all_indexed_keywords' AND 'result_list_test_queue' AS QUEUES

"""
#result_list_test_queue = []
#for i in range(len(all_indexed_keywords)):
#    alist = all_indexed_keywords.pop(0)
#    start_queue = time.time()
#    output = binary_search(alist, 0, len(alist)-1, "spider")
#    end_queue = time.time()
#    if type(output) is str:
#        result_list_test_queue.append(output)
#print(f"Queue performance time: {(end_queue-start_queue)}")


"""

COMMENT OUT OTHER TESTS BEFORE - TETSING WITH STACK
VARIABLE 'all_indexed_keywords' AND 'result_list_test_stack' AS STACKS

"""

result_list_test_stack = []
for i in range(len(all_indexed_keywords)):
    blist = all_indexed_keywords.pop()
    start_stack = time.time()
    boutput = binary_search(blist, 0, len(blist)-1, "spider")
    end_stack = time.time()
    if type(boutput) is str:
        result_list_test_stack.append(boutput)
print(f"Stack performance time: {(end_stack-start_stack)}")











    




