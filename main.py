import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QApplication, QGridLayout, QPushButton, QFormLayout, \
    QListWidget, QListWidgetItem, QGroupBox, QHBoxLayout, QCheckBox

from db import Database
from currency import Currency


class MainWindow(QWidget):

    def index_changed(self, _: QListWidgetItem):  # Not an index, i is a QListWidgetItem
        # print(i.text())

        print(self.part_list.currentIndex().row(), 'selected index')

    def text_changed(self, s: str):
        print(s)

    def __init__(self):
        super().__init__()

        self.db = Database()

        self.setWindowTitle('part manager'.title())

        left, top, width, height = (10, 10, 640, 450)

        self.setGeometry(left, top, width, height)

        outer_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        middle_layout = QGridLayout()
        bottom_layout = QGridLayout()

        self.part_list = QListWidget()
        part_list = self.part_list
        part_list.addItem(f'4BG DDR4 RAM/ John Doe/ Samsung/ {Currency.format_currency(160)}')
        part_list.addItem(f'Asus Mobo/ Mike Smith/ Asus/ {Currency.format_currency(210)}')
        part_list.currentItemChanged.connect(self.index_changed)
        part_list.currentTextChanged.connect(self.text_changed)

        group_box_order_details = QGroupBox('order details')
        group_box_layout = QFormLayout()

        group_box_layout.addRow('part name'.title(), QLineEdit())
        group_box_layout.addRow('retailer'.title(), QLineEdit())
        group_box_layout.addRow('price'.title(), QLineEdit())
        group_box_layout.addRow('quantity'.title(), QLineEdit())

        group_box_customer = QGroupBox('customer details')
        group_box_layout_customer = QFormLayout()
        group_box_layout_customer.addRow('customer'.title(), QLineEdit())

        group_box_order_details.setLayout(group_box_layout)
        group_box_customer.setLayout(group_box_layout_customer)

        top_layout.addWidget(group_box_order_details)
        top_layout.addWidget(group_box_customer)

        middle_layout.addWidget(part_list)

        btn_add_part = QPushButton('add part'.title())
        btn_remove_part = QPushButton('remove part'.title())
        btn_update_part = QPushButton('update part'.title())
        btn_clear_part = QPushButton('clear part'.title())

        bottom_layout.addWidget(btn_add_part, 0, 0)
        bottom_layout.addWidget(btn_remove_part, 0, 1)
        bottom_layout.addWidget(btn_update_part, 0, 2)
        bottom_layout.addWidget(btn_clear_part, 0, 3)

        outer_layout.addLayout(top_layout)
        outer_layout.addLayout(middle_layout)
        outer_layout.addLayout(bottom_layout)

        self.setLayout(outer_layout)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
