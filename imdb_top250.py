from PyQt5 import QtWidgets
import sys
import requests
from bs4 import BeautifulSoup

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("IMDB Top 250")
        self.setFixedWidth(600)
        self.setFixedHeight(400)
        self.url = "https://www.imdb.com/chart/top/"
        self.init_ui()
        self.connection()

    def connection(self):
        self.movie_list = list()
        self.rating_list = list()

        response = requests.get(self.url)
        content = response.content

        soup = BeautifulSoup(content, "html.parser")
        movie_title = soup.find_all("td", {"class": "titleColumn"})
        movie_rating = soup.find_all("td", {"class": "ratingColumn imdbRating"})
        for i, j in zip(movie_rating, movie_title):
            i = i.text
            j = j.text

            i = i.strip()
            j = j.strip()

            i = i.replace("\n", "")
            j = j.replace("\n", "")

            self.rating_list.append(i)
            self.movie_list.append(j)


    def init_ui(self):

        self.table = QtWidgets.QTableWidget()

        self.top10 = QtWidgets.QRadioButton("Top 10")
        self.top30 = QtWidgets.QRadioButton("Top 30")
        self.top50 = QtWidgets.QRadioButton("Top 50")
        self.top100 = QtWidgets.QRadioButton("Top 100")

        self.rfirst = QtWidgets.QRadioButton("9.2 - 8.9")
        self.rsecond = QtWidgets.QRadioButton("8.9 - 8.6")
        self.rthird = QtWidgets.QRadioButton("8.6 - 8.3")
        self.rforth = QtWidgets.QRadioButton("8.3 - 8.0")

        top_hbox = QtWidgets.QHBoxLayout()
        top_hbox.addStretch()
        top_hbox.addWidget(self.top10)
        top_hbox.addWidget(self.top30)
        top_hbox.addWidget(self.top50)
        top_hbox.addWidget(self.top100)
        top_hbox.addStretch()

        mid_hbox = QtWidgets.QHBoxLayout()
        mid_hbox.addStretch()
        mid_hbox.addWidget(self.rfirst)
        mid_hbox.addWidget(self.rsecond)
        mid_hbox.addWidget(self.rthird)
        mid_hbox.addWidget(self.rforth)
        mid_hbox.addStretch()

        self.table.setColumnCount(2)
        self.table.setRowCount(251)

        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.table)

        self.showButton = QtWidgets.QPushButton("Show")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addLayout(top_hbox)
        v_box.addStretch()
        v_box.addLayout(mid_hbox)
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addWidget(self.showButton)
        v_box.addStretch()

        self.setLayout(v_box)

        self.showButton.clicked.connect(self.buttonShow)

        self.show()

    def buttonShow(self):

        if self.top10.isChecked() == True:
            self.table.clear()
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
            a = 1
            b = 1
            for i in self.movie_list[0:10]:
                self.table.setItem(a, 0, QtWidgets.QTableWidgetItem(i))
                a += 1

            for i in self.rating_list[0:10]:
                self.table.setItem(b, 1, QtWidgets.QTableWidgetItem(i))
                b += 1

        elif self.top30.isChecked() == True:
            self.table.clear()
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
            a = 1
            b = 1
            for i in self.movie_list[0:30]:
                self.table.setItem(a, 0, QtWidgets.QTableWidgetItem(i))
                a += 1

            for i in self.rating_list[0:30]:
                self.table.setItem(b, 1, QtWidgets.QTableWidgetItem(i))
                b += 1

        elif self.top50.isChecked() == True:
            self.table.clear()
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
            a = 1
            b = 1
            for i in self.movie_list[0:50]:
                self.table.setItem(a, 0, QtWidgets.QTableWidgetItem(i))
                a += 1

            for i in self.rating_list[0:50]:
                self.table.setItem(b, 1, QtWidgets.QTableWidgetItem(i))
                b += 1

        elif self.top100.isChecked() == True:
            self.table.clear()
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
            a = 1
            b = 1
            for i in self.movie_list[0:100]:
                self.table.setItem(a, 0, QtWidgets.QTableWidgetItem(i))
                a += 1

            for i in self.rating_list[0:100]:
                self.table.setItem(b, 1, QtWidgets.QTableWidgetItem(i))
                b += 1

        elif self.rfirst.isChecked() == True:
            self.table.clear()
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
            a = 1
            for i, j in zip(self.movie_list, self.rating_list):

                if float(j) <= 9.2 and float(j) >= 8.9:
                    self.table.setItem(a, 0, QtWidgets.QTableWidgetItem(i))
                    self.table.setItem(a, 1, QtWidgets.QTableWidgetItem(j))
                    a += 1

        elif self.rsecond.isChecked() == True:
            self.table.clear()
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
            a = 1
            for i, j in zip(self.movie_list, self.rating_list):

                if float(j) <= 8.9 and float(j) >= 8.6:
                    self.table.setItem(a, 0, QtWidgets.QTableWidgetItem(i))
                    self.table.setItem(a, 1, QtWidgets.QTableWidgetItem(j))
                    a += 1

        elif self.rthird.isChecked() == True:
            self.table.clear()
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
            a = 1
            for i, j in zip(self.movie_list, self.rating_list):

                if float(j) <= 8.6 and float(j) >= 8.3:
                    self.table.setItem(a, 0, QtWidgets.QTableWidgetItem(i))
                    self.table.setItem(a, 1, QtWidgets.QTableWidgetItem(j))
                    a += 1

        elif self.rforth.isChecked() == True:
            self.table.clear()
            self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Movie"))
            self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Rating"))
            a = 1
            for i, j in zip(self.movie_list, self.rating_list):

                if float(j) <= 8.3 and float(j) >= 8.0:
                    self.table.setItem(a, 0, QtWidgets.QTableWidgetItem(i))
                    self.table.setItem(a, 1, QtWidgets.QTableWidgetItem(j))
                    a += 1

        else:
            j = 1
            x = 1
            for i in self.movie_list:
                self.table.setItem(j, 0, QtWidgets.QTableWidgetItem(i))
                j += 1

            for i in self.rating_list:
                self.table.setItem(x, 1, QtWidgets.QTableWidgetItem(i))
                x += 1



app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())